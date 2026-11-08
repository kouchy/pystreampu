cmake_minimum_required(VERSION 3.15)
cmake_policy(SET CMP0054 NEW)

if (CMAKE_GENERATOR MATCHES "Ninja")
    file(
        WRITE "${CMAKE_BINARY_DIR}/GNUMakeRulesOverwrite.cmake"
            "STRING(REPLACE \"-MD\" \"-MMD\" CMAKE_DEPFILE_FLAGS_C \"\${CMAKE_DEPFILE_FLAGS_C}\")\n"
            "STRING(REPLACE \"-MD\" \"-MMD\" CMAKE_DEPFILE_FLAGS_CXX \"\${CMAKE_DEPFILE_FLAGS_CXX}\")\n"
    )
    set(CMAKE_USER_MAKE_RULES_OVERRIDE "${CMAKE_BINARY_DIR}/GNUMakeRulesOverwrite.cmake" CACHE INTERNAL "")
endif()

project (pystreampu LANGUAGES CXX)

option(INCLUDE_SPU_LIB "Include the StreamPU library inside the AFF3CT library" ON)

#set(CMAKE_INSTALL_LIBDIR streampu)
#set(CMAKE_INSTALL_INCLUDEDIR streampu)

# Enable C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Link with the "Threads library (required to link with streampu after)
set(CMAKE_THREAD_PREFER_PTHREAD ON)
set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)
include(GNUInstallDirs)
#
file(GLOB_RECURSE SRC_FILES ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)
file(GLOB_RECURSE HEADER_FILES ${CMAKE_CURRENT_SOURCE_DIR}/include/*)


#add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/lib/pybind11/)
set(PYBIND11_NEWPYTHON ON)
find_package(pybind11 CONFIG 3.0.4 REQUIRED)
# `pybind11_add_module` is a wrapper of the CMake `add_library` function
pybind11_add_module(_ext MODULE ${CMAKE_CURRENT_SOURCE_DIR}/src/ext.cpp ${SRC_FILES} ${HEADER_FILES})

# Détection free-threaded
execute_process(
    COMMAND "${Python_EXECUTABLE}" -c
        "import sysconfig; print(sysconfig.get_config_var('Py_GIL_DISABLED') or 0)"
    OUTPUT_VARIABLE PY_GIL_DISABLED
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

if(PY_GIL_DISABLED EQUAL 1)
    message(STATUS "Python free-threaded détecté — activation de Py_GIL_DISABLED")
    set_target_properties(_ext PROPERTIES
        COMPILE_DEFINITIONS "Py_GIL_DISABLED"
    )
endif()

# set(pybind11_INCLUDE_DIRS)
if (NOT INCLUDE_SPU_LIB)
        message(STATUS "Using user installed StreamPU library")
        find_package(cpptrace REQUIRED)
        if (NOT cpptrace_FOUND)
                message(FATAL_ERROR "cpptrace library not found")
        endif()
        message(STATUS "Found cpptrace: ${cpptrace_DIR}")
        target_link_libraries(_ext PUBLIC cpptrace::cpptrace)

        if (EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/lib/streampu/cmake/Modules/FindJulia.cmake")
                list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/lib/streampu/cmake/Modules")
                find_package(Julia 1.10.9 QUIET)
        endif()

        find_package(StreamPU CONFIG 1.8.1 REQUIRED)
        if (NOT StreamPU_FOUND)
                message(FATAL_ERROR "StreamPU library not found")
        endif()
        message(STATUS "Found StreamPU: ${StreamPU_DIR}")
        get_target_property(_SPU_DEFS spu::spu-static-lib INTERFACE_COMPILE_DEFINITIONS)
        if (_SPU_DEFS AND "SPU_JULIA" IN_LIST _SPU_DEFS)
                set(SPU_LINK_JULIA ON)
        endif()
        target_link_libraries(_ext PRIVATE spu::spu-static-lib)
else()
        # streampu
        message(STATUS "Including StreamPU sub-project")
        if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/lib/streampu/include/streampu.hpp")
        option(SPU_COMPILE_STATIC_LIB "" ON)
        option(SPU_COMPILE_SHARED_LIB "" OFF)
        # The StreamPU tests are not needed (and not shipped in the sdist)
        option(SPU_TESTS "" OFF)
        # Nor the benchmark executable (StreamPU >= 1.9.3), which would be installed in the wheels
        option(SPU_BENCHMARK "" OFF)
        add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/lib/streampu/)

        message(STATUS "Sub-project found: streampu")
        else()
        message(FATAL_ERROR "streampu can't be found, try to init the submodule with the following cmd:\n"
                                "$ git submodule update --init --recursive")
        endif()

        target_link_libraries(_ext PRIVATE spu-static-lib)

endif()

set(pybind11_INCLUDE_DIRS)

include_directories(_ext PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
set_target_properties(_ext PROPERTIES OUTPUT_NAME _ext
                           POSITION_INDEPENDENT_CODE ON
                           PRIVATE VERSION_INFO=${VERSION_INFO}) #  set -fpic

# Code coverage of the wrapper (ci/coverage-cpp-linux.sh): only `_ext` is instrumented and
# compiled without optimization; StreamPU stays optimized, so that the tests run faster.
# Julia modules (-DSPU_LINK_JULIA=ON): StreamPU finds Julia and links `_ext` with libjulia.
# The installed extension must find libjulia at import time: add its folder to the RPATH
# (JULIA_LIBRARY is a cache variable set by FindJulia in the StreamPU sub-project).
if(SPU_LINK_JULIA AND JULIA_LIBRARY)
    get_filename_component(JULIA_LIBRARY_DIR "${JULIA_LIBRARY}" DIRECTORY)
    message(STATUS "Julia library folder added to the RPATH of _ext: ${JULIA_LIBRARY_DIR}")
    set_property(TARGET _ext APPEND PROPERTY BUILD_RPATH "${JULIA_LIBRARY_DIR}")
    set_property(TARGET _ext APPEND PROPERTY INSTALL_RPATH "${JULIA_LIBRARY_DIR}")
endif()

# CMake package "Julia" for the extensions built against this pyStreamPU (see
# cmake/JuliaConfig.cmake.in): the installed package of StreamPU links Julia::Julia.
if(SPU_LINK_JULIA AND JULIA_INCLUDE_DIR)
    include(CMakePackageConfigHelpers)
    file(STRINGS "${JULIA_INCLUDE_DIR}/julia_version.h" SPU_JULIA_VERSION LIMIT_COUNT 1 REGEX JULIA_VERSION_STRING)
    string(REGEX REPLACE ".*\"([^\"]+)\".*" "\\1" SPU_JULIA_VERSION "${SPU_JULIA_VERSION}")
    string(REGEX MATCH "^[0-9]+\\.[0-9]+\\.[0-9]+" SPU_JULIA_VERSION "${SPU_JULIA_VERSION}")
    set(SPU_JULIA_BINDIR "${JULIA_BINDIR}")
    set(SPU_JULIA_EXECUTABLE "${JULIA_EXECUTABLE}")
    configure_file("${CMAKE_CURRENT_SOURCE_DIR}/cmake/JuliaConfig.cmake.in"
                   "${CMAKE_CURRENT_BINARY_DIR}/cmake/Julia/JuliaConfig.cmake" @ONLY)
    write_basic_package_version_file("${CMAKE_CURRENT_BINARY_DIR}/cmake/Julia/JuliaConfigVersion.cmake"
                                     VERSION "${SPU_JULIA_VERSION}"
                                     COMPATIBILITY AnyNewerVersion)
    install(FILES "${CMAKE_CURRENT_BINARY_DIR}/cmake/Julia/JuliaConfig.cmake"
                  "${CMAKE_CURRENT_BINARY_DIR}/cmake/Julia/JuliaConfigVersion.cmake"
                  "${CMAKE_CURRENT_SOURCE_DIR}/lib/streampu/cmake/Modules/FindJulia.cmake"
            DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/Julia"
            COMPONENT library)
    message(STATUS "CMake package Julia ${SPU_JULIA_VERSION} installed for the extensions (${JULIA_BINDIR})")
endif()

option(PYSTREAMPU_COVERAGE "Instrument the wrapper (_ext) for gcov code coverage" OFF)
if(PYSTREAMPU_COVERAGE)
    target_compile_options(_ext PRIVATE -O0 -g --coverage)
    target_link_options(_ext PRIVATE --coverage)
    if(TARGET spu-obj)
        target_compile_options(spu-obj PRIVATE -O2)
    endif()
endif()


# Install pybind11 headers
# install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lib/pybind11/include/pybind11
#         DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
#         COMPONENT headers
#         FILES_MATCHING PATTERN "*.h")

install(TARGETS _ext
        DESTINATION .
        EXPORT pystreampu-config
        COMPONENT library)

install(EXPORT
        pystreampu-config
        DESTINATION "share/cmake/pystreampu"
        NAMESPACE pyspu::
        COMPONENT library)

install(DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/include/"
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/pystreampu
        COMPONENT headers
        FILES_MATCHING PATTERN "*.hpp")

install(DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/include/"
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/pystreampu
        COMPONENT headers
        FILES_MATCHING PATTERN "*.hxx")
install(DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/include/"
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/pystreampu
        COMPONENT headers
        FILES_MATCHING PATTERN "*.h")

message("############################################################")
message("# CMAKE_BUILD_TYPE : ${CMAKE_BUILD_TYPE}")
message("# CMAKE_CXX_FLAGS : ${CMAKE_CXX_FLAGS}")
message("# SKBUILD_PROJECT_NAME : streampu")
message("############################################################")
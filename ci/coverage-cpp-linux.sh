#!/bin/bash
set -euo pipefail
set -x

WD=$(pwd)

cmake --version
mkdir -p code_coverage_files
mkdir -p code_coverage_report

pip3 install --verbose -Ccmake.define.CMAKE_BUILD_TYPE=Debug \
                       -Ccmake.define.CMAKE_CXX_COMPILER=$CXX \
                       -Ccmake.define.CMAKE_CXX_FLAGS="$CFLAGS" \
                       -Ccmake.define.CMAKE_EXE_LINKER_FLAGS="$LFLAGS" \
                       -Ccmake.define.SPU_OVERRIDE_VERSION=v0.0.0 \
                       -Ccmake.define.CMAKE_CXX_FLAGS_DEBUG="-O0" -e $WD

# Run tests to execute C++ extension code paths and generate gcda files.
python3 -m pytest tests --junitxml=report-cpp.xml

# The build folder depends on the interpreter (build-dir = "build/{wheel_tag}" in pyproject.toml)
EXT_OBJ_DIR=$(ls -d build/*/CMakeFiles/_ext.dir/src | head -n 1)
lcov --capture --directory "${EXT_OBJ_DIR}" \
     --output-file code_coverage_files/_ext.info \
     --ignore-errors inconsistent \
     --no-external \
     --rc geninfo_unexecuted_blocks=1

rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi

lcov --extract code_coverage_files/_ext.info \
     "$WD/src/*" "$WD/include/*" "*/src/*" "*/include/*" \
     --output-file code_coverage_files/_ext_clean.info \
     --ignore-errors inconsistent,empty

rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi

lcov_cobertura code_coverage_files/_ext_clean.info --output code_coverage_report/streampu-cpp.xml

#!/bin/bash
set -euo pipefail
set -x

WD=$(pwd)

cmake --version
mkdir -p code_coverage_files
mkdir -p code_coverage_report

# Compile with all the cores
export CMAKE_BUILD_PARALLEL_LEVEL="${CMAKE_BUILD_PARALLEL_LEVEL:-$(nproc)}"

# PYSTREAMPU_COVERAGE (CMakeLists.txt): only the wrapper is instrumented, StreamPU is
# compiled with -O2. Debug build type: no LTO, which does not mix well with gcov.
pip3 install --verbose -Ccmake.define.CMAKE_BUILD_TYPE=Debug \
                       -Ccmake.define.CMAKE_CXX_COMPILER=$CXX \
                       -Ccmake.define.CMAKE_CXX_FLAGS="$CFLAGS" \
                       -Ccmake.define.PYSTREAMPU_COVERAGE=ON \
                       -Ccmake.define.SPU_OVERRIDE_VERSION=v0.0.0 \
                       -Ccmake.define.CMAKE_CXX_FLAGS_DEBUG="-O0" -e $WD

# Run tests to execute C++ extension code paths and generate gcda files.
# Several processes (pytest-xdist): gcov merges the counters of the processes safely.
python3 -m pytest tests -n "${PYTEST_WORKERS:-4}" --junitxml=report-cpp.xml --durations=10

# The build folder depends on the interpreter (build-dir = "build/{wheel_tag}" in pyproject.toml)
EXT_OBJ_DIR=$(ls -d build/*/CMakeFiles/_ext.dir/src | head -n 1)
N_GCDA=$(find "${EXT_OBJ_DIR}" -name "*.gcda" | wc -l)
echo "${N_GCDA} .gcda files in ${EXT_OBJ_DIR}"
if [[ ${N_GCDA} -eq 0 ]]; then
    echo "No coverage data in the build folder. .gcda files found elsewhere:" >&2
    find "$WD" -name "*.gcda" -not -path "*/venv/*" | head -n 20 >&2
    exit 1
fi
# lcov 2.x can process the .gcda files in parallel
LCOV_JOBS=()
if lcov --version | grep -q -E "version 2\."; then LCOV_JOBS=(--parallel "$(nproc)"); fi

# --base-directory: with --no-external, only the files under the repository are kept
# (by default, everything outside the build folder, our sources included, is dropped).
lcov --capture --directory "${EXT_OBJ_DIR}" \
     --base-directory "$WD" \
     --output-file code_coverage_files/_ext.info \
     --ignore-errors inconsistent,unused \
     --no-external \
     --exclude "$WD/venv/*" --exclude "$WD/lib/*" \
     --rc geninfo_unexecuted_blocks=1 \
     "${LCOV_JOBS[@]}"

rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi

lcov --extract code_coverage_files/_ext.info \
     "$WD/src/*" "$WD/include/*" \
     --output-file code_coverage_files/_ext_clean.info \
     --ignore-errors inconsistent,empty

rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi

lcov_cobertura code_coverage_files/_ext_clean.info --output code_coverage_report/streampu-cpp.xml

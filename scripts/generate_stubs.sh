#!/usr/bin/env bash
# Generate the type stubs (.pyi) of the compiled extension `streampu._ext`.
#
# The stubs describe the classes and functions implemented in C++ (Socket, Task, Module,
# Stateless, probes...). They are used by the API reference (mkdocstrings reads them
# instead of importing the compiled module) and by IDEs for autocompletion.
#
# Usage, from any folder, in an environment where `streampu` is installed:
#     pip install pybind11-stubgen
#     scripts/generate_stubs.sh
# Run it each time the C++ bindings change, then commit the folder `streampu/_ext/`.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${ROOT}/streampu/_ext"
WORK="$(mktemp -d)"
trap 'rm -rf "${WORK}"' EXIT

if ! python -c "import pybind11_stubgen" 2>/dev/null; then
    echo "pybind11-stubgen is not installed: pip install pybind11-stubgen" >&2
    exit 1
fi

# Run from a temporary folder: from the root of the repository, `import streampu` would
# load the sources of the repository, which do not contain the compiled `_ext` module.
cd "${WORK}"
if ! python -c "import streampu._ext" 2>/dev/null; then
    echo "streampu is not installed in this environment (pip install .)" >&2
    exit 1
fi

# Some default values cannot be written in Python (e.g. `stream=sys.stdout` bound from
# C++): such errors are ignored and reported in stubgen.log.
python -m pybind11_stubgen streampu._ext --output-dir "${WORK}/out" --ignore-all-errors \
    > "${WORK}/stubgen.log" 2>&1 || { cat "${WORK}/stubgen.log"; exit 1; }

rm -rf "${DEST}" "${DEST}.pyi"
if [[ -d "${WORK}/out/streampu/_ext" ]]; then
    cp -R "${WORK}/out/streampu/_ext" "${DEST}"
else
    cp "${WORK}/out/streampu/_ext.pyi" "${DEST}.pyi"
fi

# Missing imports and docstring indentation of the Python methods added by streampu
python "${ROOT}/scripts/fix_stubs.py" "${ROOT}/streampu"

# Same formatting as the rest of the package, with the settings of pyproject.toml
# (checked by the CI)
cd "${ROOT}"
if command -v isort >/dev/null; then isort -q streampu/_ext*; fi
if command -v black >/dev/null; then black -q streampu/_ext*; fi

n_errors=$(grep -c -i "error" "${WORK}/stubgen.log" || true)
echo "Stubs written to ${DEST} (${n_errors} ignored error line(s) reported by pybind11-stubgen)."
if [[ "${n_errors}" != "0" ]]; then
    echo "First ignored errors:"
    grep -i "error" "${WORK}/stubgen.log" | head -n 20
fi

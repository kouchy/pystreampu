
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"
CUSTOM_MODULE_SCRIPT="${ROOT_DIR}/examples/custom_python_module/custom_python_module.py"
COMPARE_SCRIPT="${ROOT_DIR}/examples/custom_python_module/compare_csvs.py"

if [[ ! -f "${ROOT_DIR}/env/bin/activate" ]]; then
	echo "Missing virtual environment: ${ROOT_DIR}/env" >&2
	exit 1
fi

if [[ ! -f "${ROOT_DIR}/env314/bin/activate" ]]; then
	echo "Missing virtual environment: ${ROOT_DIR}/env314" >&2
	exit 1
fi

source "${ROOT_DIR}/env/bin/activate"
python "${CUSTOM_MODULE_SCRIPT}" --csv "${ROOT_DIR}/durations_312.csv"
python "${CUSTOM_MODULE_SCRIPT}" --csv "${ROOT_DIR}/durations_312_cpp.csv" --cpp

deactivate
source "${ROOT_DIR}/env314/bin/activate"
PYTHON_GIL=0 python "${CUSTOM_MODULE_SCRIPT}" --csv "${ROOT_DIR}/durations_314t_ng.csv"
PYTHON_GIL=0 python "${CUSTOM_MODULE_SCRIPT}" --csv "${ROOT_DIR}/durations_314t_ng_cpp.csv" --cpp
PYTHON_GIL=1 python "${CUSTOM_MODULE_SCRIPT}" --csv "${ROOT_DIR}/durations_314t_wg.csv"
PYTHON_GIL=1 python "${CUSTOM_MODULE_SCRIPT}" --csv "${ROOT_DIR}/durations_314t_wg_cpp.csv" --cpp

# Figure of the documentation (guides/python_module.md). The C++ variants run the same
# C++ code whatever the interpreter: only one of them is plotted.
python "${COMPARE_SCRIPT}" \
	--output "${ROOT_DIR}/docs/assets/python_module_comparison.png" \
	--title "10,000 executions of a downsampler, by number of threads" --log \
	"${ROOT_DIR}/durations_312.csv" "${ROOT_DIR}/durations_314t_ng.csv" \
	"${ROOT_DIR}/durations_314t_wg.csv" "${ROOT_DIR}/durations_312_cpp.csv" \
	--labels "Python 3.12, GIL" "Python 3.14t, no GIL" "Python 3.14t, GIL" "C++ modules"


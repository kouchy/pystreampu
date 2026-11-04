#!/usr/bin/env bash
# Format and check the Python code with isort, black and flake8, like the CI does.
#
# Usage, from any folder, in an environment with the dev dependencies (pip install -e '.[dev]'):
#     scripts/lint.sh           # format the code in place (isort, black), then run flake8
#     scripts/lint.sh --check   # only check, without modifying anything (what the CI runs)
#
# The settings come from pyproject.toml (isort, black) and .flake8.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"

# Folders checked by the CI (.gitlab-ci.yml, jobs isort, black and flake8)
PATHS=(streampu examples)

mode="fix"
if [[ "${1:-}" == "--check" ]]; then
    mode="check"
elif [[ $# -gt 0 ]]; then
    echo "usage: $0 [--check]" >&2
    exit 2
fi

for tool in isort black flake8; do
    if ! command -v "${tool}" >/dev/null; then
        echo "${tool} is not installed: pip install -e '.[dev]'" >&2
        exit 1
    fi
done

status=0
run() {
    echo "--> $*"
    "$@" || status=1
}

if [[ "${mode}" == "check" ]]; then
    run isort --check-only --diff "${PATHS[@]}"
    run black --check --diff "${PATHS[@]}"
else
    run isort "${PATHS[@]}"
    run black "${PATHS[@]}"
fi
run flake8 "${PATHS[@]}"

if [[ ${status} -eq 0 ]]; then
    echo "All checks passed."
else
    echo "Some checks failed." >&2
fi
exit ${status}

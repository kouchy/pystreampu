#!/usr/bin/env bash
# Build the task-graph figures of the documentation from their TikZ sources.
#
# The sources are docs/assets/Tex_files/<name>.tex. They are drawn with the TikZ library
# pgflibrarystreampu (https://github.com/kouchy/pgflibrarystreampu, copied in the same
# folder) and converted to docs/assets/<name>.svg, with the text converted to paths so
# that the figures look the same in every browser.
#
# Requires a LaTeX distribution providing `latex` and `dvisvgm`.
#
# Usage:
#     scripts/build_figures.sh               # build all the figures
#     scripts/build_figures.sh index_graph   # build some figures only
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="${ROOT}/docs/assets/Tex_files"
DEST="${ROOT}/docs/assets"
WORK="$(mktemp -d)"
trap 'rm -rf "${WORK}"' EXIT

for tool in latex dvisvgm kpsewhich; do
    command -v "${tool}" >/dev/null || { echo "${tool} is not installed (LaTeX distribution required)" >&2; exit 1; }
done

# pgflibrarystreampu loads the fonts Libertine, newtxmath and Inconsolata. When they are
# not installed, replace them by TeX Gyre fonts, so that the figures can still be built.
mkdir -p "${WORK}/stubs"
if ! kpsewhich libertine.sty >/dev/null; then
    echo "warning: libertine.sty not found, replaced by TeX Gyre Heros" >&2
    printf '%s\n' '\ProvidesPackage{libertine}' '\RequirePackage{ifthen}' '\RequirePackage{tgheros}' \
        '\renewcommand{\familydefault}{\sfdefault}' > "${WORK}/stubs/libertine.sty"
fi
if ! kpsewhich newtxmath.sty >/dev/null; then
    echo "warning: newtxmath.sty not found, default math font used" >&2
    printf '%s\n' '\ProvidesPackage{newtxmath}' > "${WORK}/stubs/newtxmath.sty"
fi
if ! kpsewhich inconsolata.sty >/dev/null; then
    echo "warning: inconsolata.sty not found, replaced by TeX Gyre Cursor" >&2
    printf '%s\n' '\ProvidesPackage{inconsolata}' '\RequirePackage{tgcursor}' > "${WORK}/stubs/inconsolata.sty"
fi

if [[ $# -gt 0 ]]; then
    names=("$@")
else
    names=()
    for f in "${SRC}"/*.tex; do
        [[ "${f}" == *.code.tex ]] && continue
        names+=("$(basename "${f}" .tex)")
    done
fi

for name in "${names[@]}"; do
    [[ -f "${SRC}/${name}.tex" ]] || { echo "${SRC}/${name}.tex not found" >&2; exit 1; }
    echo "--> ${name}"
    # The dvisvgm driver of PGF produces native SVG (patterns of the sockets...)
    if ! (cd "${WORK}" && TEXINPUTS="${SRC}:${WORK}/stubs:" latex -interaction=nonstopmode -halt-on-error \
            -jobname="${name}" "\def\pgfsysdriver{pgfsys-dvisvgm.def}\input{${name}}" > "${name}.out" 2>&1); then
        grep -A 5 "^!" "${WORK}/${name}.out" >&2 || tail -n 30 "${WORK}/${name}.out" >&2
        exit 1
    fi
    dvisvgm --no-fonts --exact-bbox --page=1 "${WORK}/${name}.dvi" -o "${DEST}/${name}.svg" > "${WORK}/${name}.dvisvgm" 2>&1 \
        || { cat "${WORK}/${name}.dvisvgm" >&2; exit 1; }
    echo "    ${DEST}/${name}.svg"
done

#!/usr/bin/env python3
"""Prepare the integration of the next version of StreamPU in pyStreamPU.

Run by the scheduled pipeline `update-streampu` (.gitlab-ci.yml). When StreamPU has a
version newer than the one embedded (`SPU_OVERRIDE_VERSION` in pyproject.toml), it:

1. analyses the changes of StreamPU between the two versions (public headers, classes,
   CMake options, dependencies) and writes an integration plan;
2. creates the branch `streampu-X.Y.Z`: submodule on the new tag, `SPU_OVERRIDE_VERSION`,
   table of versions in docs/install.md;
3. opens a merge request whose description is the plan: a ready merge request when only
   the internals of StreamPU change, a draft when its API or its build options change.

Versions are integrated one at a time (the next tag, not the latest), and each minor
version of pyStreamPU follows one minor version of StreamPU. The new version of pyStreamPU
is computed from its latest tag, as pyStreamPU also has releases of its own: a patch of
StreamPU gives the next patch of pyStreamPU, a minor version of StreamPU gives the next
minor version of pyStreamPU.

Usage:
    python ci/update_streampu.py --dry-run            # print the plan, change nothing
    python ci/update_streampu.py --dry-run --from v1.9.4 --to v1.10.0
    python ci/update_streampu.py                      # in the CI (needs STREAMPU_BOT_TOKEN)

Only the standard library is used.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBMODULE = "lib/streampu"
PYPROJECT = os.path.join(ROOT, "pyproject.toml")
INSTALL_DOC = os.path.join(ROOT, "docs", "install.md")
OUR_CMAKE = os.path.join(ROOT, "CMakeLists.txt")
VERSION_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")
OVERRIDE_RE = re.compile(r'(cmake\.define\.SPU_OVERRIDE_VERSION\s*=\s*")(v[0-9.]+)(")')
OPTION_RE = re.compile(r'^\s*option\(\s*(\w+)\s+"([^"]*)"\s+(\w+)\s*\)', re.M)


def run(cmd, cwd=ROOT, check=True):
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and res.returncode != 0:
        sys.exit(f"command failed: {' '.join(cmd)}\n{res.stdout}{res.stderr}")
    return res.stdout.strip()


def parse(tag):
    m = VERSION_RE.match(tag)
    return tuple(int(x) for x in m.groups()) if m else None


def fmt(v):
    return "v{}.{}.{}".format(*v)


# --------------------------------------------------------------------------- versions
def current_streampu():
    m = OVERRIDE_RE.search(open(PYPROJECT, encoding="utf-8").read())
    if not m:
        sys.exit("SPU_OVERRIDE_VERSION not found in pyproject.toml")
    return m.group(2)


def streampu_tags(url):
    out = run(["git", "ls-remote", "--tags", "--refs", url])
    tags = [line.split("refs/tags/")[1] for line in out.splitlines() if "refs/tags/" in line]
    return sorted((t for t in tags if parse(t)), key=parse)


def next_streampu(current, tags):
    newer = [t for t in tags if parse(t) > parse(current)]
    return newer[0] if newer else None


def latest_pystreampu():
    run(["git", "fetch", "--tags", "--quiet", "origin"], check=False)
    tags = [t for t in run(["git", "tag", "--list", "v*"]).split() if parse(t)]
    return max(tags, key=parse) if tags else None


def next_pystreampu(py_latest, spu_old, spu_new):
    if py_latest is None:
        return None
    major, minor, patch = parse(py_latest)
    if parse(spu_new)[:2] != parse(spu_old)[:2]:  # new minor (or major) version of StreamPU
        return fmt((major, minor + 1, 0))
    return fmt((major, minor, patch + 1))


# --------------------------------------------------------------------------- analysis
def git_sub(*args, check=True):
    return run(["git", "-C", os.path.join(ROOT, SUBMODULE), *args], check=check)


def options(cmake_text):
    return {m.group(1): (m.group(3).upper(), m.group(2)) for m in OPTION_RE.finditer(cmake_text)}


def analyse(old, new):
    git_sub("fetch", "--tags", "--quiet", "origin")
    if git_sub("rev-parse", "--is-shallow-repository") == "true":
        git_sub("fetch", "--unshallow", "--quiet", "origin")

    a = {}
    a["commits"] = git_sub("log", "--oneline", "--no-merges", f"{old}..{new}").splitlines()
    status = git_sub("diff", "--name-status", old, new, "--", "include", "src", "CMakeLists.txt", "cmake")
    files = [line.split("\t") for line in status.splitlines() if line]
    a["headers_added"] = [f[-1] for f in files if f[0].startswith("A") and f[-1].startswith("include/")]
    a["headers_removed"] = [f[1] for f in files if f[0].startswith("D") and f[1].startswith("include/")]
    a["headers_modified"] = [f[-1] for f in files if f[0][0] in "MR" and f[-1].startswith("include/")]
    a["sources_changed"] = [f[-1] for f in files if f[-1].startswith("src/")]

    diff = git_sub("diff", old, new, "--", "include")
    cls = re.compile(r"^([+-])\s*(?:template\s*<[^>]*>\s*)?class\s+(\w+)\b(?![^;{]*;)")
    a["classes_added"], a["classes_removed"] = [], []
    for line in diff.splitlines():
        m = cls.match(line)
        if m and not line.startswith(("+++", "---")):
            (a["classes_added"] if m.group(1) == "+" else a["classes_removed"]).append(m.group(2))
    common = set(a["classes_added"]) & set(a["classes_removed"])  # moved or reformatted
    a["classes_added"] = sorted(set(a["classes_added"]) - common)
    a["classes_removed"] = sorted(set(a["classes_removed"]) - common)

    opt_old = options(git_sub("show", f"{old}:CMakeLists.txt"))
    opt_new = options(git_sub("show", f"{new}:CMakeLists.txt"))
    a["options_added"] = {k: v for k, v in opt_new.items() if k not in opt_old}
    a["options_removed"] = sorted(k for k in opt_old if k not in opt_new)
    a["options_changed"] = {
        k: (opt_old[k][0], v[0]) for k, v in opt_new.items() if k in opt_old and opt_old[k][0] != v[0]
    }

    cmake_diff = git_sub("diff", old, new, "--", "CMakeLists.txt")
    a["dependencies_added"] = sorted(
        {m.group(1) for m in re.finditer(r"^\+\s*find_package\(\s*(\w+)", cmake_diff, re.M)}
    )
    ours = open(OUR_CMAKE, encoding="utf-8").read()
    a["options_to_set"] = [
        k for k, (default, _) in a["options_added"].items() if default == "ON" and f"option({k} " not in ours
    ]
    a["big"] = bool(
        a["headers_added"]
        or a["headers_removed"]
        or a["classes_added"]
        or a["classes_removed"]
        or a["options_added"]
        or a["options_removed"]
        or a["dependencies_added"]
    )
    a["notes"] = release_notes(new)
    return a


def release_notes(tag):
    url = f"https://api.github.com/repos/aff3ct/streampu/releases/tags/{tag}"
    try:
        req = urllib.request.Request(
            url, headers={"Accept": "application/vnd.github+json", "User-Agent": "pystreampu-ci"}
        )
        with urllib.request.urlopen(req, timeout=20) as r:
            return (json.load(r).get("body") or "").strip()
    except (urllib.error.URLError, TimeoutError, ValueError):
        return ""


# --------------------------------------------------------------------------- plan
def plan(old, new, py_new, a):
    def items(title, values):
        return [f"- {title}:"] + [f"  - `{v}`" for v in values] if values else []

    kind = (
        "**Draft**: StreamPU changes its API or its build options"
        if a["big"]
        else ("Ready: only the internals of StreamPU change, the API used by the wrapper is the same")
    )
    out = [
        f"## Update StreamPU from {old} to {new}",
        "",
        f"pyStreamPU version after the merge: **{py_new or '?'}**, the next version when this merge request "
        "was created. If another version of pyStreamPU has been tagged since, take the next one instead and "
        "update the table of `docs/install.md`.",
        "",
        kind + ".",
        "",
        "Done by the bot: submodule `lib/streampu` on the new tag, `SPU_OVERRIDE_VERSION` in "
        "`pyproject.toml`, table of versions in `docs/install.md`.",
        "",
        "### Changes of StreamPU",
        "",
    ]
    out += [f"- {c}" for c in a["commits"]] or ["- (no commit)"]
    if a["notes"]:
        out += ["", "<details><summary>Release notes</summary>", "", a["notes"], "", "</details>"]
    out += ["", "### Analysis", ""]
    analysis = (
        items("New public headers", a["headers_added"])
        + items("Removed public headers", a["headers_removed"])
        + items("Modified public headers", a["headers_modified"])
        + items("New classes", a["classes_added"])
        + items("Removed classes", a["classes_removed"])
        + items("New CMake options", [f"{k} (default {v[0]}): {v[1]}" for k, v in a["options_added"].items()])
        + items("Removed CMake options", a["options_removed"])
        + items("CMake options with a new default", [f"{k}: {o} -> {n}" for k, (o, n) in a["options_changed"].items()])
        + items("New dependencies (find_package)", a["dependencies_added"])
    )
    out += analysis or ["- Public headers and CMake options unchanged."]
    if a["sources_changed"]:
        out += ["", f"{len(a['sources_changed'])} source file(s) of StreamPU changed (internal)."]

    todo = []
    for k in a["options_to_set"]:
        todo.append(
            f"Decide whether `{k}` (ON by default) is needed; if not, add "
            f'`option({k} "" OFF)` next to `SPU_TESTS` in `CMakeLists.txt`.'
        )
    if a["classes_added"] or a["headers_added"]:
        todo.append(
            "Decide which new classes to expose in Python, write their bindings "
            "(`src/wrapper`, `include/wrapper`), tests and documentation."
        )
    if a["classes_removed"] or a["headers_removed"] or a["options_removed"]:
        todo.append("Remove or adapt the bindings of what StreamPU removed.")
    if a["headers_modified"]:
        todo.append(
            "Check that the modified headers do not change a wrapped signature " "(the CI build fails if they do)."
        )
    todo.append("Regenerate the stubs if the bindings change (`scripts/generate_stubs.sh`).")
    todo.append(
        f"Check that `{py_new or 'the new version'}` is still the next version of pyStreamPU "
        "(table of `docs/install.md`)."
    )
    todo.append(f"After the merge (squash), tag `develop` with `{py_new or 'the new version'}`.")
    out += ["", "### To do", ""] + [f"- [ ] {t}" for t in todo]
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- changes
def update_files(old, new, py_new):
    text = open(PYPROJECT, encoding="utf-8").read()
    open(PYPROJECT, "w", encoding="utf-8").write(OVERRIDE_RE.sub(rf"\g<1>{new}\g<3>", text, count=1))

    if not os.path.exists(INSTALL_DOC) or py_new is None:
        return False
    doc = open(INSTALL_DOC, encoding="utf-8").read()
    sep = re.search(r"^\| pyStreamPU \(from\) \| StreamPU \|\n\|[-| ]+\|\n", doc, re.M)
    if not sep:
        return False
    row = f"| {py_new[1:]:<17} | {new[1:]:<8} |\n"
    doc = doc[: sep.end()] + row + doc[sep.end() :]
    if parse(new)[:2] != parse(old)[:2]:  # sentence about the series
        p = parse(py_new)
        doc = re.sub(
            r"pyStreamPU \d+\.\d+\.x follows StreamPU \d+\.\d+\.x",
            f"pyStreamPU {p[0]}.{p[1]}.x follows StreamPU {parse(new)[0]}.{parse(new)[1]}.x",
            doc,
        )
    open(INSTALL_DOC, "w", encoding="utf-8").write(doc)
    return True


def gitlab_api(method, path, data=None):
    url = f"{os.environ['CI_API_V4_URL']}/projects/{os.environ['CI_PROJECT_ID']}{path}"
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(
        url,
        data=body,
        method=method,
        headers={"PRIVATE-TOKEN": os.environ["STREAMPU_BOT_TOKEN"], "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--dry-run", action="store_true", help="print the plan, change nothing")
    parser.add_argument("--from", dest="from_", help="embedded StreamPU tag (default: SPU_OVERRIDE_VERSION)")
    parser.add_argument("--to", help="StreamPU tag to integrate (default: the next one)")
    parser.add_argument("--plan-file", default="streampu-update-plan.md")
    args = parser.parse_args()

    url = run(["git", "config", "-f", ".gitmodules", f"submodule.{SUBMODULE}.url"])
    old = args.from_ or current_streampu()
    new = args.to or next_streampu(old, streampu_tags(url))
    if new is None:
        print(f"StreamPU {old} is the latest version: nothing to do.")
        return
    branch = f"streampu-{new[1:]}"
    print(f"StreamPU: {old} -> {new} (branch {branch})")

    if not args.dry_run and run(["git", "ls-remote", "--heads", "origin", branch]):
        print(f"The branch {branch} already exists: nothing to do.")
        return

    py_new = next_pystreampu(latest_pystreampu(), old, new)
    a = analyse(old, new)
    text = plan(old, new, py_new, a)
    open(os.path.join(ROOT, args.plan_file), "w", encoding="utf-8").write(text)
    print(text)
    if args.dry_run:
        return

    for var in ("STREAMPU_BOT_TOKEN", "CI_API_V4_URL", "CI_PROJECT_ID", "CI_SERVER_HOST", "CI_PROJECT_PATH"):
        if not os.environ.get(var):
            sys.exit(f"{var} is not set (see .gitlab-ci.yml, job update-streampu)")
    target = os.environ.get("CI_DEFAULT_BRANCH", "develop")

    run(["git", "checkout", "-B", branch])
    git_sub("checkout", "--quiet", new)
    run(["git", "submodule", "update", "--init", "--recursive", "--quiet"], cwd=os.path.join(ROOT, SUBMODULE))
    doc_updated = update_files(old, new, py_new)
    run(["git", "add", SUBMODULE, "pyproject.toml"] + (["docs/install.md"] if doc_updated else []))
    run(
        [
            "git",
            "-c",
            "user.name=pyStreamPU bot",
            "-c",
            "user.email=noreply@" + os.environ["CI_SERVER_HOST"],
            "commit",
            "--quiet",
            "-m",
            f"Update StreamPU to {new}",
        ]
    )
    env = os.environ
    remote = f"https://oauth2:{env['STREAMPU_BOT_TOKEN']}@{env['CI_SERVER_HOST']}/{env['CI_PROJECT_PATH']}.git"
    # ci.skip: no branch pipeline, the merge request pipeline runs when the merge request is created
    run(["git", "push", "--quiet", "-o", "ci.skip", remote, f"HEAD:refs/heads/{branch}"])

    mr = gitlab_api(
        "POST",
        "/merge_requests",
        {
            "source_branch": branch,
            "target_branch": target,
            "title": ("Draft: " if a["big"] else "") + f"Update StreamPU to {new}",
            "description": text,
            "remove_source_branch": True,
            "squash": True,
            "labels": "streampu-update",
        },
    )
    print("Merge request:", mr.get("web_url"))


if __name__ == "__main__":
    main()

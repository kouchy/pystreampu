# Development guidelines

## Install for development

Install the package in editable mode with the development dependencies (`isort`,
`black`, `flake8`, `pytest`, `pybind11-stubgen`, `pre-commit`) and the documentation
dependencies:

```bash
pip install -ve '.[dev,docs]'
```

## Code formatting and linting

The Python code of `streampu/` and `examples/` is formatted with
[isort](https://pycqa.github.io/isort/) and [black](https://black.readthedocs.io/), and
checked with [flake8](https://flake8.pycqa.org/). Their settings are in
`pyproject.toml` and `.flake8`. The CI rejects code that does not pass these checks.

The script `scripts/lint.sh` runs the three tools:

```bash
scripts/lint.sh           # format the code in place, then run flake8
scripts/lint.sh --check   # only check, like the CI
```

To run these checks automatically on the modified files at each commit, install the
[pre-commit](https://pre-commit.com/) hooks once:

```bash
pre-commit install
pre-commit run --all-files   # optional: check the whole repository
```

The C++ code of `src/` and `include/` is formatted with clang-format:

```bash
scripts/apply_clang_format.sh
```

## Tests

```bash
pytest tests  # from the root of the repository, with the package installed
```

## Type stubs of the C++ bindings

The folder `streampu/_ext/` contains the type stubs (`.pyi`) of the compiled module
`streampu._ext`. They are used by the API reference and by IDEs. Regenerate them each
time the C++ bindings change, and commit the result:

```bash
scripts/generate_stubs.sh
```

The CI job `stubs` checks that they are up to date.

## Building and publishing the wheels

The wheels are built by GitLab CI on the tags `v*`, or on demand (Build > Pipelines >
Run pipeline):

- `build-wheels-linux` (Linux x86_64) and `sdist` run on the x86 runner;
- `build-wheels-macos` (macOS arm64 and x86_64) and `build-wheels-linux-aarch64` run on
  an Apple Silicon Mac registered as a runner (shell executor, tag `macos-arm64`);
- on a tag, `publish` uploads all of them to TestPyPI, or to PyPI when the variable
  `PYPI_REPOSITORY_URL` is `https://upload.pypi.org/legacy/`.

Setup of the Apple Silicon runner, under a dedicated user account (a standard account,
for example `gitlab-runner`, with no access to personal data):

- with an administrator account: the Xcode command line tools (`xcode-select --install`),
  Rosetta (`softwareupdate --install-rosetta`, to test the x86_64 wheels) and, with
  Homebrew, `brew install python gitlab-runner colima docker` (Python >= 3.11 runs
  cibuildwheel; the commands in `/opt/homebrew/bin` can be used by every account);
- cibuildwheel installs the python.org builds of Python with `sudo installer`: allow it
  without password for the dedicated account, with
  `sudo visudo -f /etc/sudoers.d/gitlab-runner` and the line
  `gitlab-runner ALL=(root) NOPASSWD: /usr/sbin/installer`. Anyone who can run a job on
  this runner then has the rights of root: keep the runner protected and dedicated to
  this project;
- with the dedicated account: register the runner for this project only
  (Settings > CI/CD > Runners > New project runner), with the tag `macos-arm64`, the
  `shell` executor and the option "Protected" (it then only runs the jobs of the
  protected branches and tags). In `~/.gitlab-runner/config.toml`, set `concurrent = 2`
  and, in the `[[runners]]` section,
  `environment = ["PATH=/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"]`
  (the service does not get the PATH of a terminal). Then `gitlab-runner install` and
  `gitlab-runner start`;
- Colima provides the Docker engine of the Linux aarch64 wheels, without a graphical
  session; the job starts it when it is not running (8 CPUs and 16 GB by default, see
  the variables `COLIMA_CPUS` and `COLIMA_MEMORY`). Check once with
  `colima start --arch aarch64` and `docker run --rm hello-world`. If
  `~/.docker/config.json` contains `"credsStore": "desktop"` (left by Docker Desktop),
  remove this line;
- on macOS, `gitlab-runner` runs as a service of the user (LaunchAgent): it only works
  while this account has an open session. Enable the automatic login of the dedicated
  account (System Settings > Users & Groups), so that the runner comes back after a
  restart.

Publication: the masked and protected variable `PYPI_API_TOKEN` holds an API token of
TestPyPI (or PyPI), and the tags `v*` must be protected (Settings > Repository >
Protected tags) so that the job of a tag can read it.

The GitHub workflow `.github/workflows/wheels.yml` only runs on demand and publishes
nothing: it can test the platforms that GitLab does not cover, such as Windows.

## Documentation

The documentation is written in Markdown in `docs/` and built with MkDocs:

```bash
mkdocs serve            # local preview at http://127.0.0.1:8000
mkdocs build --strict   # same check as the CI
```

The task graphs of the documentation (`docs/assets/*.svg`) are drawn with the TikZ
library [pgflibrarystreampu](https://github.com/kouchy/pgflibrarystreampu). Their sources
are in `docs/assets/Tex_files/`; rebuild them with a LaTeX distribution providing `latex`
and `dvisvgm`:

```bash
scripts/build_figures.sh               # all the figures
scripts/build_figures.sh index_graph   # one figure
```

The outputs shown in the examples are written by hand. `scripts/check_tutorial.py` runs
the examples of the documentation and compares their results with these outputs:

```bash
python scripts/check_tutorial.py
```

## Updating StreamPU

Each minor version of pyStreamPU embeds one minor version of StreamPU (see the table of
versions in the [installation page](install.md#versions)). The new versions of StreamPU
are integrated one at a time, by `ci/update_streampu.py`:

- the scheduled pipeline `update-streampu` (variable `STREAMPU_UPDATE=true`) runs it on
  the default branch. When StreamPU has a newer tag than `SPU_OVERRIDE_VERSION`, it
  creates the branch `streampu-X.Y.Z` (submodule, `SPU_OVERRIDE_VERSION`, table of
  versions) and opens a merge request whose description is the integration plan. The
  merge request is a draft when StreamPU changes its public headers, its classes, its
  CMake options or its dependencies;
- after the merge (squash), tag the default branch with the version given in the plan.

pyStreamPU also has releases of its own between two versions of StreamPU (fixes, new
features of the wrapper): the bot computes the new version from the latest tag of
pyStreamPU, so the numbers of pyStreamPU and StreamPU do not have to match.

To see the plan of the next version without changing anything:

```bash
python ci/update_streampu.py --dry-run
python ci/update_streampu.py --dry-run --from v1.9.4 --to v1.10.0   # any two tags
```

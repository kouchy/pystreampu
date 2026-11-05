# Third-party notices

The `streampu` package (pyStreamPU) is released under the MIT License (see `LICENSE`).
Its binary distributions (wheels) also include the following third-party code. The full
text of each license is installed with the package metadata, in the folder
`streampu-<version>.dist-info/licenses/` (paths of the source distribution).

| Component | Included as | License | License file |
|-----------|-------------|---------|--------------|
| [StreamPU](https://github.com/aff3ct/streampu) | static library linked in `streampu/_ext`, headers | MIT | `lib/streampu/LICENSE` |
| [cpptrace](https://github.com/jeremy-rifkin/cpptrace) | static library linked in `streampu/_ext`, headers | MIT | `lib/streampu/lib/cpptrace/LICENSE` |
| [nlohmann/json](https://github.com/nlohmann/json) | headers | MIT | `lib/streampu/lib/json/LICENSE.MIT` |
| [rang](https://github.com/agauniyal/rang) | headers | Unlicense (public domain) | `lib/streampu/lib/rang/LICENSE` |
| [pybind11](https://github.com/pybind/pybind11) | compiled in `streampu/_ext` | BSD-3-Clause | `lib/pybind11/LICENSE` |

The sources of these components are in the folder `lib/` of the source distribution.

# Embedded Project Template

A professional template for embedded C/C++ projects.

This repository defines a clean structure for building, testing, documenting, and delivering embedded software projects. It is intended as a reusable starting point for portfolio projects, freelance assignments, prototypes, and technical demonstrations.

## Goals

The goal of this template is to show how I structure embedded software work in a professional way:

- clear project layout
- reproducible build system
- separation between source, headers, tests, scripts, and documentation
- basic CMake build flow
- automated tests
- GitHub Actions CI
- architecture documentation
- test reporting
- delivery reporting

## Repository Structure

```text
embedded-project-template/
|-- README.md
|-- CMakeLists.txt
|-- include/
|   `-- app.hpp
|-- src/
|   |-- app.cpp
|   `-- main.cpp
|-- tests/
|   `-- test_app.cpp
|-- scripts/
|   `-- run_tests.sh
|-- docs/
|   |-- ARCHITECTURE.md
|   |-- TEST_REPORT.md
|   `-- DELIVERY_REPORT.md
|-- .github/
|   `-- workflows/
|       `-- ci.yml
`-- STYLE_GUIDE.md
```

## Build

```sh
cmake -S . -B build
cmake --build build
```

## Run

On Linux/macOS:

```sh
./build/embedded_project_template
```

On Windows:

```powershell
.\build\Debug\embedded_project_template.exe
```

or sometimes:

```powershell
.\build\embedded_project_template.exe
```

## Test

On Linux/macOS:

```sh
ctest --test-dir build
```

On Windows with Visual Studio:

```powershell
ctest --test-dir build -C Debug --output-on-failure
```

## Documentation

The `docs/` folder contains templates for professional project delivery:

- `ARCHITECTURE.md` - design overview, modules, interfaces, and tradeoffs
- `TEST_REPORT.md` - test strategy, test cases, results, and known limitations
- `DELIVERY_REPORT.md` - final client-style delivery summary

## Intended Use

This template will be reused across future projects such as:

- embedded driver examples
- hardware abstraction layer demos
- Linux userspace services
- sensor/networking projects
- FPGA software-control examples
- test automation projects

## Status

Initial template under development.

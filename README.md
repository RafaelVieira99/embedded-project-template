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
├── README.md
├── CMakeLists.txt
├── src/
│   └── main.cpp
├── include/
│   └── app.hpp
├── tests/
│   └── test_app.cpp
├── scripts/
│   └── run_tests.sh
├── docs/
│   ├── ARCHITECTURE.md
│   ├── TEST_REPORT.md
│   └── DELIVERY_REPORT.md
├── .github/
│   └── workflows/
│       └── ci.yml
└── STYLE_GUIDE.md

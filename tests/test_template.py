"""Pytest template for project-level checks.

Copy this file or extend it when adding Python-based tests such as log parsers,
CLI smoke tests, generated artifact checks, or hardware test automation.
"""

from pathlib import Path
import shutil
import subprocess

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run_command(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=PROJECT_ROOT,
        check=False,
        text=True,
        capture_output=True,
    )


def test_expected_project_files_exist() -> None:
    required_files = [
        "CMakeLists.txt",
        "include/app.hpp",
        "src/app.cpp",
        "tests/test_app.cpp",
    ]

    for relative_path in required_files:
        assert (PROJECT_ROOT / relative_path).is_file(), relative_path


def test_cmake_configure_template() -> None:
    """Example smoke test.

    Enable this test when the CI environment has CMake installed and configure
    checks should be part of the Python test suite.
    """

    if shutil.which("cmake") is None:
        pytest.skip("CMake is not available on PATH")

    result = run_command("cmake", "-S", ".", "-B", "build/pytest-template")
    assert result.returncode == 0, result.stderr

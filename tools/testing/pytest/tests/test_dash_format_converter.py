# *******************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0
#
# SPDX-License-Identifier: Apache-2.0
# *******************************************************************************

import os
import subprocess
import pytest
from pathlib import Path


@pytest.fixture
def temp_files(tmp_path):
    """
    Creates temporary input and output files for the test and returns their paths.
    """
    input_file = tmp_path / "input_file.txt"
    output_file = tmp_path / "formatted.txt"
    return input_file, output_file


@pytest.fixture(scope="session")
def converter_path():
    """
    Determines the correct way to call dash_format_converter.

    - If running inside Bazel, use TEST_SRCDIR to find the `py_binary` target.
    - If running manually, call the Python script directly.
    """
    if "TEST_SRCDIR" in os.environ:
        # Running inside Bazel: Use runfiles to locate the binary
        return os.path.join(
            os.environ["TEST_SRCDIR"],
            "PROJECT_REPO_NAME",  # Change to your actual repo name
            "tools",
            "dash",
            "formatters",
            "dash_format_converter",
        )

    # Running standalone: Use direct Python script execution
    script_path = (
        Path(__file__).parent / "../../tools/dash/formatters/dash_format_converter.py"
    )
    if script_path.exists():
        return f"python3 {script_path}"

    raise FileNotFoundError("Could not find 'dash_format_converter' script or binary.")


def test_requirements_conversion(temp_files, converter_path):
    """
    Tests that dash_format_converter.py correctly converts a simple requirements.txt file.
    """
    input_file, output_file = temp_files

    # Write a sample requirements file
    input_file.write_text("requests==2.28.1\nFlask==2.2.2\n")

    # Invoke the converter with -t requirements
    subprocess.run(
        f"{converter_path} -i {input_file} -o {output_file} -t requirements",
        shell=True,
        check=True,
    )

    # Read the output and verify correctness
    actual = output_file.read_text().splitlines()
    expected = [
        "pypi/pypi/-/requests/2.28.1",
        "pypi/pypi/-/Flask/2.2.2",
    ]
    assert actual == expected, f"Expected {expected} but got {actual}"


def test_cargo_conversion(temp_files, converter_path):
    """
    Tests that dash_format_converter.py correctly converts a sample Cargo.lock file.
    """
    input_file, output_file = temp_files

    # Write a minimal Cargo.lock content in TOML format
    cargo_lock_content = """\
[[package]]
name = "serde"
version = "1.0.123"

[[package]]
name = "reqwest"
version = "0.11.12"
"""
    input_file.write_text(cargo_lock_content)

    # Invoke the converter with -t cargo
    subprocess.run(
        f"{converter_path} -i {input_file} -o {output_file} -t cargo",
        shell=True,
        check=True,
    )

    # Read the output and verify correctness
    actual = output_file.read_text().splitlines()
    expected = [
        "cargo/cargo/-/serde/1.0.123",
        "cargo/cargo/-/reqwest/0.11.12",
    ]
    assert actual == expected, f"Expected {expected} but got {actual}"

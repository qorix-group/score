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

import sys
import tempfile
import os

# Import the main function from your converter.
from tools.dash.formatters.dash_format_converter import (
    main as dash_format_converter_main,
)


def run_converter(input_text: str, converter_args: str) -> list[str]:
    """
    Runs the converter by creating temporary input and output files,
    writing the provided input_text to the input file, and passing the
    file paths to the converter as arguments. Returns the converter's output
    as a list of lines.
    """
    with (
        tempfile.NamedTemporaryFile("w+", delete=False) as input_file,
        tempfile.NamedTemporaryFile("w+", delete=False) as output_file,
    ):
        try:
            # Write input_text to the temporary input file.
            input_file.write(input_text)
            input_file.flush()
            input_path = input_file.name
            output_path = output_file.name

            # Build the full set of arguments.
            # We need to add the required -i and -o arguments.
            extra_args = converter_args.split() + ["-i", input_path, "-o", output_path]
            sys.argv = ["dash_format_converter"] + extra_args

            # Call the converter's main function.
            dash_format_converter_main()

            # Read and return the output file content as a list of lines.
            with open(output_path, "r") as f:
                output_text = f.read()
            return output_text.splitlines()
        finally:
            # Clean up the temporary files.
            os.unlink(input_file.name)
            os.unlink(output_file.name)


def test_requirements_conversion():
    """
    Tests that dash_format_converter.py correctly converts a simple requirements.txt file
    by calling the converter's main function directly.
    """
    input_text = "requests==2.28.1\nFlask==2.2.2\n"
    actual = run_converter(input_text, "-t requirements")
    expected = [
        "pypi/pypi/-/requests/2.28.1",
        "pypi/pypi/-/Flask/2.2.2",
    ]
    assert actual == expected, f"Expected {expected} but got {actual}"


def test_cargo_conversion():
    """
    Tests that dash_format_converter.py correctly converts a sample Cargo.lock file
    by calling the converter's main function directly.
    """
    cargo_lock_content = """\
[[package]]
name = "serde"
version = "1.0.123"

[[package]]
name = "reqwest"
version = "0.11.12"
"""
    actual = run_converter(cargo_lock_content, "-t cargo")
    expected = [
        "cargo/cargo/-/serde/1.0.123",
        "cargo/cargo/-/reqwest/0.11.12",
    ]
    assert actual == expected, f"Expected {expected} but got {actual}"

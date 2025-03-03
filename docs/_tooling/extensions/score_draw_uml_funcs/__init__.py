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
"""
This 'sphinx-extension' is responsible to allow for functional drawings of UML diagrams

    - Features
    - Logical Interfaces
    - Modules
    - Components
    - Component Interfaces

and all applicable linkages between them.

It provides this functionality by adding classes to `needs_render_context`,
which then can be invoked inside 'needarch' and 'needuml' blocks in rst files.
"""

import hashlib
import time
from functools import cache
from pathlib import Path

from sphinx.application import Sphinx  # type: ignore
from sphinx_needs.logging import get_logger  # type: ignore

from score_draw_uml_funcs.helpers import (
    find_interfaces_of_operations,
    gen_alias,
)

logger = get_logger(__file__)


def setup(app: Sphinx) -> dict:
    app.config.needs_render_context = draw_uml_function_context
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


@cache
def scripts_directory_hash():
    start = time.time()
    all = ""
    for file in Path(".devcontainer/sphinx_conf").glob("**/*.py"):
        with open(file) as f:
            all += f.read()
    hash_object = hashlib.sha256(all.encode("utf-8"))
    directory_hash = hash_object.hexdigest()
    logger.info(
        "calculate directory_hash = "
        + directory_hash
        + " within "
        + str(time.time() - start)
        + " seconds."
    )
    return directory_hash


#       ╭──────────────────────────────────────────────────────────────────────────────╮
#       │                           Actual drawing functions                           │
#       ╰──────────────────────────────────────────────────────────────────────────────╯


def draw_component(
    need: dict, all_needs: dict, processed_operations: set[str] | None = None
) -> tuple[str, str, set[str]]:
    """
    Drawing and parsing function of a component.

    Example:
        input:
            need: component_1
            all_needs: all_needs_dict
            processed_operations: set()
        return:
            # Part 1 Structure Text
            component "Component 1" as C1 {
            }
            interface "Component Interface 1" as CI1 {
            real operation 1 ()
            real operation 2 ()
            }

            interface "Logical Interface 1" as LI1 {
            Logical Operation 1
            Logical Operation 2
            }

            interface "Component Interface 3" as CI3 {
            real operation 5 ()
            real operation 6 ()
            }

            # Part 2 Linkage Text
            CI1 --> LI1: implements
            C1 --> CI1: implements
            C1 --> CI3: uses

            # Part 3 Processed Operations
            {
             'real_operation_1',
             'real_operation_6',
             'real_operation_2',
             'real_operation_5',
             'logical_interface_1'
            }


            Note: part 1 and 2 are returned as one text item separated by '\n'.
            They are interpreted and names are shortened here to aid readability.


    Args:
        need: the need that currently should be drawn / traversed
        all_needs: all_needs_dict
        processed_operations: set of processed_operations. Default: None


    Returns:
        Tuple of 3 parts.
        (Structure Text, Linkage Text, Processed Operations)

    """
    processed_operations = processed_operations or set()
    alias = gen_alias(need["title"])
    structure_text = f'component "{need["title"]}" as {alias} {{\n'
    linkage_text = ""

    # Process includes (subcomponents and interfaces)
    for need_inc in need.get("includes", []):
        curr_need = all_needs[need_inc]

        if "component_interface" in need_inc:
            sub_structure, sub_links, processed_operations = draw_component_interface(
                curr_need, all_needs, processed_operations
            )
        elif "component" in need_inc or "sub_component" in need_inc:
            sub_structure, sub_links, processed_operations = draw_component(
                curr_need, all_needs, processed_operations
            )
        else:
            continue

        structure_text += sub_structure
        linkage_text += sub_links

    structure_text += "}\n"

    for relationship_type in ["implements", "uses"]:
        if need.get(relationship_type):
            interface_ids = set()
            for op_id in need[relationship_type]:
                # Determine parent interface for operations
                parent_id = (
                    all_needs[op_id]["includes_back"][0]
                    if "operation" in op_id
                    else op_id
                )
                interface_ids.add(parent_id)

            # Create links
            for iface_id in interface_ids:
                iface_alias = gen_alias(all_needs[iface_id]["title"])
                linkage_text += f"{alias} --> {iface_alias}: {relationship_type}\n"

            # Draw interfaces
            for iface_id in interface_ids:
                curr_need = all_needs[iface_id]
                sub_structure, sub_links, processed_operations = (
                    draw_component_interface(curr_need, all_needs, processed_operations)
                )
                structure_text += sub_structure
                linkage_text += sub_links

    # Remove duplicate links
    linkage_text = "\n".join(set(linkage_text.split("\n"))) + "\n"

    return structure_text, linkage_text, processed_operations


def draw_component_interface(
    need: dict, all_needs: dict, processed_operations: set[str] | None = None
) -> tuple[str, str, set[str]]:
    """
    Parsing and drawing of a component interface.
    If needed it also will follow and draw any linked interfaces

    Example:
        input:
            need: component_interface_3
            all_needs: all_needs_dict
            processed_operations: None
        returns:

            # Part 1 Structure Text
            interface "Component Interface 3" as CI3 {
            real operation 5 ()
            real operation 6 ()
            }

            # Part 2 Linkage Text
            ""

            # Part 3 Processed Operations
            (real_operation_5, real_operation_6)

            Note: part 1 and 2 are returned as one text item separated by '\n'.
            They are interpreted and names are shortened here to aid readability.

    Args:
        need: need that should be parsed / drawn
        all_needs: all_needs_dict
        processed_operations: set of already processed_operations. Default: None

    Returns:
        Tuple of 3 parts.
        (Structure Text, Linkage Text, Processed Operations)

    """
    processed_operations = processed_operations or set()

    # Skip if not an interface
    if "interface" not in need["id"]:
        return "", "", processed_operations

    alias = gen_alias(need["title"])
    interface_text = f'interface "{need["title"]}" as {alias} {{\n'

    # Process unprocessed operations
    new_includes = [inc for inc in need["includes"] if inc not in processed_operations]
    processed_operations.update(new_includes)

    # Add operations as methods
    operation_str = "\n".join(
        all_needs[inc]["title"] for inc in new_includes if "operation" in inc
    )
    interface_text += operation_str + "\n}\n\n"

    # Find and create links to upper interfaces
    linkage_text = ""
    includes_id = [all_needs[inc]["id"] for inc in need["includes"]]
    upper_interfaces = find_interfaces_of_operations(all_needs, includes_id)

    for upper_id in upper_interfaces:
        upper_alias = gen_alias(all_needs[upper_id]["title"])
        linkage_text += f"{alias} --> {upper_alias}: implements\n"

    # Generate text for upper interfaces
    # (like the logical interfaces from the logic ops we are linking to)
    upper_interface_text = "".join(
        gen_interface_text(all_needs[iface_id], all_needs)
        for iface_id in upper_interfaces
        if iface_id not in processed_operations and "interface" in iface_id
    )
    processed_operations.update(
        iface_id for iface_id in upper_interfaces if "interface" in iface_id
    )

    return interface_text + upper_interface_text, linkage_text, processed_operations


def gen_interface_text(need: dict, all_needs: dict) -> str:
    """Generate interface text if it's an actual interface."""
    if "interface" not in need["id"]:
        return ""

    alias = gen_alias(need["title"])
    text = f'interface "{need["title"]}" as {alias} {{\n'
    includes_str = "\n".join(all_needs[inc]["title"] for inc in need["includes"])
    text += includes_str + "\n}\n\n"
    return text


#       ╭──────────────────────────────────────────────────────────────────────────────╮
#       │                    Classes with hashing to enable caching                    │
#       ╰──────────────────────────────────────────────────────────────────────────────╯


class draw_full_feature:
    def __repr__(self):
        return "draw_full_feature" + " in " + scripts_directory_hash()

    def __call__(self, need, all_needs: dict) -> str:
        alias = gen_alias(need["title"])
        structure_text = f'component "{need["title"]}" as {alias} {{\n'
        for need_inc in need.get("includes", []):
            curr_need = all_needs[need_inc]

            structure_text += gen_interface_text(curr_need, all_needs)
        structure_text += "}\n"
        return structure_text


class draw_logical_interface:
    def __repr__(self):
        return "draw_logical_interface" + " in " + scripts_directory_hash()

    def __call__(self, need, all_needs: dict) -> str:
        return gen_interface_text(need, all_needs)


class draw_full_component:
    def __repr__(self):
        return "draw_full_component" + " in " + scripts_directory_hash()

    def __call__(self, need, all_needs) -> str:
        structure_text, linkage_text, processed_operations = draw_component(
            need, all_needs, set()
        )
        return structure_text + "\n" + linkage_text


class draw_full_component_interface:
    def __repr__(self):
        return "draw_full_component_interface" + " in " + scripts_directory_hash()

    def __call__(self, need, all_needs) -> str:
        structure_text, linkage_text, _ = draw_component_interface(
            need, all_needs, set()
        )
        return structure_text + "\n" + linkage_text


class draw_module:
    def __repr__(self):
        return "draw_module" + " in " + scripts_directory_hash()

    def __call__(self, need, all_needs) -> str:
        alias = gen_alias(need["title"])
        module_text = f'component "{need["title"]}" as {alias} {{\n'
        for need_inc in need.get("includes", []):
            curr_need = all_needs[need_inc]
            module_text += draw_full_component().__call__(curr_need, all_needs)
        return module_text


draw_uml_function_context = {
    "draw_logical_interface": draw_logical_interface(),
    "draw_component_interface": draw_full_component_interface(),
    "draw_component": draw_full_component(),
    "draw_module": draw_module(),
    "draw_feature": draw_full_feature(),
}

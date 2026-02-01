"""
Module containing the subcommand 'dims' of stl2scad.

Copyright:
    2026 by Clemens Rabe <clemens.rabe@clemensrabe.de>

    All rights reserved.

    This file is part of stl2scad (https://github.com/seeraven/stl2scad)
    and is released under the "BSD 3-Clause License". Please see the ``LICENSE`` file
    that is included as part of this package.
"""

# -----------------------------------------------------------------------------
# Module Import
# -----------------------------------------------------------------------------
import argparse
import logging
from typing import Any

import stl

from stl_2_scad.stl_helpers import get_stl_bounding_box

# -----------------------------------------------------------------------------
# Module Variables
# -----------------------------------------------------------------------------
DESCRIPTION = """
stl2scad dims
=============

Print the dimensions of a STL object.
"""


# -----------------------------------------------------------------------------
# Argument Parser
# -----------------------------------------------------------------------------
def add_subcommand(subparsers: Any) -> None:
    """Add the subcommand 'dims'."""
    parser = subparsers.add_parser(
        "dims",
        help="Print the dimensions of a STL object.",
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("stl", help="STL file.")
    parser.set_defaults(func=stl2scad_dims)


# -----------------------------------------------------------------------------
# Command
# -----------------------------------------------------------------------------
def stl2scad_dims(args) -> int:
    """Determine the dimensions of the STL object and print them to stdout."""
    logger = logging.getLogger(__name__)
    logger.debug("Executing command stl2scad dims")

    logger.debug("Loading file %s", args.stl)
    try:
        mesh = stl.mesh.Mesh.from_file(args.stl)
    except FileNotFoundError:
        logger.critical("File %s not found.", args.stl)
        return 1

    bbox = get_stl_bounding_box(mesh)
    print(f"X: {bbox[0]} - {bbox[3]}")
    print(f"Y: {bbox[1]} - {bbox[4]}")
    print(f"Z: {bbox[2]} - {bbox[5]}")

    return 0

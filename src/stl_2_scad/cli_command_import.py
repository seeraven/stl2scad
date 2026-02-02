"""
Module containing the subcommand 'import' of stl2scad.

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
from pathlib import Path
from typing import Any

import stl

from stl_2_scad.stl_helpers import get_stl_bounding_box

# -----------------------------------------------------------------------------
# Module Variables
# -----------------------------------------------------------------------------
DESCRIPTION = """
stl2scad import
===============

Generate an OpenSCAD import statement with anchoring support. The anchor
is specified the same way BOSL2 allows to specify an anchor, so all BOSL2
constants like TOP, FORDWARD, etc. can be used. Like BOSL2, the anchor
is internally a vector like [0, 0, 1] specifying the translation from the
center in bounding box units.

Example:
    $ stl2scad import test/data/example_cube.stl
    /*
     * Import the file example_cube.stl.
     */
    module example_cube(anchor = [0, 0, 0]) {
        center = [2.0, 3.0, 2.0];
        displacement = [anchor.x * 5.0,
                        anchor.y * 10.0,
                        anchor.z * 15.0];

        translate(-center - displacement)
        import("test/data/example_cube.stl");
    }
"""


# -----------------------------------------------------------------------------
# Argument Parser
# -----------------------------------------------------------------------------
def add_subcommand(subparsers: Any) -> None:
    """Add the subcommand 'import'."""
    parser = subparsers.add_parser(
        "import",
        help="Generate an OpenSCAD import statement with anchoring support.",
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("stl", help="STL file.")
    parser.set_defaults(func=stl2scad_import)


# -----------------------------------------------------------------------------
# Command
# -----------------------------------------------------------------------------
def stl2scad_import(args) -> int:
    """Generate an OpenSCAD import statement with anchoring support."""
    logger = logging.getLogger(__name__)
    logger.debug("Executing command stl2scad import")

    logger.debug("Loading file %s", args.stl)
    try:
        mesh = stl.mesh.Mesh.from_file(args.stl)
    except FileNotFoundError:
        logger.critical("File %s not found.", args.stl)
        return 1

    bbox = get_stl_bounding_box(mesh)
    half_dims = [float(bbox[3] - bbox[0]) / 2, float(bbox[4] - bbox[1]) / 2, float(bbox[5] - bbox[2]) / 2]
    center = [
        float((bbox[3] + bbox[0]) / 2),
        float((bbox[4] + bbox[1]) / 2),
        float((bbox[5] + bbox[2]) / 2),
    ]

    print(f"""
/*
 * Import the file {Path(args.stl).name}.
 */
module {Path(args.stl).stem}(anchor = [0, 0, 0]) {{
    center = {center};
    displacement = [anchor.x * {half_dims[0]},
                    anchor.y * {half_dims[1]},
                    anchor.z * {half_dims[2]}];

    translate(-center - displacement)
    import("{args.stl}");
}}
""")
    return 0

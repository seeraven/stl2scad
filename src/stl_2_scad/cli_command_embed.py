"""
Module containing the subcommand 'embed' of stl2scad.

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
stl2scad embed
==============

Generate an OpenSCAD module that embeds the given STL object.
"""


# -----------------------------------------------------------------------------
# Argument Parser
# -----------------------------------------------------------------------------
def add_subcommand(subparsers: Any) -> None:
    """Add the subcommand 'embed'."""
    parser = subparsers.add_parser(
        "embed",
        help="Generate an OpenSCAD module that embeds the given STL object.",
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("stl", help="STL file.")
    parser.set_defaults(func=stl2scad_embed)


# -----------------------------------------------------------------------------
# Command
# -----------------------------------------------------------------------------
def stl2scad_embed(args) -> int:
    """Generate an OpenSCAD module that embeds the given STL object."""
    logger = logging.getLogger(__name__)
    logger.debug("Executing command stl2scad embed")

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

    vertices = []
    faces = []
    # pylint: disable=consider-using-enumerate
    for i in range(len(mesh.v0)):
        vertices.append([float(mesh.v0[i][0]), float(mesh.v0[i][1]), float(mesh.v0[i][2])])
        vertices.append([float(mesh.v1[i][0]), float(mesh.v1[i][1]), float(mesh.v1[i][2])])
        vertices.append([float(mesh.v2[i][0]), float(mesh.v2[i][1]), float(mesh.v2[i][2])])
        faces.append([i * 3 + 2, i * 3 + 1, i * 3])

    print(f"""
/*
 * Embedded STL file {Path(args.stl).name}.
 */
module polyhedron_{Path(args.stl).stem}(convexity = 1) {{
    vertices = {vertices};
    faces = {faces};
    polyhedron(points = vertices, faces = faces, convexity = convexity);
}}
""")

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
    polyhedron_{Path(args.stl).stem}();
}}
""")
    return 0

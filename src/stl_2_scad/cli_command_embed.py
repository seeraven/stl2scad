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

from stl_2_scad.settings import STL2SCAD_VERSION
from stl_2_scad.stl_helpers import get_stl_bounding_box

# -----------------------------------------------------------------------------
# Module Variables
# -----------------------------------------------------------------------------
DESCRIPTION = """
stl2scad embed
==============

Generate an OpenSCAD module that embeds the given STL object as a polyhedron.
This command creates two modules: A module to generate the STL object called
`polyhedron_<object>` and a module to place the STL object with support to
specify an anchor called `<object>`.

The name of the object is the STL filename without the suffix, but it can be
overwritten using the `--name` option.

The OpenSCAD code is printed on stdout per default, unless the `--output`
option is used to write it into a file instead.

Example:
    $ stl2scad embed --name MyCube --output mycube.scad test/data/example_cube.stl
    Generates the file mycube.scad that contains the OpenSCAD modules
    `polyhedron_MyCube()` and `MyCube()`.
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
    parser.add_argument(
        "-r",
        "--reverse-faces",
        help="If given, specify the face indices in reverse order.",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-n",
        "--name",
        help="Name of the object used in the OpenSCAD code. Default is the STL filename without the suffix.",
        default=None,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Write the generated OpenSCAD code into the specified file instead of printing it on stdout.",
        default=None,
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

    object_name = args.name if args.name is not None else Path(args.stl).stem

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
        if args.reverse_faces:
            faces.append([i * 3, i * 3 + 1, i * 3 + 2])
        else:
            faces.append([i * 3 + 2, i * 3 + 1, i * 3])

    header = f"""/*
 * Generated code by stl2scad v{STL2SCAD_VERSION} (https://github.com/seeraven/stl2scad)
 */
"""

    module_polyhedron = f"""
/*
 * Embedded STL object {object_name} from file {Path(args.stl).name}.
 */
module polyhedron_{object_name}(convexity = 1) {{
    vertices = {vertices};
    faces = {faces};
    polyhedron(points = vertices, faces = faces, convexity = convexity);
}}
"""

    module_object = f"""
/*
 * Place the embedded STL object {object_name} into the scene taking the
 * given anchor into account.
 */
module {object_name}(anchor = [0, 0, 0]) {{
    center = {center};
    displacement = [anchor.x * {half_dims[0]},
                    anchor.y * {half_dims[1]},
                    anchor.z * {half_dims[2]}];

    translate(-center - displacement)
    polyhedron_{object_name}();
}}
"""

    if args.output is None:
        print(header)
        print(module_polyhedron)
        print(module_object)
    else:
        logger.info("Writing output to file %s.", args.output)
        with open(args.output, "w", encoding="utf-8") as file_handle:
            file_handle.write(header)
            file_handle.write(module_polyhedron)
            file_handle.write(module_object)

    return 0

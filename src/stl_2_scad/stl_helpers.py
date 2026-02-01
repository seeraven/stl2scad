"""
Module containing the helpers for STL files of stl2scad.

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
import stl


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
def get_stl_bounding_box(mesh: stl.mesh.Mesh):
    """Get the bounding box of the STL mesh."""
    min_point = [min(mesh.points, key=lambda p: p[idx])[idx] for idx in range(3)]
    max_point = [max(mesh.points, key=lambda p: p[idx])[idx] for idx in range(3)]
    return min_point + max_point

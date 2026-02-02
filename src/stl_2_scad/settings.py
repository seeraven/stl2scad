"""
Module containing the common settings of stl2scad.

Copyright:
    2026 by Clemens Rabe <clemens.rabe@clemensrabe.de>

    All rights reserved.

    This file is part of stl2scad (https://github.com/seeraven/stl2scad)
    and is released under the "BSD 3-Clause License". Please see the ``LICENSE`` file
    that is included as part of this package.
"""

# -----------------------------------------------------------------------------
# Module Imports
# -----------------------------------------------------------------------------
import os

# -----------------------------------------------------------------------------
# Settings
# -----------------------------------------------------------------------------
STL2SCAD_VERSION = "1.0.0"
STL2SCAD_LOGFORMAT = os.getenv("STL2SCAD_LOGFORMAT", "%(asctime)s %(message)s")

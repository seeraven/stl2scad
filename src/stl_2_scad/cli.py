"""
Module containing the main entry point of stl2scad.

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
import os
import sys

import coloredlogs

# -----------------------------------------------------------------------------
# Module Variables
# -----------------------------------------------------------------------------
DESCRIPTION = """
stl2scad
========

Tool for using STL files with OpenSCAD.
"""
STL2SCAD_VERSION = "1.0.0"
STL2SCAD_LOGFORMAT = os.getenv("STL2SCAD_LOGFORMAT", "%(asctime)s %(message)s")


# -----------------------------------------------------------------------------
# Argument Parser
# -----------------------------------------------------------------------------
def get_parser() -> argparse.ArgumentParser:
    """Get the argument parser."""
    parser = argparse.ArgumentParser(description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--version", help="Print the version of stl2scad.", action="store_true", default=False)
    default_loglevel = os.getenv("STL2SCAD_LOGLEVEL", "INFO")
    parser.add_argument(
        "--loglevel",
        "-l",
        help=f"Configure the log level. Default: {default_loglevel}",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default=default_loglevel,
    )
    return parser


# -----------------------------------------------------------------------------
# Main Function
# -----------------------------------------------------------------------------
def main_cli() -> int:
    """The main entry point of the stl2scad command."""
    parser = get_parser()
    args = parser.parse_args()

    if args.version:
        print(f"stl2scad v{STL2SCAD_VERSION}")
        return 0

    # Setup logging
    log_level_styles = {
        "debug": {"color": "cyan"},
        "info": {"color": "green"},
        "warning": {"color": "yellow"},
        "error": {"color": "red"},
        "critical": {"bold": True, "color": "red"},
    }
    coloredlogs.install(level=args.loglevel, level_styles=log_level_styles, fmt=STL2SCAD_LOGFORMAT)

    logger = logging.getLogger(__name__)
    logger.debug("Python executable: %s", sys.executable)
    logger.debug("Called as %s", sys.argv)

    logger.info("Info log")
    logger.warning("Warning log")
    logger.error("Error log")
    logger.critical("Critical log")

    return 0

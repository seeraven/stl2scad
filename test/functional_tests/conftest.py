"""Configuration of pytest for functional tests."""

# pylint: disable=redefined-outer-name

# ----------------------------------------------------------------------------
#  MODULE IMPORTS
# ----------------------------------------------------------------------------
import os
import shutil
from pathlib import Path
from typing import List

import helpers.stl2scad_ifc
import pytest


# ----------------------------------------------------------------------------
#  PYTEST ADDITIONAL OPTIONS
# ----------------------------------------------------------------------------
def pytest_addoption(parser):
    """Add options to the pytest argument parser."""
    parser.addoption(
        "--executable",
        action="store",
        type=str,
        help="The stl2scad executable. Default: %(default)s",
        default="src/stl2scad",
    )


# ----------------------------------------------------------------------------
#  PYTEST ADDITIONAL FIXTURES
# ----------------------------------------------------------------------------
@pytest.fixture(scope="session")
def executable(pytestconfig) -> List[str]:
    """Fill the executable argument as a list of strings from the pytest option."""
    abs_args = []
    for arg in pytestconfig.getoption("executable").split(" "):
        if os.path.exists(arg):
            abs_args.append(os.path.abspath(arg))
        else:
            abs_args.append(shutil.which(arg))
    return abs_args


@pytest.fixture
def stl2scad_ifc(executable: List[str]) -> helpers.stl2scad_ifc.Stl2scadIfc:
    """Return the high-level interface to stl2scad."""
    return helpers.stl2scad_ifc.Stl2scadIfc(executable)


@pytest.fixture
def test_data_dir() -> Path:
    """Return the path to the test data directory."""
    return Path(__file__).parent.parent / "data"

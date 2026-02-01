"""Test the usage output of the application."""

# ----------------------------------------------------------------------------
#  MODULE IMPORTS
# ----------------------------------------------------------------------------
from helpers.stl2scad_ifc import Stl2scadIfc


# ----------------------------------------------------------------------------
#  TESTS
# ----------------------------------------------------------------------------
def test_usage(stl2scad_ifc: Stl2scadIfc):
    """Test the usage output when the '-h' or '--help' option is used."""
    result = stl2scad_ifc.run_ok(["--help"])
    result = stl2scad_ifc.run_ok(["-h"])

    assert "usage: stl2scad" in result.stdout
    assert "Tool for using STL files with OpenSCAD." in result.stdout
    assert "--version" in result.stdout
    assert "Print the version of stl2scad." in result.stdout

"""Test the output of the dims subcommand."""

# ----------------------------------------------------------------------------
#  MODULE IMPORTS
# ----------------------------------------------------------------------------
from pathlib import Path

from helpers.stl2scad_ifc import Stl2scadIfc


# ----------------------------------------------------------------------------
#  TESTS
# ----------------------------------------------------------------------------
def test_dims(stl2scad_ifc: Stl2scadIfc, test_data_dir: Path):
    """Test the output of the dims subcommand."""
    result = stl2scad_ifc.run_ok(["dims", str(test_data_dir / "example_cube.stl")])

    assert "X: -3.0 - 7.0" in result.stdout
    assert "Y: -7.0 - 13.0" in result.stdout
    assert "Z: -13.0 - 17.0" in result.stdout

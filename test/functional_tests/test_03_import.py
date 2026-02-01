"""Test the output of the import subcommand."""

# ----------------------------------------------------------------------------
#  MODULE IMPORTS
# ----------------------------------------------------------------------------
from pathlib import Path

from helpers.stl2scad_ifc import Stl2scadIfc


# ----------------------------------------------------------------------------
#  TESTS
# ----------------------------------------------------------------------------
def test_import(stl2scad_ifc: Stl2scadIfc, test_data_dir: Path):
    """Test the output of the import subcommand."""
    result = stl2scad_ifc.run_ok(["import", str(test_data_dir / "example_cube.stl")])

    expected_stdout = f"""module example_cube(anchor = [0, 0, 0]) {{
    center = [2.0, 3.0, 2.0];
    displacement = [anchor.x * 5.0,
                    anchor.y * 10.0,
                    anchor.z * 15.0];

    translate(-center - displacement)
    import("{str(test_data_dir)}/example_cube.stl");
}}
"""
    assert expected_stdout in result.stdout

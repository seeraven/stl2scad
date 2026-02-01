/*
 * This OpenSCAD file demonstrates the generated import statement.
 */

/* *************************************************************** *
 * INCLUDES
 * *************************************************************** */
include <BOSL2/std.scad>;


/* *************************************************************** *
 * CUSTOMIZER VALUES
 * *************************************************************** */

/* [General] */

ANCHOR_X = 0; // [0:CENTER, -1:LEFT, 1:RIGHT]
ANCHOR_Y = 0; // [0:CENTER, -1:FRONT, 1:BACK]
ANCHOR_Z = 0; // [0:CENTER, -1:BOTTOM, 1:TOP]

/* [Hidden] */


/* *************************************************************** *
 * GENERATED MODULE
 * *************************************************************** */

/*
 * Import the file example_cube.stl.
 */
module example_cube(anchor = [0, 0, 0]) {
    center = [2.0, 3.0, 2.0];
    displacement = [anchor.x * 5.0,
                    anchor.y * 10.0,
                    anchor.z * 15.0];

    translate(-center - displacement)
    import("example_cube.stl");
}


/* *************************************************************** *
 * USAGE
 * *************************************************************** */
example_cube(anchor = [ANCHOR_X, ANCHOR_Y, ANCHOR_Z]);

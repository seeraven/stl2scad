/*
 * OpenSCAD generator of the example data STL files.
 */

/* *************************************************************** *
 * CUSTOMIZER VALUES
 * *************************************************************** */

/* [General] */

SELECTED_COMPONENT = "cube"; // [cube, sphere]

/* [Quality] */

// Minimum angle for a fragment
$fa = 1.0; // .1

// Minimum size of a fragment
$fs = 2; // .01

// Number of fragments
$fn = 0;


/* [Hidden] */


/* *************************************************************** *
 * CUBE
 * *************************************************************** */
module example_cube() {
    translate([-3, -7, -13])
    cube([10, 20, 30]);
}


/* *************************************************************** *
 * SPHERE
 * *************************************************************** */
module example_sphere() {
    translate([3, -7, 13])
    sphere(r = 10);
}


/* *************************************************************** *
 * SHOW PARTS
 * *************************************************************** */
if (SELECTED_COMPONENT == "cube") {
    example_cube();
}

if (SELECTED_COMPONENT == "sphere") {
    example_sphere();
}

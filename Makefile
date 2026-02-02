# ----------------------------------------------------------------------------
# Makefile for stl2scad
#
# Copyright (c) 2026 by Clemens Rabe <clemens.rabe@clemensrabe.de>
# All rights reserved.
# This file is part of stl2scad (https://github.com/seeraven/stl2scad)
# and is released under the "BSD 3-Clause License". Please see the LICENSE file
# that is included as part of this package.
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
#  SETTINGS
# ----------------------------------------------------------------------------
APP_NAME             := stl2scad
APP_VERSION          := 1.0.1

ALL_TARGET           := check-style.venv
SCRIPT               := src/stl2scad

UBUNTU_DIST_VERSIONS := 22.04 24.04
MAKE4PY_DOCKER_IMAGE := make4py-stl2scad

PYINSTALLER_ARGS_LINUX   := --clean --onefile
PYINSTALLER_ARGS_DARWIN  := --clean --onedir
PYINSTALLER_ARGS_WINDOWS := --clean --onefile

VARS_TO_PROPAGATE        := UNITTESTS FUNCTESTS IN_GITHUB_ACTION

PIP_PACKAGE              := pip<26.0


# ----------------------------------------------------------------------------
#  MAKE4PY INTEGRATION
# ----------------------------------------------------------------------------
include .make4py/make4py.mk

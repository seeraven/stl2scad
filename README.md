# STL to OpenSCAD Tool

This repository hosts a simple tool to work with STL files in OpenSCAD. It
allows you to
  - get the dimensions of an STL object
  - create an OpenSCAD import statement with anchor support

## Installation on Linux

stl2scad is distributed as a single executable packaged using [pyInstaller].
So all you have to do is to download the latest executable and copy it to a
location of your choice, for example `~/bin`:

    wget https://github.com/seeraven/stl2scad/releases/download/v1.0.0/stl2scad_v1.0.0_Ubuntu22.04_x86_64
    mv stl2scad_v1.0.0_Ubuntu22.04_x86_64 ~/bin/stl2scad
    chmod +x ~/bin/stl2scad

## Installation on Windows

Download the latest executable for Windows from the release page
https://github.com/seeraven/stl2scad/releases. Rename the executable to
`stl2scad.exe` and put it into a directory in your PATH, e.g., into
`C:\Windows`.

## stl2scad Command Usage

The `stl2scad` command provides the following options:

  - `-h`, `--help` to show the command help.
  - `-v`, `--version` to show the version of `stl2scad`.

The following subcommands are provided:

  - `dims <stlfile>` to print the bounding box of the STL object
  - `import <stlfile>` to generate the OpenSCAD code to import the
    STL object and position it using the provided `anchor` argument.

## Development

To start development on this project, you have to clone this repository first including
all submodules:

    git clone https://github.com/seeraven/stl2scad.git
    cd stl2scad
    git submodule update --init

Using the [make4py] framework, we access all major steps using the good old `make`
command. The main make targets of interest are:

  - `make format` to format the source code
  - `make check-style` to perform a static code analysis
  - `make tests` to perform unit and functional tests

The actions are executed in a virtual environment per default. You can also use
dedicated suffixes on the targets to specify the environment to use:

  - `<target>.venv` specifies explicitly to use a virtual env.
  - `<target>.ubuntu24.04` specifies to use a Ubuntu 24.04 docker container
  - `<target>.alpine3.20` specifies to use a Alpine 3.20 docker container
  - `<target>.windows` specifies to use a vagrant machine running Windows
  - `<target>.all` specifies to run the target on all variants.

For example, if you want to execute the unit tests on Ubuntu 22.04, you can call

    make unittests.ubuntu22.04

## Notes on Releases

Releases are now automatically built if a new tag `v<major>.<minor>.<revision>`
is pushed to the repository. This changes the release process a little bit:

  - Ensure the upcoming release is fully tested. A look on the commits on github
    should be enough.
  - Modify the `CHANGELOG.md` file and insert the new version number.
  - Commit the modified `CHANGELOG.md` file and tag the commit with the new
    version number.
  - As soon as the new tag is pushed to github, the release is built. When it
    is finished, it is found as a draft on the releases page.
  - Now edit the release draft, insert the changes from the `CHANGELOG.md` file.
    Then the release can be saved as a regular release.
  - Now prepare the next version. Edit the files `Makefile`, `pyproject.toml`,
    `src/git_cache/git_cache_command.py` and `doc/source/installation.rst` and
    replace the version number:

        sed -i 's/1.0.30/1.0.31/g' Makefile pyproject.toml src/git_cache/git_cache_command.py doc/source/installation.rst

[pyInstaller]: https://www.pyinstaller.org/
[make4py]: https://github.com/seeraven/make4py

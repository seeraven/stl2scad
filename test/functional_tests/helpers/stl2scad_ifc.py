"""
Module for providing a test interface to stl2scad.

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
import subprocess
from typing import List


# -----------------------------------------------------------------------------
# Interface Class
# -----------------------------------------------------------------------------
class Stl2scadIfc:
    """Interface to run stl2scad and check its state."""

    def __init__(self, executable: List[str]) -> None:
        """Create the interface to stl2scad."""
        self._executable = executable

    def run(self, args: List[str], cwd=None) -> subprocess.CompletedProcess:
        """Run stl2scad and return the result."""
        return subprocess.run(
            self._executable + args,
            shell=False,
            text=True,
            check=False,
            cwd=cwd,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )

    def run_ok(self, args: List[str], cwd=None) -> subprocess.CompletedProcess:
        """Run stl2scad and return the result. Also assert a return code of 0."""
        result = self.run(args, cwd)
        if result.returncode != 0:
            print(f"Command {self._executable + args} failed:")
        print(f"  Stdout: {result.stdout}")
        print(f"  Stderr: {result.stderr}")
        assert 0 == result.returncode
        return result

    def run_fail(self, args: List[str], cwd=None) -> subprocess.CompletedProcess:
        """Run stl2scad and return the result. Also assert a return code of non-zero."""
        result = self.run(args, cwd)
        assert 0 != result.returncode
        return result

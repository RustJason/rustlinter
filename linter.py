#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jason Young,,,
# Copyright (c) 2015 Jason Young,,,
#
# License: MIT
#

"""This module exports the Rustlinter plugin class."""

from SublimeLinter.lint import Linter, util


class Rustlinter(Linter):
    """Provides an interface to rustlinter."""

    syntax = 'rust'
    cmd = ('rustc', '*', '-')
    executable = 'rustc'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.5.0'
    regex = (
        r'.*?:(?P<line>\d+):(?P<col>\d+): '
        r'.*?warning: (?P<warning>.*$)'
        r'.*?error: (?P<error>.*$)'
    )
    multiline = True
    inline_overrides = ('standard')


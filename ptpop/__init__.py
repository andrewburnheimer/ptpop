#!/usr/bin/env python
# -*- coding: ascii -*-

# The __init__.py is loaded (only) when importing the package

"""
Package Ptpop
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""
import os

__author__ = 'Andrew Burnheimer (Andrew.Burnheimer@nbcuni.com)'
__copyright__ = 'Copyright (c) 2016 Andrew Burnheimer'
__license__ = 'Creative Commons Attribution and ShareAlike'
__version__ = ""

with open(os.path.join('./', 'VERSION')) as version_file:
    __version__ = version_file.read().strip()

from Console import Console
from Listener import Listener
from PtpNeighbor import PtpNeighbor
from AnnounceMessage import AnnounceMessage

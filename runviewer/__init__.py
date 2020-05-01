#####################################################################
#                                                                   #
# /__init__.py                                                      #
#                                                                   #
# Copyright 2013, Monash University                                 #
#                                                                   #
# This file is part of the program runviewer, in the labscript     #
# suite (see http://labscriptsuite.org), and is licensed under the  #
# Simplified BSD License. See the license.txt file in the root of   #
# the project for the full license.                                 #
#                                                                   #
#####################################################################
import os

from labscript_utils.versions import get_version, NoVersionInfo
from pathlib import Path
__version__ = get_version(__name__, import_path=Path(__file__).parent.parent)
if __version__ is NoVersionInfo:
    __version__ = None
    
runviewer_dir = os.path.dirname(os.path.realpath(__file__))

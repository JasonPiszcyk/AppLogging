#!/usr/bin/env python3
'''
PyTest - Test of usage recipies

Copyright (C) 2025 Jason Piszcyk
Email: Jason.Piszcyk@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program (See file: COPYING). If not, see
<https://www.gnu.org/licenses/>.
'''
###########################################################################
#
# Imports
#
###########################################################################
# Shared variables, constants, etc
from tests.constants import *

# System Modules

# Local app modules
from applogging.logging import (
    get_logger,
    init_console_logger,
    init_file_logger
)

# Imports for python variable type hints
from pytest import CaptureFixture

###########################################################################
#
# Module Specific Items
#
###########################################################################
#
# Types
#

#
# Constants
#

#
# Global Variables
#


###########################################################################
#
# The tests...
#
###########################################################################
#
# Log to Console
#
class Test_LogToConsole():
    '''
    Test Class - Log to Console

    Attributes:
        None
    '''
    #
    #
    #
    def test_log_error(self, capsys: CaptureFixture):
        '''
        Test logging an error (default threshold is INFO)

        Args:
            capfd (str, str): Fixture to capture stdout/stderr 

        Returns:
            None

        Raises:
            AssertionError:
                when test fails
        '''
        _log = init_console_logger(name=LOGGER_NAME)

        _log.error(DEFAULT_LOG_STRING)
        _cap = capsys.readouterr()

        assert _cap.err == DEFAULT_LOG_STRING

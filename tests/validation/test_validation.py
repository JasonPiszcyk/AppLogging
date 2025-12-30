#!/usr/bin/env python3
'''
PyTest - Test of validation functions

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
from applogging.logging import is_valid_log_level_string

# Imports for python variable type hints


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
# Validate Log Level
#
class Test_ValidateLogLevel():
    '''
    Test Class - Validate Log Level

    Attributes:
        None
    '''
    #
    # Valid methods
    #
    def test_valid_log_level(self):
        '''
        Test that valid log levels are validated correctly

        Args:
            None

        Returns:
            None

        Raises:
            AssertionError:
                when test fails
        '''
        for _log_level in VALID_LOG_LEVELS:
            assert is_valid_log_level_string(_log_level)


    #
    # Invalid methods
    #
    def test_invalid_log_level(self):
        '''
        Test invalid log levels are NOT validated

        Args:
            None

        Returns:
            None

        Raises:
            AssertionError:
                when test fails
        '''
        # Test invalid log levels
        assert not is_valid_log_level_string()
        assert not is_valid_log_level_string("")
        assert not is_valid_log_level_string(None) # type: ignore
        assert not is_valid_log_level_string(level="")
        assert not is_valid_log_level_string(0) # type: ignore
        assert not is_valid_log_level_string("no level")
        assert not is_valid_log_level_string(self) # type: ignore

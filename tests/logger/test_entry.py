#!/usr/bin/env python3
'''
PyTest - Test of log entry processing

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
import pytest

# Local app modules
from applogging.entry import LogEntry

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
LOG_ENTRY_DICT = {
    "DEFAULT": {
        "format": "%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
        "message": (
            f"2025-01-01 10:00:00,000: [{LOGGER_NAME}] "
            f"[{DEFAULT_LOG_SEVERITY}] {DEFAULT_LOG_STRING}"
        ),
        "token_map": {}
    },
    "TOKEN_CURLY_BRACES": {
        "format": "%(asctime)s: {%(name)s} {%(levelname)s} %(message)s",
        "message": (
            f"2025-01-01 10:00:00,000: {{{LOGGER_NAME}}} "
            f"{{{DEFAULT_LOG_SEVERITY}}} {DEFAULT_LOG_STRING}"
        ),
        "token_map": {
            "name": { "delimiters": [ "{", "}" ] },
            "levelname": { "delimiters": [ "{", "}" ] }
        }
    },
    "TOKEN_PARENTHESES": {
        "format": "%(asctime)s: (%(name)s) (%(levelname)s) %(message)s",
        "message": (
            f"2025-01-01 10:00:00,000: ({LOGGER_NAME}) "
            f"({DEFAULT_LOG_SEVERITY}) {DEFAULT_LOG_STRING}"
        ),
        "token_map": {
            "name": { "delimiters": [ "(", ")" ] },
            "levelname": { "delimiters": [ "(", ")" ] }
        }
    }
}

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
class Test_LogEntry():
    '''
    Test Class - Test breakdown of log entries

    Attributes:
        None
    '''
    #
    #
    #
    @pytest.mark.parametrize("log_entry_dict_key", LOG_ENTRY_DICT)
    def test_log_entry(self, log_entry_dict_key):
        '''
        Test Log Entry is decoding correctly

        Args:
            None

        Returns:
            None

        Raises:
            AssertionError:
                when test fails
        '''
        assert log_entry_dict_key in LOG_ENTRY_DICT
        _log_info = LOG_ENTRY_DICT[log_entry_dict_key]

        assert "format" in _log_info
        assert "message" in _log_info
        assert "token_map" in _log_info

        _log_entry = LogEntry(
            msg=_log_info["message"],
            format=_log_info["format"],
            token_map=_log_info["token_map"]
        )

        assert _log_entry.message == DEFAULT_LOG_STRING
        assert _log_entry.severity == DEFAULT_LOG_SEVERITY
        assert _log_entry.logger_name == LOGGER_NAME

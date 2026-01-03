#!/usr/bin/env python3
'''
PyTest - Test of usage recipes

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
from applogging.constants import VALID_LOG_LEVELS

# System Modules
import pytest

# Local app modules
from applogging.logging import init_console_logger, init_file_logger
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
    @pytest.mark.parametrize("log_level", VALID_LOG_LEVELS)
    def test_log_error(self, log_level, capsys: pytest.CaptureFixture):
        '''
        Test logging a message to all valid log levels

        Args:
            capsys (CaptureFixture): Fixture to capture stdout/stderr 

        Returns:
            None

        Raises:
            AssertionError:
                when test fails
        '''
        _severity = str(log_level).lower()
        if log_level in MAP_LOG_LEVELS.keys():
            _output_severity = MAP_LOG_LEVELS[log_level]
        else:
            _output_severity = log_level

        # Don't try to log to NOTSET
        if _output_severity == "NOTSET": return

        _log = init_console_logger(name=LOGGER_NAME)
        _log.setLevel(level="DEBUG")

        # See if we can log at requested severity
        _func = getattr(_log, _severity, None)
        if callable(_func): _func(DEFAULT_LOG_STRING)

        _cap = capsys.readouterr()

        _log_entry = LogEntry(msg=f"{_cap.out}{_cap.err}")

        assert _log_entry.message == DEFAULT_LOG_STRING
        assert _log_entry.severity == _output_severity
        assert _log_entry.logger_name == LOGGER_NAME


#
# Log to File
#
class Test_LogToFile():
    '''
    Test Class - Log to File

    Attributes:
        None
    '''
    #
    #
    #
    @pytest.mark.parametrize("log_level", VALID_LOG_LEVELS)
    def test_log(self, log_level, logfile):
        '''
        Test logging at various levels

        Args:
            logfile: str

        Returns:
            None

        Raises:
            AssertionError:
                when test fails
        '''
        _log_file = logfile

        _severity = str(log_level).lower()
        if log_level in MAP_LOG_LEVELS.keys():
            _output_severity = MAP_LOG_LEVELS[log_level]
        else:
            _output_severity = log_level

        # Don't try to log to NOTSET
        if _output_severity == "NOTSET": return

        _log = init_file_logger(name=LOGGER_NAME, filename=_log_file)
        _log.setLevel(level="DEBUG")

        # See if we can log at requested severity
        _func = getattr(_log, _severity, None)
        if callable(_func): _func(DEFAULT_LOG_STRING)

        # Read the log file
        with open(_log_file, "r") as f:
            _file_contents = f.read()

        _log_entry = LogEntry(msg=_file_contents)

        assert _log_entry.message == DEFAULT_LOG_STRING
        assert _log_entry.severity == _output_severity
        assert _log_entry.logger_name == LOGGER_NAME
 
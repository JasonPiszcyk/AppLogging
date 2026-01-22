#!/usr/bin/env python3
'''
Logging Functions

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
from __future__ import annotations

# Shared variables, constants, etc

# System Modules
import sys
import logging
import logging.handlers
import datetime

# Local app modules
from applogging.constants import (
    VALID_LOG_LEVELS,
    DEFAULT_LOG_LEVEL,
    DEFAULT_LOG_FORMAT
)

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
DEFAULT_CONSOLE_HANDLER_NAME = "TO_CONSOLE"

# Defaults for timed rotating file
DEFAULT_TIMED_ROTATING_FILE_WHEN = "W6"
DEFAULT_TIMED_ROTATING_FILE_AT_TIME = datetime.time(0, 0, 0)
DEFAULT_TIMED_ROTATING_FILE_COPIES = 5


###########################################################################
#
# Validation
#
###########################################################################
#
# is_valid_log_level_string
#
def is_valid_log_level_string(level: str = "") -> bool:
    '''
    Validate the supplied log level string is valid

    Args:
        level (str): A string representing a log level

    Returns:
        bool: True if level is valid, false otherwise

    Raises:
        None
    '''
    # Make sure the log level is a string
    if not isinstance(level, str): return False

    # Get the valid Level Names (getLevelNamesMapping added in 3.11)
    if sys.version_info < (3, 11):
        _valid_levels = VALID_LOG_LEVELS
    else:
        _valid_levels = logging.getLevelNamesMapping().keys()

    # Check if the level is valid
    return level.upper() in _valid_levels


###########################################################################
#
# Manipulate Loggers
#
###########################################################################
#
# get_logger
#
def get_logger(name: str | None = None) -> logging.Logger:
    '''
    Simple wrapper for logging.get_logger

    Args:
        name (str | None): The name of the logger to get, or the root logger if
            name is None

    Returns:
        logging.Logger: A logger

    Raises:
        AssertionError:
            when name is not a string or None
    '''
    assert (
        name is None or
        (isinstance(name, str) and name)
    ), (
        "'name' must be None or a non-empty string"
    )

    return logging.getLogger(name=name)


#
# clear_handlers
#
def clear_handlers(logger: logging.Logger | None = None):
    '''
    Clear any handlers associated with the logger

    Args:
        logging.Logger: A logger

    Returns:
        None

    Raises:
        AssertionError:
            when no logger provided
    '''
    assert logger, f"Logging instance not supplied."
    assert isinstance(logger, logging.Logger), (
        f"logger is not a logging.Logger instance."
    )

    # Remove existing handlers
    for _handler in logger.handlers.copy():
        logger.removeHandler(_handler)


#
# init_console_logger
#
def init_console_logger(name: str | None = None) -> logging.Logger:
    '''
    Create a standard logger to the console

    Args:
        name (str | None): The name of the logger to init, or the root logger
            if name is None

    Returns:
        logging.Logger: A logger

    Raises:
        AssertionError:
            when name is not a string or None
    '''
    assert (
        name is None or
        (isinstance(name, str) and name)
    ), (
        "'name' must be None or a non-empty string"
    )

    # Create the logger
    _logger = get_logger(name=name)

    # Clear any existing handlers
    clear_handlers(_logger)

    # Add the handl,er
    _logger.addHandler(handler_to_console())

    return _logger


#
# init_file_logger
#
def init_file_logger(
        name: str | None = None,
        filename: str = ""
) -> logging.Logger:
    '''
    Create a standard logger to a rotating file

    Args:
        name (str | None): The name of the logger to init, or the root logger
            if name is None
        filename (str): The name of the file to log to

    Returns:
        logging.Logger: A logger

    Raises:
        AssertionError:
            when name is not a string or None
    '''
    assert (
        name is None or
        (isinstance(name, str) and name)
    ), (
        "'name' must be None or a non-empty string"
    )

    # Create the logger
    _logger = get_logger(name=name)

    # Clear any existing handlers
    clear_handlers(_logger)

    # Add the handl,er
    _logger.addHandler(handler_to_timed_rotating_file(filename=filename))

    return _logger


###########################################################################
#
# Query Logging Config
#
###########################################################################
#
# get_log_level
#
def get_log_level(logger: logging.Logger | None = None) -> str:
    '''
    Get the log level for the logger

    Args:
        logger (Logger): The logger to query

    Returns:
        str: The name of the logging level

    Raises:
        AssertionError:
            when no logger provided
    '''
    assert logger, f"Logging instance not supplied."
    assert isinstance(logger, logging.Logger), (
        f"logger is not a logging.Logger instance."
    )

    _log_level_int = logger.level
    if not isinstance(_log_level_int, int): _log_level_int = 0

    return logging.getLevelName(level=_log_level_int)


###########################################################################
#
# Set Logging Config
#
###########################################################################
#
# set_log_level
#
def set_log_level(
        logger: logging.Logger | None = None,
        level: str = DEFAULT_LOG_LEVEL
):
    '''
    Set the log level for the logger

    Args:
        logger (Logger): The logger to update
        level (str): The log level to set

    Returns:
        None

    Raises:
        AssertionError:
            when no logger provided
        ValueError:
            when level is not valid
    '''
    assert logger, f"Logging instance not supplied."
    assert isinstance(logger, logging.Logger), (
        f"Logging instance not supplied."
    )

    if not is_valid_log_level_string(level=level):
        raise ValueError(f"'{level}' is not a valid logging level")

    logger.setLevel(level=level.upper())


###########################################################################
#
# 'Standard' handlers
#
###########################################################################
#
# _set_handler_config
#
def _set_handler_config(
        format:str = DEFAULT_LOG_FORMAT,
        name: str = "",
        handler: logging.Handler | None = None
):
    '''
    Perform basic config on the handler

    Args:
        format (str): The format to use for the log output
        name (str): The name to use for the handler
        handler (logging.Handler): The handler to use

    Returns:
        None

    Raises:
        AssertionError:
            when format is not a non-empty string
            when filename is not a non-empty string
            when handler is not a handler instance
    '''
    assert format, f"Empty format supplied."
    assert isinstance(format, str), f"Format must be a string."

    assert name, f"Empty name supplied."
    assert isinstance(name, str), f"Name must be a string."

    assert isinstance(handler, logging.Handler), (
        f"A handler instrance must be provided."
    )

    _log_format = logging.Formatter(fmt=format)

    # Set the log format and add the handler
    handler.setFormatter(_log_format)
    handler.name = name


#
# handler_to_console
#
def handler_to_console(
        format:str = DEFAULT_LOG_FORMAT,
        name: str = DEFAULT_CONSOLE_HANDLER_NAME
) -> logging.Handler:
    '''
    Create a handler to output to console

    Args:
        format (str): The format to use for the log output (default used if
            not provided)
        name (str): The name to use for the handler (default used if
            not provided)

    Returns:
        Handler: The handler for output stream

    Raises:
        AssertionError:
            when format is not a non-empty string
            when name is not a non-empty string
    '''
    # Setup the handler to stdout
    _handler = logging.StreamHandler()

    _set_handler_config(
        format=format,
        name=name,
        handler=_handler
    )

    # Return the handler
    return _handler


#
# handler_to_file
#
def handler_to_file(
        filename: str = "",
        format:str = DEFAULT_LOG_FORMAT
) -> logging.Handler:
    '''
    Create a handler to output to a file

    Args:
        filename (str): The name of the file to log to
        format (str): The format to use for the log output

    Returns:
        Handler: The handler for output stream

    Raises:
        AssertionError:
            when format is not a non-empty string
            when filename is not a non-empty string
    '''
    assert filename, f"Empty filename supplied."
    assert isinstance(filename, str), f"Filename must be a string."

    _log_format = logging.Formatter(fmt=format)

    # Set up the handler to rotate log files
    _handler = logging.FileHandler(filename)

    _set_handler_config(
        format=format,
        name=filename,
        handler=_handler
    )

    # Return the handler
    return _handler


#
# handler_to_timed_rotating_file
#
def handler_to_timed_rotating_file(
        filename: str = "",
        format:str = DEFAULT_LOG_FORMAT,
        when:str = DEFAULT_TIMED_ROTATING_FILE_WHEN,
        at_time: datetime.time = DEFAULT_TIMED_ROTATING_FILE_AT_TIME,
        copies: int = DEFAULT_TIMED_ROTATING_FILE_COPIES
) -> logging.Handler:
    '''
    Create a handler to output to a file that is rotated on a timed basis

    Args:
        name (str): The name of the file to log to
        format (str): The format to use for the log output
        when (str): Weekday on wich to rotate the file
            one of: "W0", "W1", "W2", "W3", "W4", "W5", "W6"
        at_time (datetime.time): A time structure indicating the time to rotate
            the file
        copies (int): Number of backup copies to keep

    Returns:
        Handler: The handler for output stream

    Raises:
        AssertionError:
            when format is not a non-empty string
            when filename is not a non-empty string
            when 'when' is not valid
            when at_time is not a valid time instance
            when copies is not 0 or a positive integer
    '''
    assert filename, f"Empty filename supplied."
    assert isinstance(filename, str), f"Filename must be a string."

    _valid_when = [ "W0", "W1", "W2", "W3", "W4", "W5", "W6" ]
    assert when in _valid_when, f"'when' must be one of {_valid_when}"

    assert isinstance(at_time, datetime.time), (
        f"at_time is not a valid datetime.time instance"
    )

    assert isinstance(copies, int), "copies must be an integer"
    assert copies >= 0, "copies must be greater than or equal to 0"

    # Set up the handler to rotate log files
    _handler = logging.handlers.TimedRotatingFileHandler(
        filename,
        when=when,
        atTime=at_time,
        backupCount=copies
    )

    _set_handler_config(
        format=format,
        name=filename,
        handler=_handler
    )

    # Return the handler
    return _handler


###########################################################################
#
# In case this is run directly rather than imported...
#
###########################################################################
'''
Handle case of being run directly rather than imported
'''
if __name__ == "__main__":
    pass

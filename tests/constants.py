#!/usr/bin/env python3
'''
The Constants used for Testing

Copyright (C) 2025 Jason Piszcyk
Email: Jason.Piszcyk@gmail.com

All rights reserved.

This software is private and may NOT be copied, distributed, reverse engineered,
decompiled, or modified without the express written permission of the copyright
holder.

The copyright holder makes no warranties, express or implied, about its 
suitability for any particular purpose.
'''
###########################################################################
#
# Imports
#
###########################################################################
# Shared variables, constants, etc

# System Modules

# Local app modules

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
LOGGER_NAME = "AppLogging"
LOG_FILE_NAME = f"/tmp/{LOGGER_NAME}-test.log"

VALID_LOG_LEVELS = [
    "CRITICAL",
    "FATAL",
    "ERROR",
    "WARN",
    "WARNING",
    "INFO",
    "DEBUG",
    "NOTSET",
]

# Log levels may appears as something different in the log output
MAP_LOG_LEVELS = {
    "FATAL": "CRITICAL",
    "WARN": "WARNING"
}


DEFAULT_LOG_STRING = "The default log string"

VALID_LOG_ENTRY = (
    "2025-01-01 10:00:00,000: [AppLogging] [ERROR] The default log string"
)

#
# Global Variables
#

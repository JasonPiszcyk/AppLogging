#!/usr/bin/env python3
'''
Module Initialisation

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

# What to import when 'import * from module'
__all__ = [ 
    "get_logger",
    "clear_handlers",
    "init_console_logger",
    "init_file_logger",
    "get_log_level",
    "set_log_level",
    "handler_to_console",
    "handler_to_file",
    "handler_to_timed_rotating_file",
    "LogEntry"
]

# What to import as part of the the module (import module)
from applogging.logging import (
    get_logger,
    clear_handlers,
    init_console_logger,
    init_file_logger,
    get_log_level,
    set_log_level,
    handler_to_console,
    handler_to_file,
    handler_to_timed_rotating_file
)
from applogging.entry import LogEntry

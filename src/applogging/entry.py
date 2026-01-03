#!/usr/bin/env python3
'''
LogEntry - Class for processing a log string and decoding it

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
import re

# Local app modules
from applogging.constants import DEFAULT_LOG_FORMAT

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

# The default mapping of tokens to attributes along with token delimiters
#   Anything not mapped or delimited is aggregated into msg
#   Mapping to an empty string means the token is ignored
#   
DEFAULT_TOKEN_MAP = {
    "asctime": { "mapto": "time", "delimiters": [ "", ":" ] },
    "created": { "mapto": "", "delimiters": [ "[", "]" ] },
    "filename": { "mapto": "", "delimiters": [ "[", "]" ] },
    "funcName": { "mapto": "", "delimiters": [ "[", "]" ] },
    "levelname": { "mapto": "severity", "delimiters": [ "[", "]" ] },
    "levelno": { "mapto": "", "delimiters": [ "[", "]" ] },
    "lineno": { "mapto": "", "delimiters": [ "[", "]" ] },
    "module": { "mapto": "", "delimiters": [ "[", "]" ] },
    "msecs": { "mapto": "", "delimiters": [ "[", "]" ] },
    "name": { "mapto": "logger_name", "delimiters": [ "[", "]" ] },
    "pathname": { "mapto": "", "delimiters": [ "[", "]" ] },
    "process": { "mapto": "process_id", "delimiters": [ "[", "]" ] },
    "processName": { "mapto": "process_name", "delimiters": [ "[", "]" ] },
    "relativeCreated": { "mapto": "", "delimiters": [ "[", "]" ] },
    "thread": { "mapto": "thread_id", "delimiters": [ "[", "]" ] },
    "threadName": { "mapto": "thread_name", "delimiters": [ "[", "]" ] },
    "taskName": { "mapto": "", "delimiters": [ "[", "]" ] }
}

# The data types for tokens found in the format string (from Logging module)
TOKEN_TYPING = {
    "asctime": "s",
    "created": "f",
    "filename": "s",
    "funcName": "s",
    "levelname": "s",
    "levelno": "s",
    "lineno": "d",
    "module": "s",
    "msecs": "d",
    "name": "s",
    "pathname": "s",
    "process": "d",
    "processName": "s",
    "relativeCreated": "d",
    "thread": "d",
    "threadName": "s",
    "taskName": "s"
}

DELIMITERS_TO_ESCAPE = [ "[", "]", "(", ")" ]

#
# Global Variables
#


###########################################################################
#
# LogEntry Class Definition
#
###########################################################################
class LogEntry():
    '''
    Class for processing a log string and decoding it

    Attributes:
        time (str) [ReadOnly]: The time the entry was logged
        logger_name (str) [ReadOnly]: The name of the logger used
        severity (str) [ReadOnly]: The severity of the log message
        source (str) [ReadOnly]: The source of the log message
        process_id (int) [ReadOnly]: The process ID that logged the message
        process_name (str) [ReadOnly]: The process Name that logged the message
        thread_id (int) [ReadOnly]: The thread ID that logged the message
        thread_name (str) [ReadOnly]: The thread Name that logged the message
        message (str) [ReadOnly]: The message
    '''

    #
    # __init__
    #
    def __init__(
            self,
            msg: str = "",
            format: str = DEFAULT_LOG_FORMAT,
            token_map: dict = {}
    ):
        '''
        Initialises the instance.

        A number of tokens can be extracted.  The extraction and order of
        tokens is described by the format

        Args:
            msg: (str): The log message to be decoded
            format (str): The format used to create the log entry
            token_map (dict): Modifications to the default mapping dict used
                to extract the tokens

        Returns:
            None

        Raises:
            AssertionError:
                when mapping is not valid
        '''
        # Private Attributes
        self._time = ""
        self._logger_name = ""
        self._severity = ""
        self._source = ""
        self._process_id = 0
        self._process_name = ""
        self._thread_id = 0
        self._thread_name = ""
        self._message = ""

        # The token map
        self._token_map = {}

        # Manually merge in the default token map
        self._merge_token_map(token_map=DEFAULT_TOKEN_MAP)

        # Manually merge in any changes to the token map
        self._merge_token_map(token_map=token_map)

        # Attributes

        # Decode the entry
        self._decode_log_entry(msg=msg, format=format)


    ###########################################################################
    #
    # Properties
    #
    ###########################################################################
    #
    # time
    #
    @property
    def time(self) -> str:
        ''' The time string found in the log entry '''
        return self._time


    #
    # logger_name
    #
    @property
    def logger_name(self) -> str:
        ''' The name of the logger used '''
        return self._logger_name


    #
    # severity
    #
    @property
    def severity(self) -> str:
        ''' The severity of the log message '''
        return self._severity


    #
    # source
    #
    @property
    def source(self) -> str:
        ''' The source of the log message '''
        return self._source


    #
    # process_id
    #
    @property
    def process_id(self) -> int:
        ''' The process ID that logged the message '''
        return self._process_id


    #
    # process_name
    #
    @property
    def process_name(self) -> str:
        ''' The process name that logged the message '''
        return self._process_name


    #
    # thread_id
    #
    @property
    def thread_id(self) -> int:
        ''' The thread ID that logged the message '''
        return self._thread_id


    #
    # thread_name
    #
    @property
    def thread_name(self) -> str:
        ''' The thread name that logged the message '''
        return self._thread_name


    #
    # message
    #
    @property
    def message(self) -> str:
        ''' The  message '''
        return self._message


    ###########################################################################
    #
    # Methods
    #
    ###########################################################################
    #
    # _merge_token_map
    #
    def _merge_token_map(self, token_map: dict = {}):
        '''
        Merge in any changes to the token map
            
        Args:
            token_map (dict): Dict containing updates to the token map
        
        Returns:
            None

        Raises:
            AssertionError:
                when token_map is not a dict
        '''
        assert isinstance(token_map, dict), "map must be a dict"

        # Go through token_map and merge in any items
        for _key, _val in token_map.items():
            # Make sure the entry contains a sub-dict
            assert isinstance(_val, dict), (
                f"Invalid token mapping entry: {_key}"
            )

            # Create a new entry
            _entry = {}

            # Go through the list of attributes to process
            for _attr in [ "mapto", "delimiters" ]:
                if _attr in _val:
                    # The map contains the attribute - Just set it
                    _entry[_attr] = _val[_attr]

                else:
                    # See if there is a default for the attribute
                    _default_entry = DEFAULT_TOKEN_MAP.get(_key, {})

                    if _attr in _default_entry:
                        # There is an entry in the default map
                        _entry[_attr] = _default_entry[_attr]

                    else:
                        # Create an entry based on some sensible defaults
                        if _attr in [ "mapto", ]:
                            _entry[_attr] = ""
                        elif _attr in [ "delimiters", ]:
                            _entry[_attr] = [ "[", "]" ]

            # Ensure mapto is a string
            assert isinstance(_entry["mapto"], str), (
                f"mapto must be a string: {_key}"
            )

            # Make sure delimiters is a list
            assert isinstance(_entry["delimiters"], list), (
                f"delimiters must be a list: {_key}"
            )

            # Add the entry
            self._token_map[_key] = _entry


    #
    # _decode_log_entry
    #
    def _decode_log_entry(self, msg: str = "", format: str = ""):
        '''
        Decode the message into the tokens
            
        Args:
            msg: (str): The log message to be decoded
            format (str): The format used to create the log entry
        
        Returns:
            None

        Raises:
            AssertionError:
                when format is empty or not a string
                when mapping is not valid
        '''
        assert format, "Format is empty"
        assert isinstance(format, str), "Format is not a string"

        _decoded_msg = msg

        # Go through the token map to find any tokens in the format string
        _re_format = format
        for _attr, _val in self._token_map.items():
            assert isinstance(_val, dict), "Token map is invalid"

            # The token to look for is the attr surrounded by delimiters
            _delimiters = _val.get("delimiters", [])
            assert isinstance(_delimiters, list) and len(_delimiters) > 1, (
                "Token map delimiters are invalid"
            )

            _start_delimiter = _delimiters[0]
            _end_delimiter = _delimiters[1]

            _attr_type = TOKEN_TYPING.get(_attr, "s")
            _format_token = (
                f"{_start_delimiter}"
                f"%({_attr}){_attr_type}"
                f"{str(_end_delimiter)}"
            )

            # Replace the token in the format with a regular expression
            if _start_delimiter in DELIMITERS_TO_ESCAPE:
                _start_delimiter = f"\\{_start_delimiter}"

            if _end_delimiter in DELIMITERS_TO_ESCAPE:
                _end_delimiter = f"\\{_end_delimiter}"

            _regexp = (
                f"{_start_delimiter}"
                f"(?P<{_attr}>.*)"
                f"{_end_delimiter}"
            )

            _re_format = _re_format.replace(_format_token, _regexp)

        # Remove the 'message' attribute
        # The message attribute is set from everything left over
        _re_format = _re_format.replace("%(message)s", "")

        match = re.match(fr"^{_re_format}", msg)
        if match:
            # Process the matched entries
            for _key, _val in match.groupdict().items():
                # Get the mapto property, and set the attr in the instance
                _token = self._token_map.get(_key, None)
                if _token and isinstance(_token, dict):
                    _mapto = _token.get("mapto", None)
                    _delims = _token.get("delimiters", [])
                else:
                    _mapto = None
                    _delims = []

                if _mapto and hasattr(self, f"_{_mapto}"):
                    setattr(self, f"_{_mapto}", _val)

                # Remove the val from the entry string
                assert isinstance(_delims, list) and len(_delims) > 1, (
                    "Token map delimiters are invalid"
                )
                _val_to_del = f"{_delims[0]}{_val}{_delims[1]}"

                _decoded_msg = _decoded_msg.replace(_val_to_del, "")

        # Whatever is left in the message can be used as the message component
        self._message = _decoded_msg.strip()


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

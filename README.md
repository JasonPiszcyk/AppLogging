# AppLogging
Copyright (c) 2025 Jason Piszcyk

Applications Components - Network Communications.

<!-- 
Not yet Published to PyPi
[![PyPI version](https://badge.fury.io/py/applogging.svg)](https://pypi.org/project/applogging/)
[![Build Status](https://github.com/JasonPiszcyk/AppLogging/actions/workflows/python-app.yml/badge.svg)](https://github.com/JasonPiszcyk/AppLogging/actions)
 -->


## Overview


**AppLogging** provides components to simplify the usage of python logging.


## Features


**AppLogging** consists of a number of sub-modules, being:
- [Logging](#logging-usage)
  - General functions to provide a simplified interface to the python logging module
- [LogEntry](#logentry-usage)
  - A class for processing a log entry string (ie from a log file) and providing access to any tokens


## Installation

Module has not been published to PyPi yet.  Install via:
```bash
pip install "applogging @ git+https://github.com/JasonPiszcyk/AppLogging"
```


## Requirements

Python >= 3.8

> [!NOTE]
> The module has been tested against Python 3.8 and 3.14.


## Dependencies

- pytest


## Usage


### <a id="logging-usage"></a>Logging


**is_valid_log_level_string(** level="" **)**

> Return *True* if the supplied log level string is valid, *False* otherwise.

> | Argument | Description |
> | - | - |
> | **level** (str) | A string representing a log level |


**get_logger(** name=None **)**

> Return the logging instance associated with name.  Creates the logging instance if necessary.

> | Argument | Description |
> | - | - |
> | **name** (str | None) | The name of the logger to get. If name is None (an empty string is invalid) return the root logger. |


**init_console_logger(** name=None **)**

> Return a logging instance, associated with *name*, configured to output to the console.
> [!CAUTION]
> This will overwrite the configuration of the named logger. If the logger is None, the root logger config will be cleared and set to log to a console.

> | Argument | Description |
> | - | - |
> | **name** (str | None) | The name of the logger to initialise. If name is None (an empty string is invalid) init the root logger. |


**init_file_logger(** name=None, filename="" **)**

> Return a logging instance, associated with *name*, configured to output to *filename*.
> [!NOTE]
> The handler will be a timed rotaing file handler useing the defaults for the [handler_to_timed_rotating_file](#func_handler_to_timed_rotating_file)
> [!CAUTION]
> This will overwrite the configuration of the named logger. If the logger is None, the root logger config will be cleared and set to log to *filename*.

> | Argument | Description |
> | - | - |
> | **name** (str | None) | The name of the logger to initialise. If name is None (an empty string is invalid) init the root logger. |
> | **filename** (str) | The name of the file to use for logging. |


**clear_handlers(** logger=None **)**

> Clear any handlers associated with the logger.

> | Argument | Description |
> | - | - |
> | **logger** (logging.Logger) | An instance of a logger object. |


**get_log_level(** logger=None **)**

> Return the current log level for a logger, as a string.

> | Argument | Description |
> | - | - |
> | **logger** (logging.Logger) | An instance of a logger object. |


**set_log_level(** logger=None, level="INFO" **)**

> Set the current log level for a logger.

> | Argument | Description |
> | - | - |
> | **logger** (logging.Logger) | An instance of a logger object. |
> | **level** (str) | A valid log level as a string. |


**handler_to_console(** format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s", name="TO_CONSOLE" **)**

> Return a handler to log to the console.

> | Argument | Description |
> | - | - |
> | **format** (format) | The format to use for the log output. This is a string containing [log attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes). Default = "%(asctime)s: [%(name)s] [%(levelname)s] %(message)s" |
> | **name** (str) | A name for the handle.  Default = "TO_CONSOLE". |


**handler_to_file(** filename="", format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s" **)**

> Return a handler to log to *filename*.

> | Argument | Description |
> | - | - |
> | **filename** (str) | Name of the file to use for logging. |
> | **format** (format) | The format to use for the log output. This is a string containing [log attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes). Default = "%(asctime)s: [%(name)s] [%(levelname)s] %(message)s" |


**<a id="func_handler_to_timed_rotating_file"></a>handler_to_timed_rotating_file(** filename="", format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s", when="W6", at_time=*datetime.time*, copies=5 **)**

> Return a handler to log to to *filename*. The log file will be automatically rotated on a schedule. See [Timed Rotating File Handler](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler) for more information.

> | Argument | Description |
> | - | - |
> | **filename** (str) | A name for the handle.  Default = "TO_CONSOLE". |
> | **format** (str) | The format to use for the log output. This is a string containing [log attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes). Default = "%(asctime)s: [%(name)s] [%(levelname)s] %(message)s" |
> | **when** (str) | Weekday on wich to rotate the file one of: "W0", "W1", "W2", "W3", "W4", "W5", "W6". "W0" = Monday. Default = "W6". |
> | **at_time** (str) | A *datetime.time* instance indicating the time to roate the file. Default = datetime.time(0, 0, 0) (midnight). |
> | **copies** (int) | The number of copies of the log file.  Default = 5. |


### <a id="logentry-usage"></a>LogEntry

#### *class* AppLogging.**LogEntry**(*msg="", format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s", token_map={}*)

LogEntry processes log string *msg* and attempts to decode it into the class properties. The expected format of the log entry is described by *format*.  Any entries that cannot be decoded are added to *message*.

To decode the message, the process looks for various tokens as described by the [token map](#token_map). Changes and additions to the token map can be made via the arg *token_map*.

| Argument | Description |
| - | - |
| **msg** (str) | The log message to be decoded |
| **format** (str) | The format used to create the log output. This is a string containing [log attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes). Default = "%(asctime)s: [%(name)s] [%(levelname)s] %(message)s" |
| **token_map** (str) | Modifications to the default mapping dict used to extract the tokens.  Format should be as per [token map](#token_map). |


| Property | Description |
| - | - |
| **time** (str) [ReadOnly] | The time the entry was logged |
| **logger_name** (str) [ReadOnly] | The name of the logger used |
| **severity** (str) [ReadOnly] | The severity of the log message |
| **source** (str) [ReadOnly] | The source of the log message |
| **process_id** (str) [ReadOnly] | The process ID that logged the message |
| **process_name** (str) [ReadOnly] | The process Name that logged the message |
| **thread_id** (str) [ReadOnly] | The thread ID that logged the message |
| **thread_name** (str) [ReadOnly] | The thread Name that logged the message |
| **message** (str) [ReadOnly] | The message |

**<a id="token_map"></a>Token Map**

The token map is a list of rules to extract tokens from the log string. An entry in the map contains:
- The entry name corresponding to an attribute in *format*
- A dict containing:
  - "mapto" - The class property to map the entry to
  - "delimiters" - The delimiters surrounding the token in the log message

To modify the token map, just provide the entry to be changed.  There is no need to respecify the whole map.

> [!NOTE]
> It is not necessary to specify 'message' as this is the default for anything that cannot be decoded.

```python
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
```


### Examples

```python
# Example Usage
import applogging

# To create a logger outputting to STDOUT/STDERR
log = applogging.init_console_logger(name="Non-Default Logger")

# Set the level accepted by the logger
log.setLevel(level="DEBUG")

# Log a message
log.error("The message")

# Access the logger fom a different module
log_created_elsewhere = applogging.get_logger(name="Non-Default Logger")
log_created_elsewhere.error("A different message to previously created logger")

```

## Development

1. Clone the repository:
    ```bash
    git clone https://github.com/JasonPiszcyk/AppLogging.git
    cd AppLogging
    ```
2. Install dependencies:
    ```bash
    pip install -e .[dev]
    ```

## Running Tests

```bash
pytest
```

## Contributing

Contributions are welcome! Please submit issues or pull requests via [GitHub Issues](https://github.com/JasonPiszcyk/AppLogging/issues).

## License

GNU General Public License

## Author

Jason Piszcyk  
[Jason.Piszcyk@gmail.com](mailto:Jason.Piszcyk@gmail.com)

## Links

- [Homepage](https://github.com/JasonPiszcyk/AppLogging)
- [Bug Tracker](https://github.com/JasonPiszcyk/AppLogging/issues)

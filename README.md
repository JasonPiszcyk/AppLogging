# AppLogging
Copyright (c) 2025 Jason Piszcyk

Applications Components - Network Communications.

<!-- 
Not yet Published to PyPi
[![PyPI version](https://badge.fury.io/py/applogging.svg)](https://pypi.org/project/applogging/)
[![Build Status](https://github.com/JasonPiszcyk/AppLogging/actions/workflows/python-app.yml/badge.svg)](https://github.com/JasonPiszcyk/AppLogging/actions)
 -->

## Overview

**AppLogging** provides components to build network communications

## Features

**AppLogging** consists of a number of sub-modules, being:
- Logging
  - General functions to provide a simplified interface to the python logging module
- LogEntry
  - A class for processing a log entry string (ie from a log file) and providing access to any tokens.

## Installation

Module has not been published to PyPi yet.  Install via:
```bash
pip install "applogging @ git+https://github.com/JasonPiszcyk/AppLogging"
```

## Requirements

- Python >= 3.8

**NOTE:** The module has been built and tested against Python 3.14 and 3.8

## Dependencies

- pytest

## Usage

```python
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

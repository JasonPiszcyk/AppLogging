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
- Multiprocessing
  - A generalised Task interface proving multiprocessing via Process and Threads
    - Task Lifecycle management including starting, stopping and watchdog processing to ensure task state

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
- "crypto_tools @ git+https://github.com/JasonPiszcyk/CryptoTools"

## Usage

```python
import applogging
# Example usage of AppLogging components
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

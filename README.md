# aelf-api-client

An unofficial Python client for interacting with the [AELF API](https://api.aelf.org/). This library provides an easy-to-use interface for fetching liturgical information from the AELF API.

## Table of contents
- [aelf-api-client](#aelf-api-client)
  - [Table of contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Available Methods:](#available-methods)
  - [Development](#development)
    - [Setting Up the Local Environment](#setting-up-the-local-environment)
    - [Running Tests](#running-tests)
    - [Code Formatting and Linting](#code-formatting-and-linting)
  - [Contributing](#contributing)
  - [License](#license)
  - [Links](#links)

## Features

- Fetch liturgical information for a specific date and zone.
- Retrieve prayers such as `laudes`, `vepres`, `tierce`, `sexte`, and more.
- Built with `aiohttp` for asynchronous requests.
- Validates API responses using `pydantic` models.

## Installation

Package is directly available from the Pypi repositories:

```bash
pip install aelf-api-client
```

## Usage

Example: Fetch masses informations

```python
from datetime import datetime

import asyncio

from aelf_api_client import AELFClient
from aelf_api_client.schemas.enums import ZonesEnum

async def main():
    client = AELFClient()
    date = datetime.now()
    zone = ZonesEnum.FRANCE

    # Fetch messes
    messes = await client.request_messes(date, zone)
    print(messes)

asyncio.run(main())
```

## Available Methods:
The AELFClient provides the following methods:

- `request_informations(date: datetime, zone: ZonesEnum)` -> **InformationsResponseModel**
- `request_messes(date: datetime, zone: ZonesEnum)` -> **MessesResponseModel**
- `request_complies(date: datetime, zone: ZonesEnum)` -> **CompliesResponseModel**
- `request_laudes(date: datetime, zone: ZonesEnum)` -> **LaudesResponseModel**
- `request_lectures(date: datetime, zone: ZonesEnum)` -> **LecturesResponseModel**
- `request_none(date: datetime, zone: ZonesEnum)` -> **NoneResponseModel**
- `request_sexte(date: datetime, zone: ZonesEnum)` -> **SexteResponseModel**
- `request_tierce(date: datetime, zone: ZonesEnum)` -> **TierceResponseModel**
- `request_vepres(date: datetime, zone: ZonesEnum)` -> **VepresResponseModel**

Each method fetches data for a specific liturgical endpoint and returns a validated response model.


## Development

### Setting Up the Local Environment
```bash
git clone git@github.com:thamin-i/aelf-api-client.git
cd aef-client
make install
```

### Running Tests

Tests are written using `pytest`. To run the tests:
```bash
poetry run pytest
```

### Code Formatting and Linting

This project uses `ruff`, `isort`, and `pylint` for formatting and linting. To check the code:
```bash
make format_code && make check_code
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Write tests for your changes.
4. Run the tests to ensure everything works.
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Links
- Pypi: [Project](https://pypi.org/project/aelf-api-client)
- Homepage: [AELF Python Client](https://github.com/thamin-i/aelf-api-client)
- Issues: [https://github.com/thamin-i/aelf-api-client/issues](https://github.com/thamin-i/aelf-api-client/issues)

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
- Retrieve liturgical entities (`masses`, `complines`, `lauds`, `readings`, `none`, `sext`, `terce` or `vespers`) for a specific date and zone.
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
from aelf_api_client.schemas.enums import ZoneEnum, EntityEnum
from aelf_api_client.schemas.responses import MassesResponseModel

async def main():
    client = AELFClient()
    date = datetime.now()
    zone = ZoneEnum.FRANCE

    masses: MassesResponseModel

    # 2 ways to fetch a liturgical entity:
    masses = await client.request_masses(date=date, zone=zone)
    # or
    masses = await client.request(entity=EntityEnum.MASS, date=date, zone=zone)

    print(masses)

asyncio.run(main())
```

## Available Methods:
The AELFClient provides the following methods:

- `request(entity: EntityEnum, date: datetime, zone: ZonesEnum)`: Fetch any liturgical entity for a given day and zone
- `request_informations(date: datetime, zone: ZonesEnum)`: Fetch informations for a given day and zone
- `request_masses(date: datetime, zone: ZonesEnum)`: Fetch masses for a given day and zone
- `request_complines(date: datetime, zone: ZonesEnum)`: Fetch comlines for a given day and zone
- `request_lauds(date: datetime, zone: ZonesEnum)`: Fetch lauds for a given day and zone
- `request_readings(date: datetime, zone: ZonesEnum)`: Fetch readings for a given day and zone
- `request_none(date: datetime, zone: ZonesEnum)`: Fetch none for a given day and zone
- `request_sext(date: datetime, zone: ZonesEnum)`: Fetch sext for a given day and zone
- `request_terce(date: datetime, zone: ZonesEnum)`: Fetch terce for a given day and zone
- `request_vespers(date: datetime, zone: ZonesEnum)`: Fetch vespers for a given day and zone

Each method fetches data for a specific liturgical entity and returns a validated Pydantic response model.


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

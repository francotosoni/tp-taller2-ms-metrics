# FastAPI template

![Tests](https://github.com/Taller2SnapMsg/fastapi_template/actions/workflows/tests.yaml/badge.svg)

* development check: checks that all tests pass and code is correctly formatted

requirements: `docker`, `docker-compose` and `poetry`

# Usage

Create an `.env` file based on `.env.template`.

For development: `docker-compose up`

For production: `docker-compose -f docker-compose.prod.yaml up`

# Tests

`poetry run pytest`

# Code Format and Linter

`poetry run black .`

`poetry run flake8 .`

`poetry run mypy .`

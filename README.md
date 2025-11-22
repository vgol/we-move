# We move

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/badge/ruff-passing-brightgreen.svg?style=flat&logo=ruff&logoColor=white)](https://github.com/astral-sh/ruff)
[![Mypy](https://img.shields.io/badge/mypy-passing-brightgreen.svg?style=flat&logo=python&logoColor=white)](http://mypy-lang.org/)
[![Coverage](https://img.shields.io/codecov/c/github/vgol/lazy-seller?flag=backend&logo=python&logoColor=white&label=backend%20coverage)](https://codecov.io/gh/vgol/lazy-seller)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.0%2B-3776AB.svg?style=flat&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)

LLM-assisted data pipeline for long-term apartment listings in Berlin. We scrape provider websites, normalize records into rich Pydantic models, persist batches as JSON, and keep cloud copies on Google Drive. Dash/Plotly apps plus ipykernel notebooks power interactive filtering and grouping.

For the strategic blueprint (data contracts, ingestion loop, integration plan) read `instructions/PIPELINE_BLUEPRINT.md`.

## Current State

- Project scaffold created with `uv` and Python 3.13+ runtime (targeting 3.14 semantics).
- Core directories for scraping, pipelines, transformers, storage, analytics, and data lakes are in place.
- Dependency stack includes Dash, Plotly, FastAPI, Pydantic, Google Drive SDK, Typer CLI, Tenacity retries.
- Configuration handled via `app/core/config.py` (Pydantic settings) with placeholders for Drive + LLM credentials.

## Near-Term Roadmap

- Stand up canonical Pydantic models (`RawListing`, `ListingEnvelope`, pricing/location submodels).
- Implement scraper base class + source-specific extractors with polite crawling controls.
- Add LLM-powered transformers for enrichment and deduplication.
- Ship JSON batch writers and Drive upload chainlink.
- Build first Dash dashboard + exploratory notebooks pulling from `data/normalized`.

Details, sequencing, and acceptance criteria live in `instructions/PIPELINE_BLUEPRINT.md`; keep that doc authoritative to avoid duplicating content here.

## Repository Map

| Path | Purpose |
| --- | --- |
| `app/` | Runtime code (scrapers, pipelines, analytics, storage connectors). |
| `app/core/` | Config + logging utilities shared across modules. |
| `data/raw`, `data/normalized`, `data/manifests` | JSON lakes for scraped and enriched payloads. |
| `instructions/PIPELINE_BLUEPRINT.md` | End-to-end architecture and contracts. |
| `instructions/PYTHON_GUIDELINES.md` | Coding rules (modern Python only, typing expectations). |
| `notebooks/` | ipykernel notebooks for EDA and ranking experiments. |

## Development Setup

```bash
# install project dependencies
uv sync --all-groups

# run the placeholder app entrypoint
uv run python -m app.main

# add or remove packages
uv add <package>
uv remove <package>
```

Use `.env` for secrets (LLM keys, Google Drive IDs). Settings are exposed through `app/core/config.py`.

## Contribution Notes

- Review `instructions/PYTHON_GUIDELINES.md` before authoring Python code; future-import polyfills (e.g., `from __future__ import annotations`) are not allowed under Python 3.14.
- Consult `instructions/PIPELINE_BLUEPRINT.md` prior to editing pipelines to keep implementations aligned with the contract.
- Tests and linting are managed through `pytest`, `ruff`, and `mypy` (see `pyproject.toml`).

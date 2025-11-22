# We Move Data Pipeline Blueprint

## 1. Mission Summary
- Build an LLM-assisted scraping and enrichment pipeline for long-term Berlin apartment listings.
- Persist every raw and normalized record as JSON that adheres to strict Pydantic models.
- Orchestrate lightweight storage via local files, then sync to Google Drive for sharing and backup.
- Provide interactive filtering and grouping via notebooks, Plotly visualizations, and Dash apps.

## 2. Guiding Principles
1. **Data fidelity first** – capture as much structured context as possible for each offer (pricing, geography, contact, amenities, policies, availability windows).
2. **Deterministic contracts** – all internal steps operate on typed Pydantic models to prevent silent schema drift.
3. **Modular ingestion** – each source website gets its own scraper + normalizer pair conforming to shared base classes.
4. **Storage independence** – local JSON shards are the source of truth, while cloud sinks (Google Drive) remain interchangeable connectors.
5. **LLM-in-the-loop** – use foundation models for assisted parsing, entity normalization, or deduplication where HTML is inconsistent.

## 3. Target End-to-End Flow
1. **Discovery** – scheduler fetches target URLs + metadata from `app/scraping/manifests`.
2. **Acquisition** – scraper fetches HTML/JSON using `requests` + optional headless browser hooks.
3. **Structuring** – parser emits `RawListing` (Pydantic) objects capturing site-native fields.
4. **Enrichment** – LLM-powered transformer upgrades `RawListing` to canonical `ListingEnvelope` (pricing breakdowns, amenities, policy tags, embeddings).
5. **Persistence** – listings serialized to versioned JSON files (one file per batch) under `data/raw` and `data/normalized`.
6. **Sync** – Google Drive connector uploads batch manifests + payloads, preserving lineage metadata.
7. **Exploration** – notebooks + Dash app consume normalized JSON via pandas for filtering/grouping and interactive dashboards.

## 4. Core Data Contracts (Pydantic)
- `SourceMeta`: provider slug, crawl timestamp, locale, URL, parser version.
- `ContactInfo`: landlord/agency name, email, phone, preferred language, response ETA.
- `Pricing`: currency, base rent, deposit, utilities, services, historical list.
- `Location`: street, district, coordinates, nearby transit, noise score.
- `AmenitySet`: boolean flags + free-form descriptors (pets, furnished, balcony, elevator, workspace, energy class).
- `Policy`: min/max stay, documents required, background checks, allowed occupants.
- `RawListing`: raw dicts as scraped, html snapshot pointers, SourceMeta.
- `ListingEnvelope`: fully normalized record referencing all nested models + LLM reasoning traces.

## 5. Integration Surfaces
- **Google Drive** – Service-account OAuth, resumable uploads, folder-per-environment layout, signed URLs stored beside JSON.
- **LLM Services** – abstract client for OpenAI/Anthropic/Azure; deterministic wrapper enabling retries + cost tracking.
- **Dash/Plotly UI** – thin Dash server reading from `data/normalized` and providing filter panels (district, price bands, amenities, stay length).
- **ipykernel notebooks** – curated notebooks under `notebooks/experiments` for ad-hoc EDA, dedupe analysis, ranking experiments.

## 6. Tooling & Ops
- **Runtime**: Python 3.13, `uv` for packaging, Ruff + Mypy for quality gates.
- **Testing**: pytest suite covering scrapers (responses), data models, storage connectors, Drive uploads (via fakes).
- **Observability**: structured logging (JSON), per-source metrics, Drive sync audit logs.
- **Configuration**: `.env` + `app/core/config.py` exposing typed settings (API keys, folder IDs, concurrency limits).

## 7. Immediate Backlog
1. Implement Pydantic models + validation strategies.
2. Build generic scraper base class w/ caching + politeness features (rate limits, rotating headers).
3. Serialize batch outputs and register them with a Drive uploader stub.
4. Create Dash prototype that reads normalized JSON and renders interactive histograms/maps.
5. Author notebooks for initial filtering/grouping experiments (ipykernel + Plotly).

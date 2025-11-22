"""Centralized application settings."""

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed configuration loaded from env vars and .env files."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    environment: Literal["local", "dev", "prod"] = Field(default="local")
    data_raw_dir: Path = Field(default=Path("data/raw"))
    data_normalized_dir: Path = Field(default=Path("data/normalized"))
    data_manifest_dir: Path = Field(default=Path("data/manifests"))

    google_service_account_file: Path | None = None
    google_drive_parent_id: str | None = None

    llm_provider: Literal["openai", "anthropic", "azure_openai"] | None = None
    llm_model: str | None = None
    llm_api_key: str | None = None

    request_timeout_seconds: int = Field(default=30, ge=1, le=120)
    max_concurrent_requests: int = Field(default=3, ge=1, le=20)
    drive_upload_chunk_size: int = Field(default=8 * 1024 * 1024)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached Settings instance to avoid reparsing env files."""

    return Settings()

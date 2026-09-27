"""Application settings loaded from environment variables (see .env.example)."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    model: str = os.getenv("AGENT_MODEL", "")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    phoenix_project_name: str = os.getenv("PHOENIX_PROJECT_NAME", "")
    phoenix_collector_endpoint: str = os.getenv("PHOENIX_COLLECTOR_ENDPOINT", "")


settings = Settings()

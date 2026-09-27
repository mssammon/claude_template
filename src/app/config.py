"""Application settings loaded from environment variables (see .env.example)."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    model: str = os.getenv("AGENT_MODEL", "")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()

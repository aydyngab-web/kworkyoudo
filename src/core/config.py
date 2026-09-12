"""Environment-based configuration for portfolio integrations."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    api_base_url: str
    api_token: str
    request_timeout: float = 15.0

    @classmethod
    def from_env(cls) -> "Settings":
        base_url = os.getenv("API_BASE_URL", "").strip()
        token = os.getenv("API_TOKEN", "").strip()
        if not base_url:
            raise RuntimeError("API_BASE_URL is required")
        if not token:
            raise RuntimeError("API_TOKEN is required")
        return cls(api_base_url=base_url.rstrip("/"), api_token=token)

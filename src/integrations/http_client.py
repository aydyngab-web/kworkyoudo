"""Reusable async HTTP client for API integrations."""

from __future__ import annotations

import json
from dataclasses import dataclass
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from src.core.config import Settings
from src.core.retry import with_retry


@dataclass
class ApiResponse:
    status: int
    data: dict


class ApiClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def get_json(self, path: str) -> ApiResponse:
        async def request() -> ApiResponse:
            import asyncio
            return await asyncio.to_thread(self._sync_get, path)

        return await with_retry(request, retry_on=(URLError, TimeoutError))

    def _sync_get(self, path: str) -> ApiResponse:
        url = f"{self.settings.api_base_url}/{path.lstrip('/')}"
        request = Request(
            url,
            headers={
                "Authorization": f"Bearer {self.settings.api_token}",
                "Accept": "application/json",
                "User-Agent": "ai-automation-lab/1.0",
            },
        )
        try:
            with urlopen(request, timeout=self.settings.request_timeout) as response:
                payload = json.loads(response.read().decode("utf-8"))
                return ApiResponse(status=response.status, data=payload)
        except HTTPError as exc:
            raise RuntimeError(f"API returned HTTP {exc.code}") from exc

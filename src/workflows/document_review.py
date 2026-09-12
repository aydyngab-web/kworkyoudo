"""Sanitized example inspired by AI document-analysis products.

It demonstrates workflow orchestration and structured outputs without containing
production prompts, customer documents or provider credentials.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class DocumentReview:
    summary: str
    key_terms: list[str]
    risk_flags: list[str]
    score: int


class DocumentAnalyzer(Protocol):
    async def analyze(self, text: str) -> DocumentReview: ...


async def review_document(text: str, analyzer: DocumentAnalyzer) -> DocumentReview:
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("Document text cannot be empty")

    result = await analyzer.analyze(cleaned)
    if not 0 <= result.score <= 100:
        raise ValueError("Analyzer score must be between 0 and 100")
    return result

"""Small, testable tool-orchestration layer for AI automation demos.

The agent does not pretend to be human and does not require a live LLM key.
An LLM adapter can choose a registered tool, while execution remains explicit,
validated and easy to test.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Awaitable, Callable

ToolHandler = Callable[[dict[str, Any]], Awaitable[dict[str, Any]]]


@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    handler: ToolHandler


class ToolAgent:
    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        if tool.name in self._tools:
            raise ValueError(f"Tool already registered: {tool.name}")
        self._tools[tool.name] = tool

    def available_tools(self) -> list[dict[str, str]]:
        return [
            {"name": tool.name, "description": tool.description}
            for tool in self._tools.values()
        ]

    async def execute(self, tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        tool = self._tools.get(tool_name)
        if tool is None:
            raise KeyError(f"Unknown tool: {tool_name}")
        return await tool.handler(arguments)

import unittest

from src.agents.tool_agent import Tool, ToolAgent


class ToolAgentTests(unittest.IsolatedAsyncioTestCase):
    async def test_register_and_execute_tool(self):
        async def lookup(arguments):
            return {"query": arguments["query"], "result": "demo-result"}

        agent = ToolAgent()
        agent.register(Tool("lookup", "Look up structured information", lookup))

        result = await agent.execute("lookup", {"query": "invoice"})

        self.assertEqual(result["result"], "demo-result")
        self.assertEqual(agent.available_tools()[0]["name"], "lookup")

    async def test_unknown_tool_fails_explicitly(self):
        agent = ToolAgent()
        with self.assertRaises(KeyError):
            await agent.execute("missing", {})


if __name__ == "__main__":
    unittest.main()

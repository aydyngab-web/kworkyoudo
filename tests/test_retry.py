import asyncio
import unittest

from src.core.retry import with_retry


class RetryTests(unittest.IsolatedAsyncioTestCase):
    async def test_returns_successful_result(self):
        async def operation():
            return "ok"

        result = await with_retry(operation)
        self.assertEqual(result, "ok")

    async def test_retries_transient_failure(self):
        calls = 0

        async def operation():
            nonlocal calls
            calls += 1
            if calls < 3:
                raise TimeoutError("temporary")
            return 42

        result = await with_retry(operation, attempts=3, base_delay=0)
        self.assertEqual(result, 42)
        self.assertEqual(calls, 3)


if __name__ == "__main__":
    unittest.main()

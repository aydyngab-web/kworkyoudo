import unittest

from src.workflows.document_review import DocumentReview, review_document


class FakeAnalyzer:
    async def analyze(self, text: str) -> DocumentReview:
        return DocumentReview(
            summary=f"Reviewed {len(text)} characters",
            key_terms=["term"],
            risk_flags=["example risk"],
            score=78,
        )


class DocumentReviewTests(unittest.IsolatedAsyncioTestCase):
    async def test_structured_review(self):
        result = await review_document("Example agreement", FakeAnalyzer())
        self.assertEqual(result.score, 78)
        self.assertTrue(result.risk_flags)

    async def test_empty_document_rejected(self):
        with self.assertRaises(ValueError):
            await review_document("   ", FakeAnalyzer())


if __name__ == "__main__":
    unittest.main()

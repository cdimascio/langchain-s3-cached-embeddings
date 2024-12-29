import random

class MockEmbeddings:
    """A mock implementation of the Embeddings interface for testing purposes."""

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Simulate embedding a list of documents."""
        # Return a list of random embeddings (each embedding is a list of 300 float values)
        return [[random.random() for _ in range(300)] for _ in texts]

    def embed_query(self, text: str) -> list[float]:
        """Simulate embedding a single query."""
        # Return a random embedding for the query (a list of 300 float values)
        return [random.random() for _ in range(300)]

    async def aembed_documents(self, texts: list[str]) -> list[list[float]]:
        """Asynchronously embed a list of documents."""
        # Mimic the synchronous behavior, but this could be done asynchronously if needed
        return await self._simulate_async(self.embed_documents, texts)

    async def aembed_query(self, text: str) -> list[float]:
        """Asynchronously embed a single query."""
        # Mimic the synchronous behavior, but this could be done asynchronously if needed
        return await self._simulate_async(self.embed_query, text)

    async def _simulate_async(self, method, *args, **kwargs):
        """Simulate async embedding (in place of real async calls to an external service)."""
        # This is just a basic simulation of asynchronous behavior.
        return method(*args, **kwargs)
from calendar import c
import unittest
import pytest
from src.facades.hatchways import HatchwaysFacade

MOCK_HATCHWAYS_RESULT = {
    "posts": [
        {
            "id": 1,
            "author": "Rylee Paul",
            "authorId": 9,
            "likes": 960,
            "popularity": 0.13,
            "reads": 50361,
            "tags": ["tech", "health"],
        }
    ]
}

MOCK_HATCHWAYS_RESULT_1 = {
    "posts": [
        {
            "id": 2,
            "author": "Rylee Paul",
            "authorId": 9,
            "likes": 960,
            "popularity": 0.13,
            "reads": 50361,
            "tags": ["tech", "health"],
        }
    ]
}


class AsyncContextManagerMock:
    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        return self

    async def json(self):
        return MOCK_HATCHWAYS_RESULT


class TestHatchwaysFacade(unittest.TestCase):
    def setUp(self):
        self.sut = HatchwaysFacade()

    @pytest.mark.asyncio
    async def test_call_hatchways_api(self, monkeypatch=pytest.MonkeyPatch):
        def mock_client_get(self, auth_path, params):
            mock_response = AsyncContextManagerMock()
            mock_response.status = 200
            return mock_response.json

        monkeypatch.setattr("aiohttp.ClientSession.get", mock_client_get)
        result = await self.sut.fetch_blogs("science")

        assert result == MOCK_HATCHWAYS_RESULT_1

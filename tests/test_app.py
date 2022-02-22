import json
import unittest

from src.app import app
from src.exceptions.invalid_direction_exception import INVALID_DIRECTION_ERROR
from src.exceptions.invalid_sort_by_exception import INVALID_SORT_BY_ERROR
from src.exceptions.invalid_tag_exception import INVALID_TAG_ERROR
from src.exceptions.missing_tag_exception import MISSING_TAG_ERROR

PING_RESPONSE_200 = {"success": True}

VALID_SORT_BY_PARAMS = [
    "id",
    "reads",
    "likes",
    "popularity",
]

VALID_DIRECTION_PARAMS = [
    "asc",
    "desc",
]


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_ping_returns_200(self):
        response = self.app.get("/api/ping", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), PING_RESPONSE_200)

    def test_ping_with_args_returns_200(self):
        response = self.app.get("/api/ping?tags=potato", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_posts_with_no_tags_returns_400(self):
        response = self.app.get("/api/posts", follow_redirects=True)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), MISSING_TAG_ERROR)

    def test_posts_with_invalid_tags_returns_400(self):
        response = self.app.get("/api/posts?tags=design,", follow_redirects=True)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), INVALID_TAG_ERROR)

    def test_posts_with_invalid_sort_by_returns_400(self):
        response = self.app.get(
            "/api/posts?tags=design&sortBy=potatoes", follow_redirects=True
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), INVALID_SORT_BY_ERROR)

    def test_posts_with_invalid_direction_returns_400(self):
        response = self.app.get(
            "/api/posts?tags=design&direction=up", follow_redirects=True
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), INVALID_DIRECTION_ERROR)

    def test_posts_with_invalid_direction_returns_400(self):
        response = self.app.get(
            "/api/posts?tags=design&direction=up", follow_redirects=True
        )
        self.assertEqual(response.status_code, 400)

    if __name__ == "__main__":
        unittest.main()

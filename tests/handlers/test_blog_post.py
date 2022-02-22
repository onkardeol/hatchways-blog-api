import unittest
from unittest.mock import patch
from src.facades.hatchways import HatchwaysFacade
from src.handlers.blog_post import BlogPostHandler
from src.parsers.blog_post import DEFAULT_DIRECTION_PARAM, DEFAULT_SORT_BY_PARAM

from tests.api_call_constants import (
    API_RESPONSE_ALL_PARAMS,
    API_RESPONSE_DIRECTION,
    API_RESPONSE_SORT_BY,
    API_RESPONSE_TAG,
    UNSORTED_API_RESPONSE,
)


class TestApp(unittest.TestCase):
    def setUp(self):
        self.sut = BlogPostHandler(HatchwaysFacade())

    def tearDown(self):
        pass

    @patch("src.facades.hatchways.HatchwaysFacade.fetch_blogs")
    def test_handle_blog_post_returns_posts_with_default_values(self, fetch_blogs_mock):
        fetch_blogs_mock.return_value = UNSORTED_API_RESPONSE

        handle_blogs = self.sut.handle_blogs(
            tags="design",
            sort_by=DEFAULT_SORT_BY_PARAM,
            direction=DEFAULT_DIRECTION_PARAM,
        )

        assert handle_blogs == API_RESPONSE_TAG
        fetch_blogs_mock.assert_called_once()

    @patch("src.facades.hatchways.HatchwaysFacade.fetch_blogs")
    def test_handle_blog_post_returns_posts_with_direction(self, fetch_blogs_mock):
        fetch_blogs_mock.return_value = UNSORTED_API_RESPONSE

        handle_blogs = self.sut.handle_blogs(
            tags="design", sort_by=DEFAULT_SORT_BY_PARAM, direction="desc"
        )

        assert handle_blogs == API_RESPONSE_DIRECTION
        fetch_blogs_mock.assert_called_once()

    @patch("src.facades.hatchways.HatchwaysFacade.fetch_blogs")
    def test_handle_blog_post_returns_posts_with_sort_by(self, fetch_blogs_mock):
        fetch_blogs_mock.return_value = UNSORTED_API_RESPONSE

        handle_blogs = self.sut.handle_blogs(
            tags="design", sort_by="popularity", direction=DEFAULT_DIRECTION_PARAM
        )

        assert handle_blogs == API_RESPONSE_SORT_BY
        fetch_blogs_mock.assert_called_once()

    @patch("src.facades.hatchways.HatchwaysFacade.fetch_blogs")
    def test_handle_blog_post_returns_posts_with_all_params(self, fetch_blogs_mock):
        fetch_blogs_mock.return_value = UNSORTED_API_RESPONSE

        handle_blogs = self.sut.handle_blogs(
            tags="design", sort_by="likes", direction="desc"
        )

        assert handle_blogs == API_RESPONSE_ALL_PARAMS
        fetch_blogs_mock.assert_called_once()

import unittest
from src.exceptions.invalid_direction_exception import InvalidDirectionException
from src.exceptions.invalid_sort_by_exception import InvalidSortByException
from src.exceptions.invalid_tag_exception import InvalidTagException
from src.exceptions.missing_tag_exception import MissingTagException
from src.parsers.blog_post import BlogPostParser


class TestBlogParser(unittest.TestCase):
    def setUp(self):
        self.sut = BlogPostParser()

    def tearDown(self):
        pass

    def test_no_tag_throws_missing_tag_exception(self):
        self.assertRaises(MissingTagException, self.sut.parse, None, None, None)

    def test_invalid_tags_throws_invalid_tag_exception(self):
        self.assertRaises(InvalidTagException, self.sut.parse, ",,", None, None)
        self.assertRaises(InvalidTagException, self.sut.parse, ",design", None, None)
        self.assertRaises(InvalidTagException, self.sut.parse, "design,", None, None)

    def test_invalid_direction_throws_invalid_direction_exception(self):
        self.assertRaises(
            InvalidDirectionException, self.sut.parse, "design", None, "inorder"
        )

    def test_invalid_sort_by_throws_invalid_sort_by_exception(self):
        self.assertRaises(
            InvalidSortByException, self.sut.parse, "design", "prizes", None
        )

    def test_only_tags_supplied_returns_correct_default_sort_by_and_direction(self):
        tags = "design"
        sort_by = "id"
        direction = "asc"
        self.assertEqual(
            self.sut.parse("design", None, None), (tags, sort_by, direction)
        )

    def test_tag_and_sort_by_supplied_returns_correct_default_direction(self):
        tags = "design"
        sort_by = "likes"
        direction = "asc"
        self.assertEqual(
            self.sut.parse("design", "likes", None), (tags, sort_by, direction)
        )

    def test_tag_and_direction_supplied_returns_correct_default_sort_by(self):
        tags = "design"
        sort_by = "id"
        direction = "desc"
        self.assertEqual(
            self.sut.parse("design", None, "desc"), (tags, sort_by, direction)
        )

    def test_valid_parameters_supplied_returns_back(self):
        tags = "design,tech"
        sort_by = "likes"
        direction = "desc"
        self.assertEqual(
            self.sut.parse("design,tech", "likes", "desc"), (tags, sort_by, direction)
        )

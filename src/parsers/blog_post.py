from src.exceptions.invalid_direction_exception import InvalidDirectionException
from src.exceptions.invalid_sort_by_exception import InvalidSortByException
from src.exceptions.invalid_tag_exception import InvalidTagException
from src.exceptions.missing_tag_exception import MissingTagException

VALID_SORT_BY_PARAMS = {
    "id",
    "reads",
    "likes",
    "popularity",
    None,
}

VALID_DIRECTION_PARAMS = {
    "asc",
    "desc",
    None,
}

DEFAULT_SORT_BY_PARAM = "id"
DEFAULT_DIRECTION_PARAM = "asc"


class BlogPostParser:
    @staticmethod
    def parse(tags, sort_by, direction):

        if tags is None:
            raise MissingTagException

        if ",," in tags or tags.startswith(",") or tags.endswith(","):
            raise InvalidTagException

        if sort_by not in VALID_SORT_BY_PARAMS:
            raise InvalidSortByException

        if direction not in VALID_DIRECTION_PARAMS:
            raise InvalidDirectionException

        if direction is None:
            direction = DEFAULT_DIRECTION_PARAM

        if sort_by is None:
            sort_by = DEFAULT_SORT_BY_PARAM

        return tags, sort_by, direction

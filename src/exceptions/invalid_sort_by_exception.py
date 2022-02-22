INVALID_SORT_BY_ERROR = {"error": "sortBy parameter is invalid"}


class InvalidSortByException(Exception):
    def __init__(self, message=INVALID_SORT_BY_ERROR):
        self.message = message

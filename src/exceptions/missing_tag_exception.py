MISSING_TAG_ERROR = {"error": "Tags parameter is required"}


class MissingTagException(Exception):
    def __init__(self, message=MISSING_TAG_ERROR):
        self.message = message

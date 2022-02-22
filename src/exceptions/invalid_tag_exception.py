INVALID_TAG_ERROR = {"error": "Invalid tags supplied"}


class InvalidTagException(Exception):
    def __init__(self, message=INVALID_TAG_ERROR):
        self.message = message

INVALID_DIRECTION_ERROR = {"error": "direction parameter is invalid"}


class InvalidDirectionException(Exception):
    def __init__(self, message=INVALID_DIRECTION_ERROR):
        self.message = message

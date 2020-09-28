class Error(Exception):
    """Base class for other exceptions"""

    pass


class ServerError(Error):
    """Raised when received a 500 error"""

    pass


class NotFoundError(Error):
    """Raised when received a 404 error"""

    pass

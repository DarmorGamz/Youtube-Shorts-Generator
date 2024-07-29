class OpenAiException(Exception):
    """The base exception class for all OpenAiExceptions"""

class APIError(Exception):
    """Exception raised for errors in the API response."""
    def __init__(self, message="An error occurred with the API"):
        self.message = message
        super().__init__(self.message)

class RequestError(Exception):
    """Exception raised for errors in making the API request."""
    def __init__(self, message="An error occurred while making the request"):
        self.message = message
        super().__init__(self.message)
"""
This module defines custom exception classes for handling errors related to 
the OpenAI API interactions. These exceptions help in identifying specific 
issues that may arise during API requests or responses, making error handling 
more precise and informative.

Classes:
    OpenAiException: The base exception class for all custom exceptions in this module.
    APIError: Raised when an error occurs in the API response.
    RequestError: Raised when an error occurs while making the API request.

Usage:
    try:
        # API call or operation that may fail
    except APIError as e:
        print(f"API Error: {e.message}")
    except RequestError as e:
        print(f"Request Error: {e.message}")

Class Definitions:
    OpenAiException(Exception):
        The base exception class for all OpenAiExceptions. All other custom exceptions 
        in this module inherit from this class.

    APIError(Exception):
        Exception raised for errors in the API response.
        Attributes:
            message (str): Explanation of the error. Defaults to a general error message.

    RequestError(Exception):
        Exception raised for errors in making the API request.
        Attributes:
            message (str): Explanation of the error. Defaults to a general error message.
"""

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

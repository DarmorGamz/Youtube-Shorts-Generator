# coding: utf-8
"""
This module defines the Configuration class, which manages configuration settings 
for interacting with the OpenAI API. It includes attributes for storing the API key 
and a temporary directory path for data storage. The module also ensures the specified 
temporary directory exists or creates it if necessary.

Modules Imported:
- os: Standard library for interacting with the operating system, particularly for file 
    and directory management.
- logging: Standard library for logging error and informational messages.

Classes:
    Configuration: A class to manage configuration settings, including the API key and 
        temporary storage directory.

Usage:
    config = Configuration(api_key="your_api_key", temp_dir="/path/to/temp_dir")

    # Accessing attributes
    print(config.api_key)
    print(config.temp_dir)

    # Example initialization without optional arguments
    default_config = Configuration()
"""

from __future__ import absolute_import
import os
import logging

class Configuration: # pylint: disable=R0903:too-few-public-methods
    """
    A class to manage configuration settings for API interactions.

    Attributes:
        api_key (str): The API key for authenticating requests.
        temp_dir (str): The directory path for temporary storage.
    """

    def __init__(self, api_key=None, temp_dir="temp"):
        """
        Initializes the Configuration with an API key and a temporary directory.

        Args:
            api_key (str, optional): The API key for authenticating requests. If not provided,
                                     defaults to an empty string.
            temp_dir (str, optional): The directory path for temporary storage. Defaults to "temp".

        Raises:
            Exception: If the temporary directory cannot be created or accessed.
        """
        # Authentication Settings
        self.api_key = api_key if api_key else ""

        # Storage
        self.temp_dir = temp_dir
        try:
            os.makedirs(self.temp_dir, exist_ok=True)
        except Exception as e:
            logging.error("Failed to create or access the temporary directory: %s", e)
            raise

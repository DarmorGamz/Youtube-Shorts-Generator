# coding: utf-8
"""
    OpenAI
"""

from __future__ import absolute_import
import os
import logging

class Configuration:
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

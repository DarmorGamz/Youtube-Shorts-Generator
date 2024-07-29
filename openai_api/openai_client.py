# coding: utf-8
"""
    OpenAI
"""

from __future__ import absolute_import
from openai import OpenAI

from openai_api.configuration import Configuration

class OpenAiClient:
    """
    A client for interacting with the OpenAI API.

    Attributes:
        configuration (Configuration): Configuration settings including API key.
        client (OpenAI): An instance of the OpenAI client.
    """

    def __init__(self, configuration=None):
        """
        Initializes the OpenAiClient with a given configuration.

        Args:
            configuration (Configuration, optional): The configuration object containing 
            API settings. If None, initialization will not proceed.

        Raises:
            ValueError: If the configuration is None or lacks necessary attributes.
        """
        if configuration is None:
            raise ValueError("Configuration must be provided and contain necessary API settings.")

        if not isinstance(configuration, Configuration):
            raise TypeError("Invalid configuration type provided.")

        self.configuration: Configuration = configuration
        self.client: OpenAI = OpenAI(api_key=self.configuration.api_key)

    def __enter__(self):
        """
        Enter the runtime context related to this object.

        Returns:
            OpenAiClient: The initialized OpenAiClient instance.
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the runtime context related to this object. Ensures proper cleanup.

        Args:
            exc_type (type): The exception type, if raised.
            exc_value (Exception): The exception value, if raised.
            traceback (Traceback): The traceback object, if an exception is raised.
        """
        self.close()

    def close(self):
        """
        Close the client and release any resources.
        """
        # Add any necessary cleanup operations here

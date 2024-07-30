# coding: utf-8

# flake8: noqa

"""
This module initializes the OpenAI SDK package, providing access to various API clients 
and utilities for interacting with OpenAI's services. It includes clients for text-to-speech 
(TTS), speech-to-text (STT), and chat functionalities, along with configuration management 
and exception handling.

Modules Imported:
- TTSApi: Client for text-to-speech operations.
- STTApi: Client for speech-to-text operations.
- CHATApi: Client for generating chat responses and other text-based outputs.

Clients:
- OpenAiClient: Main client for managing API sessions and requests.
- Configuration: Utility for managing SDK configuration settings.

Exceptions:
- OpenAiException: Base exception class for all custom exceptions in the OpenAI SDK.
- APIError: Raised for errors in the API response.
- RequestError: Raised for errors in making the API request.

Usage:
    from openai_api import TTSApi, STTApi, CHATApi, OpenAiClient, Configuration
    from openai_api.exceptions import OpenAiException, APIError, RequestError

    api_client = OpenAiClient()
    tts_api = TTSApi(api_client)
    stt_api = STTApi(api_client)
    chat_api = CHATApi(api_client)

    # Example usage:
    tts_api.audio_speech_create("Hello, world!")
    transcription = stt_api.audio_transcriptions_create()
    chat_response = chat_api.generate_script("AI and the future")
"""

from __future__ import absolute_import

# Import APIs into SDK package
from openai_api.api.tts_api import TTSApi
from openai_api.api.stt_api import STTApi
from openai_api.api.chat_api import CHATApi

# Import ApiClient and Configuration
from openai_api.openai_client import OpenAiClient
from openai_api.configuration import Configuration

# Import exceptions
from openai_api.exceptions import OpenAiException, APIError, RequestError

# coding: utf-8
"""
This module serves as the package initializer for the OpenAI API SDK package. 
It imports and provides access to various API clients, which interact with 
OpenAI's services for text-to-speech (TTS), speech-to-text (STT), and chat 
generation functionalities.

Modules Imported:
- TTSApi: The client class for handling text-to-speech conversion using OpenAI's services.
- STTApi: The client class for handling speech-to-text conversion.
- CHATApi: The client class for generating chat responses and other text-based outputs.

Usage:
    from openai_api import TTSApi, STTApi, CHATApi

    # Example usage:
    tts_client = TTSApi()
    stt_client = STTApi()
    chat_client = CHATApi()

Attributes:
    TTSApi (class): Manages text-to-speech operations.
    STTApi (class): Manages speech-to-text operations.
    CHATApi (class): Manages chat and text generation operations.

Note:
    This file uses future imports for compatibility with Python 2 and 3.
    Flake8 linting is disabled for this file.
"""

from __future__ import absolute_import

# import apis into sdk package
from openai_api.api.tts_api import TTSApi
from openai_api.api.stt_api import STTApi
from openai_api.api.chat_api import CHATApi

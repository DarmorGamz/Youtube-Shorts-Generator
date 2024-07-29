"""
Blah
"""
import os
import logging
from openai import OpenAI, APIError
from openai_api.openai_client import OpenAiClient

class TTSApi:
    """
    A class to interact with the OpenAI API for text-to-speech (TTS) conversion.

    Attributes:
        api_client (OpenAI): The client for interacting with OpenAI API.
        output_speech_file_path (str): The file path for storing the generated speech audio.
    """

    def __init__(self, api_client: OpenAiClient = None):
        """
        Initializes the TTSApi with an OpenAI client and sets up file paths.

        Args:
            api_client (OpenAI, optional): The client for interacting with OpenAI API.
            If None, a message will be printed, and the method returns.
        """
        if api_client is None:
            print("api_client is None")
            return
        self.api_client: OpenAI = api_client.client
        self.output_speech_file_path = os.path.join(
            api_client.configuration.temp_dir,
            "speech.mp3"
        )

    def audio_speech_create(self, text: str, voice: str = "alloy"):
        """
        Creates a speech audio file from text using the OpenAI API.

        Args:
            text (str): The input text to be converted to speech.
            voice (str, optional): The voice model to use for speech synthesis. Defaults to "alloy".

        Returns:
            None
        """
        try:
            response = self.api_client.audio.speech.create(
                model="tts-1",
                voice=voice,
                input=text
            )

            response.stream_to_file(self.output_speech_file_path)
            print(f"Speech audio saved to {self.output_speech_file_path}")

        except APIError as e:
            logging.error("API error during speech creation: %s", e)
        except (IOError, OSError) as e:
            logging.error("File handling error: %s", e)
        except Exception as e: # pylint: disable=W0718:broad-exception-caught
            logging.error("Unexpected error during speech creation: %s", e)

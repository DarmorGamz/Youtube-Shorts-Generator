"""
Blah
"""
import os
import json
import logging
from openai import OpenAI, APIError
from openai_api.openai_client import OpenAiClient

class STTApi: # pylint: disable=R0903:too-few-public-methods
    """
    A class to interact with the OpenAI API for audio transcription.

    Attributes:
        api_client (OpenAI): The client for interacting with OpenAI API.
        output_transcription_file_path (str): The file path for storing transcription data.
    """

    def __init__(self, api_client: OpenAI = None):
        """
        Initializes the STTApi with an OpenAI client and sets up file paths.

        Args:
            api_client (OpenAI, optional): The client for interacting with OpenAI API.
            If None, a message will be printed, and the method returns.
        """
        if api_client is None:
            print("api_client is None")
            return
        self.api_client = api_client.client
        self.input_speech_file_path = os.path.join(
            api_client.configuration.temp_dir,
            "speech.mp3"
        )
        self.output_transcription_file_path = os.path.join(
            api_client.configuration.temp_dir,
            "transcription.json"
        )

    def audio_transcriptions_create(self):
        """
        Creates a transcription from an audio file using the OpenAI API.

        Returns:
            None
        """
        try:
            with open(self.input_speech_file_path, "rb") as audio_file:
                transcription_response = self.api_client.audio.transcriptions.create(
                    file=audio_file,
                    model="whisper-1",
                    response_format="verbose_json",
                    timestamp_granularities=["word"]
                )

            # Extract transcription and word timing information
            transcription_data = {
                "transcription": transcription_response.text,
                "words": [],
                "duration": transcription_response.duration
            }

            for word_info in transcription_response.words:
                transcription_data["words"].append({
                    "word": word_info["word"],
                    "start": word_info["start"],
                    "end": word_info["end"]
                })

            # Save data to JSON file
            with open(self.output_transcription_file_path, "w", encoding="utf-8") as json_file:
                json.dump(transcription_data, json_file, indent=4)
            print(f"Transcription data saved to {self.output_transcription_file_path}")

        except FileNotFoundError:
            logging.error("Audio file not found: speech.mp3")
        except APIError as e:
            logging.error("API error during transcription: %s", e)
        except json.JSONDecodeError as e:
            logging.error("JSON decoding error: %s", e)
        except (IOError, OSError) as e:
            logging.error("File handling error: %s", e)
        except Exception as e: # pylint: disable=W0718:broad-exception-caught
            logging.error("Unexpected error during transcription: %s", e)

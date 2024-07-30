"""
This module provides a client class, CHATApi, for interacting with the OpenAI API 
to generate YouTube short scripts and titles. It includes functionalities to read 
and process titles, generate scripts, and save the outputs to specified file paths. 
The module uses MoviePy and OpenAI's API for these operations and handles exceptions 
to ensure robust error management.

Modules Imported:
- json: Standard library for parsing JSON data.
- os: Standard library for interacting with the operating system.
- logging: Standard library for logging error and informational messages.
- OpenAI: The main OpenAI client for interacting with the API.
- OpenAiClient: A custom client class for OpenAI interactions.
- APIError, RequestError: Custom exception classes for handling specific API-related errors.

Classes:
    CHATApi: A class to handle the generation of YouTube short 
        scripts and titles using the OpenAI API.

Usage:
    api_client = OpenAiClient()
    chat_api = CHATApi(api_client)
    chat_api.chat_completions_title_create(topic="Artificial Intelligence")
    chat_api.chat_completions_script_create()
"""
import json
import os
import logging

from openai import OpenAI
from openai_api.openai_client import OpenAiClient
from openai_api.exceptions import APIError, RequestError

class CHATApi:
    """
    A class to interact with the OpenAI API for generating YouTube short scripts and titles.

    Attributes:
        api_client (OpenAI): The client for interacting with OpenAI API.
        titles_file_path (str): The file path for storing YouTube titles.
        output_file_path (str): The file path for storing YouTube scripts.
    """

    def __init__(self, api_client: OpenAiClient = None):
        """
        Initializes the CHATApi with an OpenAI client and sets up file paths.

        Args:
            api_client (OpenAI, optional): The client for interacting with OpenAI API.
            If None, the method will print a message and return.
        """
        if api_client is None:
            print("api_client is None")
            return
        self.api_client: OpenAI = api_client.client
        self.titles_file_path = os.path.join(api_client.configuration.temp_dir,
                                            "youtube_titles.txt")
        self.output_file_path = os.path.join(api_client.configuration.temp_dir,
                                            "youtube_scripts.json")

    def read_and_remove_first_line(self, file_path):
        """
        Reads and removes the first line from a file.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The first line of the file, or None if the file is empty or not found.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            if not lines:
                logging.warning("No content in file: %s", file_path)
                return None

            first_line = lines[0].strip()
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(lines[1:])

            return first_line

        except FileNotFoundError:
            logging.error("File not found: %s", file_path)
            raise
        except IOError as e:
            logging.error("IOError while processing file %s: %s", file_path, e)
            raise
        except Exception as e:
            logging.error("Unexpected error while processing file %s: %s", file_path, e)
            raise

    def generate_script(self, title):
        """
        Generates a YouTube short script based on a given title.

        Args:
            title (str): The title for which the script is to be generated.

        Returns:
            str: The generated script.
        """
        try:
            response = self.api_client.chat.completions.create(
                model="gpt-4o-mini",
                messages = [
                    {
                        "role": "system",
                        "content": "You are a skilled scriptwriter for YouTube shorts, \
                        focusing on engaging and informative content."
                    },
                    {
                        "role": "user",
                        "content": f"Write a 20-30 second YouTube short related to '{title}'. \
                            Do not include headings like 'Hook', 'Beginning', 'Middle', 'End'- \
                            just the script. Do not quote anyone in the script. \
                            The ending should be an open-ended question."
                    }
                ]
            )
            return response.choices[0].message.content.strip()
        except APIError as e:
            logging.error("API error while generating script: %s", e)
            raise
        except RequestError as e:
            logging.error("Request error while generating script: %s", e)
            raise
        except Exception as e:
            logging.error("Unexpected error while generating script: %s", e)
            raise

    def chat_completions_script_create(self):
        """
        Reads a title from the titles file, generates a script, and saves it to a JSON file.
        """
        title = self.read_and_remove_first_line(self.titles_file_path)
        if not title:
            print("All titles have been processed.")
            return

        script = self.generate_script(title)
        if not script:
            print(f"Failed to generate a script for the title: {title}")
            return

        data = {"title": title, "script": script}

        try:
            with open(self.output_file_path, 'a', encoding='utf-8') as file:
                json.dump(data, file)
                file.write("\n")
            print(f"Processed title: {title}")
        except IOError as e:
            logging.error("IOError while writing to file %s: %s", self.output_file_path, e)
        except Exception as e: # pylint: disable=W0718:broad-exception-caught
            logging.error("Unexpected error while writing to file %s: %s", self.output_file_path, e)

    def chat_completions_title_create(self, topic=None):
        """
        Generates a list of YouTube short titles based on a given topic and saves them to a file.

        Args:
            topic (str, optional): The topic for generating titles.
            If None, logs an error and returns.
        """
        if topic is None:
            logging.error("No topic provided.")
            return

        try:
            completion = self.api_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert in SEO and content creation, \
                        specializing in generating catchy and engaging YouTube short titles that \
                        attract viewers and rank well on search engines."},
                    {"role": "user", "content": f"Provide a list of YouTube short titles \
                        focused on {topic}, with no introductory or \
                        closing remarks, and without numbering the titles."}
                ]
            )
        except APIError as e:
            logging.error("API error while generating titles: %s", e)
            raise
        except RequestError as e:
            logging.error("Request error while generating titles: %s", e)
            raise
        except json.JSONDecodeError as e:
            logging.error("JSON decoding error: %s", e)
            raise

        # Extract the generated content
        titles = completion.choices[0].message.content.strip()
        titles = titles.replace('-', '').replace('  ', ' ')

        try:
            with open(self.titles_file_path, "a", encoding='utf-8') as file:
                file.write(titles + "\n")
            print("Titles saved to youtube_titles.txt")
        except IOError as e:
            logging.error("IOError while writing to file %s: %s", self.titles_file_path, e)
        except Exception as e: # pylint: disable=W0718:broad-exception-caught
            logging.error("Unexpected error while writing to file %s: %s", self.titles_file_path, e)

"""
Blah
"""
import sys
import os
import logging
from datetime import datetime, date

from dotenv import load_dotenv
import openai_api
import video_processing

# pylint: disable=W1401:anomalous-backslash-in-string
print(
    """
 __     _________    _____ _    _  ____  _____ _______    _____ ______ _   _ 
 \ \   / /__   __|  / ____| |  | |/ __ \|  __ \__   __|  / ____|  ____| \ | |
  \ \_/ /   | |    | (___ | |__| | |  | | |__) | | |    | |  __| |__  |  \| |
   \   /    | |     \___ \|  __  | |  | |  _  /  | |    | | |_ |  __| | . ` |
    | |     | |     ____) | |  | | |__| | | \ \  | |    | |__| | |____| |\  |
    |_|     |_|    |_____/|_|  |_|\____/|_|  \_\ |_|     \_____|______|_| \_|                                                   
"""
)
# pylint: enable=W1401:anomalous-backslash-in-string

def main() -> None:
    """
    The main function to initialize API clients and perform operations
    using OpenAiClient and VideoProccessClient.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        print("api_key is None")
        return

    configuration = openai_api.Configuration(api_key=api_key)
    with openai_api.OpenAiClient(configuration) as api_client:
        try:
            print("Creating ChatAPI instance...")
            api_instance = openai_api.CHATApi(api_client)
            api_instance.chat_completions_title_create(
                topic="mental toughness and stoicism"
            )
            script = api_instance.chat_completions_script_create()

            print("Creating TTSApi instance...")
            api_instance = openai_api.TTSApi(api_client)
            api_instance.audio_speech_create(text=script)

            print("Creating STTApi instance...")
            api_instance = openai_api.STTApi(api_client)
            transcription_data, duration = api_instance.audio_transcriptions_create()
        except openai_api.APIError as e:
            logging.error("API error occurred: %s", e)
        except openai_api.RequestError as e:
            logging.error("Request error occurred: %s", e)
        except Exception as e: # pylint: disable=W0718:broad-exception-caught
            logging.error("Unexpected error occurred: %s", e)

    with video_processing.VideoProcessClient() as process_client: # pylint: disable=W0612:unused-variable
        try:
            # Add processing logic here
            process_client.create_video(duration, transcription_data["words"], "./temp/speech.mp3")
        except Exception as e: # pylint: disable=W0718:broad-exception-caught
            logging.error("Unexpected error occurred during video processing: %s", e)

def shutdown() -> None:
    """
    Shutdown the program gracefully, logging the exit and stopping the program.
    """
    print("Exiting...")
    sys.exit()

if __name__ == "__main__":
    # Get today's date and set the time to 12 AM
    today = date.today()
    midnight = datetime.combine(today, datetime.min.time())

    # Calculate epoch time for today's date at 12 AM
    epoch_time = int((midnight - datetime(1970, 1, 1)).total_seconds())

    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)

    # Set up logging configuration with the filename as today's date in epoch time
    log_filename = f'logs/{epoch_time}.log'
    logging.basicConfig(filename=log_filename, level=logging.INFO, filemode='a',
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Load environmental variables
    load_dotenv()
    try:
        logging.info('Program start.')
        main()
    except KeyboardInterrupt:
        logging.warning('Program interrupted via KeyboardInterrupt.')
        shutdown()
    except Exception as err:
        logging.error('Program interrupted via Exception: %s', err)
        raise

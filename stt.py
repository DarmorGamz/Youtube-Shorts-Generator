from openai import OpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

audio_file = open("speech.mp3", "rb")
transcription_response  = client.audio.transcriptions.create(
  file=audio_file,
  model="whisper-1",
  response_format="verbose_json",
  timestamp_granularities=["word"]
)
audio_file.close()

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
with open("transcription.json", "w") as json_file:
    json.dump(transcription_data, json_file, indent=4)

print("Transcription data saved to transcription.json")

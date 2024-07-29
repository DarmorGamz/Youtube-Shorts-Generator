from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an expert in SEO and content creation, specializing in generating catchy and engaging YouTube short titles that attract viewers and rank well on search engines."},
        {"role": "user", "content": "Provide a list of YouTube short titles focused on mental toughness and stoicism, with no introductory or closing remarks, and without numbering the titles."}
    ]
)

# Extract the generated content
titles = completion.choices[0].message.content.strip()
titles = titles.replace('-', '').replace('  ', ' ')  # Remove dashes and extra spaces

# Append the titles to a text file
with open("youtube_titles.txt", "a") as file:
    file.write(titles + "\n\n")  # Added double newline for separation between different runs

print("Titles saved to youtube_titles.txt")

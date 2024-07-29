from openai import OpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


# Function to read and remove the first line from a file
def read_and_remove_first_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    if not lines:
        return None
    first_line = lines[0].strip()
    with open(file_path, 'w') as file:
        file.writelines(lines[1:])
    return first_line

# Function to generate script based on title
def generate_script(title):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a skilled scriptwriter for YouTube shorts, focusing on engaging and informative content."},
            {"role": "user", "content": f"Write a 20-30 second youtube short related with '{title}'. Do not include headings like 'Hook', 'Beginning' 'middle' 'End' just the scripts. Do not quote anyone in the script. the ending should be an open ended question."}
        ]
    )
    return response.choices[0].message.content.strip()



# File paths
titles_file_path = "youtube_titles.txt"
output_file_path = "youtube_scripts.json"

# Process each title
while True:
    title = read_and_remove_first_line(titles_file_path)
    if not title:
        break  # No more titles to process
    
    script = generate_script(title)
    data = {"title": title, "script": script}

    # Append the result to the JSON file
    with open(output_file_path, 'a') as file:
        json.dump(data, file)
        file.write("\n")  # Write each entry on a new line

    print(f"Processed title: {title}")

print("All titles have been processed.")
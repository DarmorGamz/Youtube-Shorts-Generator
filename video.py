from moviepy.editor import TextClip, CompositeVideoClip, ColorClip, AudioFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

# Define the duration of the video
duration = 3.5

# Create a background for the video (a plain color image)
background = ColorClip(size=(1080, 1920), color=(255, 255, 255), duration=duration)

# Define the subtitles with the given words and timestamps
subtitles_data = [
    ('Today', 0.0, 0.36),
    ('is', 0.36, 0.58),
    ('a', 0.58, 0.78),
    ('wonderful', 0.78, 1.16),
    ('day', 1.16, 1.52),
    ('to', 1.52, 1.88),
    ('build', 1.88, 2.06),
    ('something', 2.06, 2.5),
    ('people', 2.5, 2.88),
    ('love', 2.88, 3.22)
]

# Function to generate subtitle clips
def make_text_clip(txt, start, end):
    return (TextClip(txt, fontsize=48, color='black', font='Arial-Bold')
            .set_position(('center', 1600))  # Adjust position if necessary
            .set_start(start)
            .set_end(end))

# Create a composite video with subtitles
subtitles = [make_text_clip(word, start, end) for word, start, end in subtitles_data]
video = CompositeVideoClip([background] + subtitles)

# Load the audio file
audio = AudioFileClip("speech.mp3")

# Set the audio to the video
video = video.set_audio(audio)

# Export the video
video.write_videofile('video_with_subtitles_and_audio.mp4', codec='libx264', fps=24)
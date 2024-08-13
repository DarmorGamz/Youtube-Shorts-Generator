"""
This module provides functionalities for video processing using the MoviePy library. 
It imports essential components for handling text overlays, video compositions, 
color clips, audio files, and subtitles. Additionally, it configures the ImageMagick 
binary path, which is required for certain MoviePy operations.

Modules Imported:
- TextClip, CompositeVideoClip, ColorClip, AudioFileClip: 
    Core components from MoviePy for video and audio editing.
- SubtitlesClip: Tool from MoviePy for handling subtitles.
- change_settings: Utility from MoviePy's configuration module to set the path for ImageMagick.

Classes:
    VideoProcessClient: A client class to manage video processing operations, 
                        providing context management and resource handling capabilities.

Usage:
    with VideoProcessClient() as client:
        # Perform video processing tasks

Configuration:
    The module sets the path for the ImageMagick binary, which is necessary for 
    rendering text and other image-based elements in videos.
"""
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip, AudioFileClip # pylint: disable=W0611:unused-import
from moviepy.video.tools.subtitles import SubtitlesClip# pylint: disable=W0611:unused-import
from moviepy.config import change_settings
import os
change_settings({"IMAGEMAGICK_BINARY":
                r"E:\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

# Function to generate subtitle clips
def make_text_clip(txt, start, end):
    return (TextClip(txt, fontsize=100, color='black', font='Arial-Bold')
            .set_position(('center', 'center'))  # Adjust position if necessary
            .set_start(start)
            .set_end(end))

class VideoProcessClient(object): # pylint: disable=R0205:useless-object-inheritance
    """
    VideoProcessClient is a context manager class that facilitates video processing tasks.
    It handles the setup and teardown of resources, ensuring proper management of video 
    editing processes.

    Methods:
        __init__(): Initializes the client object.
        __enter__(): Enters the runtime context and returns the client instance.
        __exit__(exc_type, exc_value, traceback): Exits the runtime context, handling 
                                                  any exceptions and cleaning up resources.
        close(): Closes any resources or connections opened by the client.
    """
    def __init__(self):
        """Initializes the VideoProcessClient instance."""

    def __enter__(self):
        """Enters the runtime context and returns the client instance."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exits the runtime context. If an exception occurred, it is passed to this method.
        This method ensures that resources are properly closed.

        Args:
            exc_type (type): The exception type.
            exc_value (Exception): The exception instance.
            traceback (traceback): The traceback object.
        """
        self.close()

    def close(self):
        """Closes any resources or connections opened by the client."""

    def create_video(self, duration, subtitles_data, audio_file):
        # Create a background for the video (a plain color image)
        background = ColorClip(size=(1080, 1920), color=(255, 255, 255), duration=duration)

        # Create a composite video with subtitles
        # subtitles = [make_text_clip(word, start, end) for word, start, end in subtitles_data]
        subtitles = [make_text_clip(item["word"], item["start"], item["end"]) for item in subtitles_data]
        video = CompositeVideoClip([background] + subtitles)

        # Load the audio file
        audio = AudioFileClip(audio_file)

        # Set the audio to the video
        video = video.set_audio(audio)

        # Export the video
        num_threads = os.cpu_count()
        video.write_videofile('./temp/video.mp4',
                              codec='h264_nvenc',
                              fps=24,
                              threads=num_threads)

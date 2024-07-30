# coding: utf-8
"""
This module serves as the package initializer for the video processing package. 
It imports and provides access to the VideoProcessClient class, which is 
responsible for handling various video processing tasks such as editing, 
transcoding, and applying effects.

Modules Imported:
- VideoProcessClient: The main client class for video processing operations.

Usage:
    from video_processing import VideoProcessClient

    # Example usage:
    client = VideoProcessClient()
    client.process_video('input_file.mp4', 'output_file.mp4')

Attributes:
    VideoProcessClient (class): A class to manage video processing tasks.

Note:
    This file uses future imports for compatibility with Python 2 and 3.
    Flake8 linting is disabled for this file.
"""

from __future__ import absolute_import

# import VideoProccessClient
from video_processing.process_client import VideoProcessClient

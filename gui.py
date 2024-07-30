# coding: utf-8
"""
This module initializes a Flask web application for managing and rendering templates 
for an interactive GUI. It includes routes for the main index page and settings page, 
and sets headers to disable caching for all responses. The application can be launched 
locally, opening the default web browser to the specified port.

Modules Imported:
- webbrowser: Standard library for opening URLs in a web browser.
- Path: Pathlib module for filesystem path operations.
- tomlkit: TOML parser and writer for handling configuration files.
- Flask, render_template, request: Flask web framework for creating web applications.

Routes:
- /: Renders the main index page.
- /settings: Renders the settings page.

Usage:
    Run this module directly to start the Flask web application on the specified port.
"""

import webbrowser
from flask import Flask, render_template

app = Flask(__name__, template_folder="gui")

@app.after_request
def after_request(response):
    """
    Modifies response headers to prevent caching.

    Args:
        response (Response): The Flask response object.

    Returns:
        Response: The modified response object with no-cache headers.
    """
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    """
    Renders the main index page.

    Returns:
        str: The rendered HTML of the index page.
    """
    return render_template("index.html")

@app.route("/settings", methods=["GET", "POST"])
def settings():
    """
    Renders the settings page.

    Returns:
        str: The rendered HTML of the settings page.
    """
    return render_template("settings.html")

PORT = 4000

if __name__ == "__main__":
    webbrowser.open(f"http://localhost:{PORT}", new=2)
    app.run(port=PORT)

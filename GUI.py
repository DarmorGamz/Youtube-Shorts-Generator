import webbrowser
from pathlib import Path
import tomlkit
# import utils.gui_utils as gui
from flask import (
    Flask,
    render_template,
    request,
)



app = Flask(__name__, template_folder="GUI")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/settings", methods=["GET", "POST"])
def settings():
    return render_template("settings.html")

PORT = 4000
if __name__ == "__main__":
    webbrowser.open(f"http://localhost:{PORT}", new=2)
    app.run(port=PORT)

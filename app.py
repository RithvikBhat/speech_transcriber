from flask import Flask, render_template, request, redirect
from werkzeug.utils import redirect
import speech_recognition as sr


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if(request.method == "POST"):
        print("Form Data Received")

        # If file does not exist
        if "file" not in request.files:
            return redirect(request.url)

        # For empty file
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        # Speech recognition using audio file
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)

    return render_template('index.html', transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

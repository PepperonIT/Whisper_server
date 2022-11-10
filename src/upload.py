"""
Upload module
Essentially the main file, holding the server and api functionality
"""

import os
from flask import *# pylint: disable=wildcard-import, unused-wildcard-import
from werkzeug.utils import secure_filename# pylint: disable=unused-import
import whisper
import jsonify
from pydub import AudioSegment
import config

APP = Flask(__name__)
APP.config['UPLOAD_FOLDER'] = "../files"
APP.config['JSON_AS_ASCII'] = False

MODEL = whisper.load_model("small")

@APP.route('/')
def upload():
    """http"""
    return render_template("file_upload.html")

@APP.route('/success', methods=['POST'])
def success():# pylint: disable=inconsistent-return-statements
    """handling different audio files"""
    if request.method == 'POST':
        file = request.files['file']
        path = os.path.join(APP.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        if path[:-3] == 'wav':
            AudioSegment.from_wav(path).export(path[:-3]+"mp3", format="mp3")
            result = MODEL.transcribe(path[:-3]+"mp3", **{"language": "sv"})
        else:
            result = MODEL.transcribe(path, **{"language": "sv"})

        return render_template("success.html", data=result['text'])

@APP.route('/recieve', methods=['POST'])
def recieve():# pylint: disable=inconsistent-return-statements
    """recieves audiofile and transcribes"""
    if request.method == 'POST':
        file = request.files['file']
        path = os.path.join(APP.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        if path[:-3] == 'wav':
            AudioSegment.from_wav(path).export(path[:-3]+"mp3", format="mp3")
            result = MODEL.transcribe(path[:-3]+"mp3")
        else:
            result = MODEL.transcribe(path)

        return json.dumps({"data": result['text']})

if __name__ == '__main__':
    APP.run(config.IP_ADDRESS, debug=True)

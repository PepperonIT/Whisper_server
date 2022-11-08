from flask import *  
from werkzeug.utils import secure_filename
import os
import whisper
import jsonify
from pydub import AudioSegment
import config

app = Flask(__name__)  
app.config['UPLOAD_FOLDER'] = "files"
app.config['JSON_AS_ASCII'] = False

model = whisper.load_model("small")

@app.route('/')  
def upload():  
    return render_template("file_upload.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        f.save(path)
        if path[:-3] == 'wav':
            AudioSegment.from_wav(path).export(path[:-3]+"mp3", format="mp3")
            result = model.transcribe(path[:-3]+"mp3", **{"language": "sv"})
        else:
            result = model.transcribe(path, **{"language": "sv"})

        return render_template("success.html", data = result['text'])  
  
@app.route('/recieve', methods = ['POST'])  
def recieve():  
    if request.method == 'POST':  
        f = request.files['file']  
        path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        f.save(path)
        if path[:-3] == 'wav':
            AudioSegment.from_wav(path).export(path[:-3]+"mp3", format="mp3")
            result = model.transcribe(path[:-3]+"mp3")
        else:
            result = model.transcribe(path)


        return json.dumps({"data": result['text']}) 

if __name__ == '__main__':  
    app.run(IP_ADDRESS, debug = True)  


# \<Web_Interaction>
Provides a server using OpenAI's Whisper to do transcribing on audio files, as well as a basic API supporting it
    *- success*
    *- recieve*

*success:* success 
*recieve:* recieves audiofile and outputs a transcribed json file

# tools / installation

The tools revolves around getting a basic server up with enabled API calls in order to transcribe an audiofile. Simplicity has been highly prioritized as we currently are not concerned with safety as the audio file and transcribed text do not contain any sensitive information. Also our focus is on implementing Pepper functionality so the server is just needed as there is no plausable way Pepper can do the transcribing within a decent time frame, so even with the RTT time this solution is significantly faster

## server/whisper
> [whisper](tools.md)
OpenAI's whisper is being used for transcribing.
https://pypi.org/project/whisper/

## Tools

> [Flask](tools.md)
WSGI web application framework wrapped around Werkzeug. Chosen for a quick and easy start
https://pypi.org/project/Flask/

> [Werkzeug](tools.md)
WSGI interface for debugging and information
https://pypi.org/project/Werkzeug/

> [jsonify](tools.md)
Allows us to convert the transcription text into JSON
https://pypi.org/project/jsonify/

> [pydub](tools.md)
Easy manipulation of audio files
https://pypi.org/project/pydub/

# Usage
The entire functionality is run the server waiting for API calls from Pepper
```bash
python upload.py
```
and then return a text file.
## Examples
Currently same as above, under "Usage".

# License
MIT License

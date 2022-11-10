"""
Test module
For quickly trying different whisper modules, languages etc.
"""

import whisper
MODEL = whisper.load_model("small")
RESULT = MODEL.transcribe("files/audio.mp3", **{"language": "sv"})
print(RESULT['text'])# pylint: disable=superfluous-parens

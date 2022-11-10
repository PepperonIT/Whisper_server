import whisper

model = whisper.load_model("small")

result = model.transcribe("files/audio.mp3", **{"language": "sv"})

print(result['text'])

import faster_whisper

faster_whisper.download_model("medium")

faster_whisper.WhisperModel("medium", device="cpu", compute_type="int8")

segments, info = model.transcribe("temp/larry-foulke-last-interview.mkv", beam_size=5)

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

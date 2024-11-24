from faster_whisper import WhisperModel
import PySide6

def select_file_dialog(file_path):
    return file_path

def transcribe(self, model_size, device, file_path, language):
    model_size = self.box_models.currentText()
    model = WhisperModel(model_size, device=device, compute_type="int8")
    segments, info = model.transcribe(file_path, language, beam_size=5)
    for segment in segments:
        temp = "[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text)
        return temp
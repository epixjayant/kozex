from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

def generate_speech(text, file_path):
    tts.tts_to_file(
        text=text,
        file_path=file_path,
        speaker_wav=["sample.wav"],
        language="en",
        split_sentences=True
    )
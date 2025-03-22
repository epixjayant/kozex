from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

# generate speech by cloning a voice using default settings
tts.tts_to_file(
    text="this is the dumy text, you have to replace it to a auto store variable",
    file_path="output_samp.wav",
    speaker_wav=["sample.wav"],
    language="en",
    split_sentences=True
)
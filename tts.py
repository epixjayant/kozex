from gtts import gTTS
import os

def text_to_speech(text, output_file="output.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    os.system(f"open {output_file}")  # Play the audio file

text_to_speech("Hello, welcome to the Prodigal AI Voice Cloning Hackathon!")

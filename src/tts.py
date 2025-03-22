from flask import Flask, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

def text_to_speech(text, output_file="output.mp3", play_audio=False, save_audio=True):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    
    if play_audio:
        os.system(f"open {output_file}")  # Play the audio file
    
    if save_audio:
        saved_audio_dir = "saved_audio"
        os.makedirs(saved_audio_dir, exist_ok=True)
        saved_path = os.path.join(saved_audio_dir, output_file)
        os.rename(output_file, saved_path)
        print(f"Audio file saved to {saved_path}")
        return saved_path

@app.route('/convert-text', methods=['POST'])
def convert_text():
    data = request.json
    text = data.get('text', 'Default text if none provided')
    output_path = text_to_speech(text)
    return jsonify({"message": "Audio generated successfully", "file_path": output_path})

if __name__ == '__main__':
    app.run(debug=True)

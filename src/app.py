from flask import Flask, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename
from TTS.api import TTS  # Coqui TTS library
import soundfile as sf

app = Flask(__name__)

# Define base directory and folders for uploaded and generated audio files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, '../static/uploaded_audios')
GENERATED_FOLDER = os.path.join(BASE_DIR, '../static/generated_audios')

# Ensure the folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GENERATED_FOLDER, exist_ok=True)

# Configure Flask app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['GENERATED_FOLDER'] = GENERATED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16MB

# Initialize TTS model
tts_model = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

# Allowed audio file extensions
ALLOWED_EXTENSIONS = {'wav', 'mp3'}

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle audio file uploads."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({'message': 'File uploaded successfully', 'filepath': filepath}), 200
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/tts', methods=['POST'])
def text_to_speech():
    """Generate speech from text input."""
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Text input is required'}), 400
    text = data['text']
    output_path = os.path.join(app.config['GENERATED_FOLDER'], 'tts_output.wav')
    try:
        tts_model.tts_to_file(text=text, file_path=output_path)
        return jsonify({'message': 'TTS generated successfully', 'audio_path': output_path}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/clone', methods=['POST'])
def voice_cloning():
    """Generate speech in a cloned voice."""
    if 'reference_audio' not in request.files or 'text' not in request.form:
        return jsonify({'error': 'Reference audio and text input are required'}), 400
    file = request.files['reference_audio']
    text = request.form['text']
    if file and allowed_file(file.filename):
        reference_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(reference_path)
        output_path = os.path.join(app.config['GENERATED_FOLDER'], 'cloned_output.wav')
        try:
            tts_model.tts_to_file(text=text, speaker_wav=reference_path, file_path=output_path)
            return jsonify({'message': 'Voice cloning successful', 'audio_path': output_path}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/audio/<filename>', methods=['GET'])
def serve_audio(filename):
    """Serve generated audio files."""
    try:
        return send_from_directory(app.config['GENERATED_FOLDER'], filename, as_attachment=True)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file size limit errors."""
    return jsonify({'error': 'File is too large'}), 413

if __name__ == '__main__':
    app.run(debug=True)

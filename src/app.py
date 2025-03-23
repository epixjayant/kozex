from flask import Flask, request, send_file, render_template
import os
from xtts import generate_speech  # Fix the import statement

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', download=False)

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    generate_speech(text)
    return render_template('index.html', download=True)

@app.route('/download')
def download():
    return send_file("static/output_samp.wav", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
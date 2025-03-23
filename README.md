# Kozex AI Voice Cloning Project

Welcome to the **Kozex AI Voice Cloning Project**! This is a prototype application for voice cloning and text-to-speech (TTS). Users can:

- Convert text to speech using a high-quality generic voice.
- Clone their voice and generate speech in their voice.
- Record or upload audio and receive the output in a different voice.

---

## 📌 Table of Contents

1. [Features](#features)
2. [Folder Structure](#folder-structure)
3. [Setup Instructions](#setup-instructions)
4. [Running the Application](#running-the-application)
5. [Usage](#usage)
6. [Testing](#testing)
7. [Dependencies](#dependencies)
8. [Contributing](#contributing)
9. [License](#license)

---

## 🚀 Features

### 🔹 Core Functionality

- **Text-to-Speech (TTS):**
  - Converts text into speech using high-quality models like Tacotron, FastSpeech, etc.
  - Supports multiple pre-trained TTS models.
- **Voice Cloning:**
  - Clones a user’s voice from a short audio sample.
  - Generates speech in the cloned voice.
- **User-Friendly Interface:**
  - Record audio via a microphone.
  - Upload audio or text files.
  - Listen to or download generated audio.

---

## 📂 Folder Structure

```
ProdigalAI_Hackathon/
├── README.md            # Project documentation
├── requirements.txt      # Python dependencies
├── src/                 # Source code
│   ├── frontend/        # Frontend (HTML, CSS, JS)
│   ├── backend/         # Backend (Python, Flask)
│   ├── tests/           # Unit tests
├── samples/             # Sample audio files for testing
├── models/              # Pre-trained AI/ML models
└── static/              # Static files (uploaded/generated audio)
```

---

## ⚙️ Setup Instructions

### Prerequisites

- **Python**: Version 3.6 to 3.8 (Recommended: 3.8). [(Install Python 3.8 for Mac)](#install-python38-for-mac)
- **Git** (optional, for version control).

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/epixjayant/kozex.git
   cd kozex
   ```
2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv_name
   ```
   - Activate it:
     - **Mac/Linux:** `source venv_name/bin/activate`
     - **Windows:** `venv_name\Scripts\activate`
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application**:
   ```bash
   python src/app.py
   ```

---

## ▶️ Running the Application

### 🔹 Backend (Flask Server)

1. Navigate to the backend folder:
   ```bash
   cd src/backend
   ```
2. Run the Flask server:
   ```bash
   python app.py
   ```
   - The server starts at `http://127.0.0.1:5000`.

### 🔹 Frontend

1. Open `src/frontend/index.html` in your browser.
2. Use the UI to:
   - Record audio.
   - Upload audio or text files.
   - Generate and download output audio.

---

## 📖 Usage

### 🔹 Text-to-Speech (TTS)

1. Enter text in the input box or upload a text file.
2. Click **Generate Speech**.
3. The system will generate speech using a generic voice and provide a download link.

### 🔹 Voice Cloning

1. Record or upload an audio file of the target voice.
2. Enter text to be spoken in the cloned voice.
3. Click **Clone Voice**.
4. The system will generate speech in the cloned voice and provide a download link.

---

## 🧪 Testing

### 🔹 Running Unit Tests

1. Navigate to the `tests` folder:
   ```bash
   cd src/tests
   ```
2. Run the tests:
   ```bash
   python -m unittest test_audio_processing.py
   python -m unittest test_tts.py
   python -m unittest test_voice_cloning.py
   ```

---

## 🖥 Install Python 3.8 for Mac

Run the following command to install Python 3.8 on Mac:
```bash
brew install python@3.8
```

---

## 📦 Dependencies

### 🔹 Backend (Python Libraries)

- **Flask** – Web framework for the backend.
- **Coqui TTS** – Text-to-speech and voice cloning.
- **NumPy** – Numerical operations.
- **SoundFile** – Handling audio files.

### 🔹 Frontend (Web Technologies)

- **HTML, CSS, JavaScript** – User interface.
- **Web Audio API** – For recording audio.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Make your changes and commit them.
4. Push the branch and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

### 💡 Happy Coding! 🎙️✨


# Kozex AI Voice Cloning Project

Welcome to the **Kozex AI Voice Cloning Project**! This project is a working prototype of a voice cloning and text-to-speech (TTS) application. It allows users to:

- Convert text to speech using a generic voice.
- Clone a user's voice and generate speech in their voice.
- Record or upload audio, and receive the output in a different voice.

---

## Table of Contents

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

## Features

### Core Functionality

- **Text-to-Speech (TTS)**:
  - Convert any text into speech using a high-quality, generic voice.
  - Supports multiple pre-trained TTS models (e.g., Tacotron, FastSpeech).
- **Voice Cloning**:
  - Clone a user's voice from a short audio sample.
  - Generate speech in the cloned voice.
- **User Interface**:
  - Record audio directly via a microphone.
  - Upload audio files or text files.
  - Listen to or download the generated audio.

---

## Folder Structure

#### ProdigalAI_Hackathon/

├── README.md # Project overview and instructions  
├── requirements.txt # Project dependencies  
├── requirements.txt # Python dependencies  
├── src/ # Source code  
│ ├── frontend/ # Frontend code (HTML, CSS, JS)  
│ ├── backend/ # Backend code (Python, Flask)  
│ └── tests/ # Unit tests  
├── samples/ # Sample audio files for testing  
├── models/ # Pre-trained AI/ML models  
└── static/ # Static files (uploaded/generated audio)

---

## Setup Instructions

### Prerequisites

- Ensure Python version should greater than 3.6 but less than 3.9 installed. _( [install python 3.8 for mac](#install-python38-for-mac) )_.
- Git (optional, for version control).

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ProdigalAI_Hackathon.git
   cd ProdigalAI_Hackathon
   ```
2. **Install Dependencies**:

- create a vertual environment using `python -m venv venv_name`  
  Activate it using:  
  for mac`source venv_name/bin/activate`  
  for windows`venv_name\Scripts\activate`

  bash
  ` pip install -r requirements.txt`

3. **Run the Application**:  
   `python3 src/app.py`

# Running the Application

## Backend (Flask Server)

1. Navigate to the `src/backend/` folder:

| **bash**         | **Copy** |
| ---------------- | -------- |
| `cd src/backend` |          |

2. Run the Flask server:

| **bash**        | **Copy** |
| --------------- | -------- |
| `python app.py` |          |

- The server will start at `http://127.0.0.1:5000`.

## Frontend

1. Open the `src/frontend/index.html` file in your browser.

2. Use the UI to:
   - Record audio.
   - Upload audio or text files.
   - Generate and download output audio.

---

# Usage

## Text-to-Speech (TTS)

1. Enter text in the input box or upload a text file.

2. Click **Generate Speech**.

3. The system will generate speech using a generic voice and provide a download link.

## Voice Cloning

1. Record or upload an audio file of the target voice.

2. Enter text to be spoken in the cloned voice.

3. Click **Clone Voice**.

4. The system will generate speech in the cloned voice and provide a download link.

---

# Testing

## Unit Tests

1. Navigate to the `src/tests/` folder:

| **bash**       | **Copy** |
| -------------- | -------- |
| `cd src/tests` |          |

2. Run the tests:

| **bash**                                      | **Copy** |
| --------------------------------------------- | -------- |
| `python -m unittest test_audio_processing.py` |          |
| `python -m unittest test_tts.py`              |          |
| `python -m unittest test_voice_cloning.py`    |          |

---

## Install python3.8 for mac

---

# Dependencies

## Python Libraries

- Flask (for backend server).
- Coqui TTS (for text-to-speech and voice cloning).
- NumPy (for numerical operations).
- SoundFile (for audio file handling).

## Frontend Libraries

- HTML, CSS, JavaScript (for the user interface).
- Web Audio API (for recording audio).

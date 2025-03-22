# Import necessary libraries
import os
import wave
import pydub  # pydub is an open-source library for audio manipulation

# Function to convert MP3 to WAV format
def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    """
    Converts an MP3 file to WAV format using the pydub library.

    Parameters:
    - mp3_file_path (str): The path to the input MP3 file.
    - wav_file_path (str): The path where the output WAV file will be saved.

    Returns:
    - None
    """
    try:
        # Load the MP3 file using pydub
        audio = pydub.AudioSegment.from_mp3(mp3_file_path)

        # Export the audio to WAV format
        audio.export(wav_file_path, format="wav")

        print(f"Conversion successful: {wav_file_path}")

    except Exception as e:
        # Handle any exceptions that occur during the conversion process
        print(f"An error occurred during conversion: {e}")

# Function to validate file paths
def validate_file_path(file_path, extension):
    """
    Validates if the file path exists and has the correct extension.

    Parameters:
    - file_path (str): The path to the file.
    - extension (str): The expected file extension (e.g., '.mp3', '.wav').

    Returns:
    - bool: True if the file path is valid, False otherwise.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False

    if not file_path.lower().endswith(extension):
        print(f"Invalid file extension. Expected {extension} file.")
        return False

    return True

# Main function to handle the conversion process
def main():
    # Define the input MP3 file path and output WAV file path
    mp3_file_path = "input.mp3"  # Replace with your MP3 file path
    wav_file_path = "output.wav"  # Replace with your desired WAV file path

    # Validate the input MP3 file path
    if not validate_file_path(mp3_file_path, ".mp3"):
        return

    # Perform the conversion
    convert_mp3_to_wav(mp3_file_path, wav_file_path)

# Entry point of the script
if __name__ == "__main__":
    main()
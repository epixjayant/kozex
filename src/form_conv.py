from pydub import AudioSegment
import os

def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    """
    Convert an MP3 file to WAV format.

    :param mp3_file_path: Path to the input MP3 file.
    :param wav_file_path: Path to save the output WAV file.
    """
    try:
        # Check if the input file has a valid MP3 extension
        if not mp3_file_path.lower().endswith(".mp3"):
            raise ValueError("Input file must have a .mp3 extension.")

        # Load the MP3 file
        print(f"Loading MP3 file: {mp3_file_path}")
        audio = AudioSegment.from_mp3(mp3_file_path)

        # Ensure the output directory exists
        output_dir = os.path.dirname(wav_file_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Export the audio as WAV
        print(f"Exporting WAV file: {wav_file_path}")
        audio.export(wav_file_path, format="wav")
        print(f"Successfully converted {mp3_file_path} to {wav_file_path}")
    except Exception as e:
        print(f"Error converting MP3 to WAV: {e}")

# Example usage
if __name__ == "_main_":
    # Input MP3 file path
    mp3_file_path = input("Enter the path to the MP3 file: ").strip()

    # Output WAV file path
    wav_file_path = input("Enter the path to save the WAV file: ").strip()

    # Check if the MP3 file exists
    if not os.path.exists(mp3_file_path):
        print(f"Error: The file {mp3_file_path} does not exist.")
    else:
        # Convert MP3 to WAV
        convert_mp3_to_wav(mp3_file_path, wav_file_path)
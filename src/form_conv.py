from pydub import AudioSegment
import os

def convert_mp3_to_wav(mp3_file):
    if not os.path.exists(mp3_file):
        raise FileNotFoundError(f"The file {mp3_file} does not exist.")
    
    # Extract the file name without extension
    file_name = os.path.splitext(os.path.basename(mp3_file))[0]
    wav_file = f"{file_name}.wav"
    
    # Convert MP3 to WAV
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format="wav")
    
    print(f"Converted {mp3_file} to {wav_file}")
    return wav_file

# Example usage
# wav_file = convert_mp3_to_wav("example.mp3")
# print(f"Returned WAV file: {wav_file}")

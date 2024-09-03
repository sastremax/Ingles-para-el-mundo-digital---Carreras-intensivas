import speech_recognition as sr
from pydub import AudioSegment

# Asegúrate de que pydub use ffmpeg y flac correctamente
ffmpeg_path = "/b/miniconda/envs/audio_analysis/Library/bin/ffmpeg"  # Asegúrate de que esta ruta sea correcta
flac_path = "/b/miniconda/envs/audio_analysis/Library/bin/flac"

AudioSegment.converter = ffmpeg_path
AudioSegment.ffmpeg = ffmpeg_path
AudioSegment.ffprobe = ffmpeg_path

# Path to the converted audio file
audio_file_path = "B:/curso-coder/english 1/clase 9/audio.wav"

# Convert the audio file to FLAC
audio = AudioSegment.from_wav(audio_file_path)
flac_audio_path = "B:/curso-coder/english 1/clase 9/converted_audio.flac"
audio.export(flac_audio_path, format="flac")

# Verify the FLAC file
try:
    with open(flac_audio_path, "rb") as f:
        f.read(10)  # Try reading the first few bytes
    print("FLAC file created successfully.")
except Exception as e:
    print(f"Error verifying FLAC file: {e}")

# Initialize recognizer class
recognizer = sr.Recognizer()

# Load the FLAC audio file
try:
    with sr.AudioFile(flac_audio_path) as source:
        audio_data = recognizer.record(source)

    # Recognize the speech in the audio
    try:
        text = recognizer.recognize_google(audio_data)
        print("Transcription: ", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Sorry, the service is unavailable at the moment.")
except Exception as e:
    print(f"Error loading FLAC file: {e}")
import os
import whisper

# Add FFmpeg path explicitly
os.environ["PATH"] += os.pathsep + r"C:\Users\iidan\Downloads\ffmpeg-7.1-full_build\ffmpeg-7.1-full_build\bin"

# Load Whisper model
print("Loading Whisper model...")
model = whisper.load_model("large")  # Use "small", "medium", or "large" for better accuracy
print("Whisper model loaded successfully.")

def transcribe_audio(audio_file):
    """
    Transcribe the given audio file using Whisper.
    :param audio_file: Path to the audio file to transcribe.
    :return: Transcription result as a string, or an error message in case of failure.
    """
    try:
        print(f"Starting transcription for: {audio_file}")
        
        # Check if the file exists
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"File not found: {audio_file}")
        
        # Perform transcription
        result = model.transcribe(audio_file, language="ar")  # Set language to Arabic
        transcription = result["text"].strip()  # Clean the output
        print(f"Transcription complete: {transcription}")
        return {"transcription": transcription}

    except Exception as e:
        print(f"Error during transcription: {e}")
        return {"error": str(e)}
from flask import Flask, request, jsonify, render_template
import os
import uuid
from flask_cors import CORS
import librosa
from pydub import AudioSegment
import s
from emotion_recognition import predict_emotion
import whisper

app = Flask(__name__)

# Configurations
app.config['UPLOAD_FOLDER'] = './Temp'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16MB
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # Ensure the Temp folder exists
CORS(app)

# Load Whisper model for speech-to-text
print("Loading Whisper model...")
model = whisper.load_model("large")  # You can choose "small", "medium", or "large"
print("Whisper model loaded successfully.")


def convert_audio_to_wav(file_path):
    """
    Converts any audio file to .wav format using pydub.
    """
    try:
        audio = AudioSegment.from_file(file_path)  # Load the input file as audio
        wav_path = file_path.rsplit('.', 1)[0] + '.wav'  # Change extension to .wav
        audio.export(wav_path, format="wav")  # Export audio as .wav file
        print(f"Audio converted to wav: {wav_path}")
        return wav_path
    except Exception as e:
        print(f"Error converting audio to wav: {e}")
        return None


def validate_audio(file_path):
    """
    Validates the audio file using ffmpeg to ensure it's a valid audio format.
    """
    try:
        result = subprocess.run(['ffmpeg', '-v', 'error', '-i', file_path, '-f', 'null', '-'], stderr=subprocess.PIPE)
        if result.returncode != 0:
            print(f"Invalid audio file: {file_path}")
            return False
        return True
    except Exception as e:
        print(f"Validation error: {e}")
        return False


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
        return transcription

    except Exception as e:
        print(f"Error during transcription: {e}")
        return None


@app.route('/')
def home():
    return "Welcome to the Emotion Recognition API"


@app.route('/process-audio', methods=['POST'])
def process_audio():
    try:
        # Check if 'audio' key exists in the request
        if 'audio' not in request.files:
            print("No audio file in the request!")
            return jsonify({"error": "No audio file provided"}), 400

        # Extract the file from the request
        audio_file = request.files['audio']
        print(f"Received file: {audio_file.filename}")
        
        # Validate filename
        if audio_file.filename == '':
            print("Empty filename!")
            return jsonify({"error": "No selected file"}), 400

        # Save the audio file to the Temp folder
        original_file_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
        audio_file.save(original_file_path)
        print(f"File saved to: {os.path.abspath(original_file_path)}")

        # Convert the audio file to .wav format if necessary
        converted_file_path = convert_audio_to_wav(original_file_path)
        if not converted_file_path:
            return jsonify({"error": "Failed to convert audio file to WAV format"}), 500

        # Validate the audio file using ffmpeg
        if not validate_audio(converted_file_path):
            print(f"Invalid audio file detected: {converted_file_path}")
            return jsonify({"error": "Invalid audio format"}), 400

        # Perform speech-to-text transcription
        transcription = transcribe_audio(converted_file_path)
        if not transcription:
            return jsonify({"error": "Failed to transcribe audio"}), 500

        # Perform emotion recognition
        try:
            result = predict_emotion(converted_file_path)
            print(f"Prediction result: {result}")
        except Exception as e:
            print(f"Error during emotion recognition: {e}")
            return jsonify({"error": f"Prediction failed: {e}"}), 500

        # Check if the model returned an error
        if "error" in result and result["error"]:
            return jsonify({"error": result["error"]}), 500

        # Prepare the output data
        output = {
            "transcription": transcription,
            "emotion": result.get("emotion", "Unknown")
        }

        # Check if the request accepts HTML
        if "text/html" in request.headers.get("Accept", ""):
            # Render the results as an HTML page
            return render_template("result.html", transcription=output["transcription"], emotion=output["emotion"])
        
        # Otherwise, return a JSON response
        return jsonify(output), 200

    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({"error": str(e)}), 500

    finally:
        # Delete the temporary files if they exist
        if 'original_file_path' in locals() and os.path.exists(original_file_path):
            os.remove(original_file_path)
            print(f"Temporary file {original_file_path} deleted.")
        if 'converted_file_path' in locals() and os.path.exists(converted_file_path):
            os.remove(converted_file_path)
            print(f"Converted file {converted_file_path} deleted.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

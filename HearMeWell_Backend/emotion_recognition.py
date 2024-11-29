import tensorflow as tf
import librosa
import numpy as np
import librosa.display
import matplotlib.pyplot as pl

model_path='./models/HMW_EfficientNetB0Classification_model.keras'
print(f"Loading emotion recognition model from: {model_path}")
model = tf.keras.models.load_model(model_path)
print("Model loaded successfully.")

def predict_emotion(audio_file):
    try:
        # Add debug logs for input file path
        print(f"Processing file: {audio_file}")
        # Load the audio file
        y, sr = librosa.load(audio_file, sr=22050)

        # Generate Mel-Spectrogram
        mel_spec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
        mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

        # Debug original spectrogram shape
        print(f"Shape of Mel-Spectrogram (original): {mel_spec_db.shape}")


        # Resize to 224x224 and add channel dimension for the EfficientNetB0
        mel_spec_resized = tf.image.resize(mel_spec_db[..., np.newaxis], [224, 224])  # Add channel dimension
        print(f"Shape of Resized Mel-Spectrogram: {mel_spec_resized.shape}")

        # Convert grayscale to RGB
        mel_spec_rgb = np.concatenate([mel_spec_resized, mel_spec_resized, mel_spec_resized], axis=-1)
        print(f"Shape of RGB Mel-Spectrogram: {mel_spec_rgb.shape}")

        # Add batch dimension
        mel_spec_rgb = np.expand_dims(mel_spec_rgb, axis=0)  # Add batch dimension
        print(f"Shape of Final Input to Model: {mel_spec_rgb.shape}")
        # Predict emotion
        prediction = model.predict(mel_spec_rgb)
        emotion_index = np.argmax(prediction)
        emotions = ["happy", "angry", "sad", "calm", "disgust"]
        return {"emotion": emotions[emotion_index]}
    except Exception as e:
        print(f"Error in prediction: {e}")
        return {"error": str(e)}

    except Exception as e:
        return {"error": str(e)}

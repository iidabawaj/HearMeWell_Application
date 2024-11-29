# import tensorflow as tf
# 
# model_path = './models/best-CNNBi.h5'
# model = tf.keras.models.load_model(model_path)
# 
# print(f"Model input shape: {model.input_shape}")
# 
# model.summary()
# 
# 
# 

import librosa

# Define the file path for debugging
file_path = 'C:\\Users\\iidan\\HMW_python_backend\\HMW_python_backend\\Temp\\7c8f4e82-1796-4fc9-8326-2c6b732e9f15.wav'

try:
    y, sr = librosa.load(file_path, sr=None)  # Load with original sampling rate
    duration = librosa.get_duration(y=y, sr=sr)
    print(f"Audio Loaded Successfully: {file_path}")
    print(f"Sampling Rate: {sr}")
    print(f"Duration: {duration} seconds")
    print(f"Audio Shape: {y.shape}")
except Exception as e:
    print(f"Error: {e}")

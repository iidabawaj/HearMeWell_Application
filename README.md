# **HearMeWell: Emotion Recognition App**

> An application that integrates speech-to-text technology with emotion recognition, designed to help individuals with hearing impairments communicate effectively and understand emotions.

---

## **Project Overview**

**HearMeWell** is a cross-platform application that integrates **emotion recognition** with **speech-to-text** technology. It provides users with the ability to upload audio, receive transcriptions, and determine the emotional tone of the speaker’s voice. This app is designed to assist those with hearing impairments by converting spoken words into text and recognizing the emotions conveyed in the speech.

The application is composed of two main components:
- **Frontend**: A mobile application built using **Flutter**, which provides a user-friendly interface for interaction.
- **Backend**: A Flask-based server that processes audio, performs speech-to-text transcription, and emotion recognition.

---

## **Backend: Flask API**

### **Overview**
The **backend** of the application is built using **Flask**, a lightweight Python web framework. It is responsible for handling API requests, processing audio files, performing **speech-to-text** using the **Whisper model**, and emotion recognition using a pre-trained **EfficientNetB0 model**.

### **Features**
- **Speech-to-Text**: Converts audio input into text using OpenAI’s **Whisper** model.
- **Emotion Recognition**: Analyzes the audio to detect emotions such as happiness, sadness, anger, etc.
- **Firebase Authentication**: Allows users to sign in using their phone number with Firebase Authentication.
- **Model**: EfficientNetB0 model fine-tuned to recognize emotions from speech.

### **Technologies Used**
- **Python**
- **Flask** for the backend server
- **Whisper** for speech-to-text transcription
- **EfficientNetB0** for emotion recognition
- **Firebase Authentication** for phone number login
- **Git LFS** for managing large model files

### **Setup and Installation**
To set up the backend locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/HearMeWell/HearMeWell_BachelorProject.git

2. Navigate to the backend directory:
   ```bash
   cd backend
4. Create a virtual environment (optional but recommended):
   ```bash
    python -m venv venv

6. Install dependencies:
   ```bash
   pip install -r requirements.txt

8. Set up Firebase (Follow Firebase setup instructions to create your project and download the credentials file):
   ```bash
   Place the Firebase credentials JSON file in the Config/ folder.
   
10. Run the Flask application:
    ```bash
    python app.py

12. The backend will be running on
    ```bash
    http://localhost:5000.


# **HearMeWell: An Application for Emotion Signal Detection and Speech Recognition from Arabic Voice Messages** 

HearMeWell is a comprehensive solution that processes audio inputs to provide transcriptions accompanied by emotion recognition. The system comprises a Flask-based backend and a Flutter-based mobile frontend, delivering seamless user interaction and robust processing capabilities to help individuals with hearing impairments communicate effectively and understand emotions.
---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

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
   cd HearMeWell_BachelorProject/HearMeWell_Backend
   
3. Create and Activate a virtual environment (optional but recommended):
   ```bash
    python -m venv venv
   
    # On Windows
   venv\Scripts\activate
   
   # On Unix or MacOS
   
   source venv/bin/activate

4. Install dependencies:
   ```bash
   pip install -r requirements.txt

5. Set Up Environment Variables:
   ```bash
   Create a .env file in the backend directory with the necessary configurations.
   
6. Run the Flask application:
    ```bash
    python app.py

7. The backend will be running on
    ```bash
    http://localhost:5000.
    
---
## **Frontend: Flutter Mobile Application**

### **Overview**
The **frontend** of the application is built using **Flutter**, a powerful UI toolkit for building natively compiled applications for mobile, web, and desktop from a single codebase. It provides users with an intuitive interface to interact with the backend, upload audio files, view transcriptions, and see emotion analysis.

### **Features**
- **User Authentication**: Users can sign in using their phone number via Firebase Authentication.
- **Audio Upload**: Allows users to upload audio files for processing.
- **Emotion Display**: Displays transcribed text along with detected emotions.
- **Cross-Platform Compatibility**: Works seamlessly on both Android and iOS devices.
- **Responsive Design**: Delivers a consistent user experience across devices.

### **Technologies Used**
- **Flutter** for the mobile application
- **Dart** for application logic
- **Firebase Authentication** for secure login
- **HTTP requests** for communication with the Flask backend

### **Setup and Installation**
To set up the frontend locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/HearMeWell/HearMeWell_BachelorProject.git

2. Navigate to the frontend directory:
    ```bash
    cd HearMeWell_BachelorProject/HearMeWell_Frontend

3. Install dependencies:
   ```bash
   flutter pub get

4. Set Up Firebase for the Application:
- Go to Firebase Console and create a new Firebase project.
- Download the google-services.json file for Android and place it in the android/app directory.
- Download the GoogleService-Info.plist file for iOS and place it in the ios/Runner directory.
- Update the android/build.gradle and android/app/build.gradle files as per Firebase setup instructions.
  
5. Run the application:
   ```bash
   flutter run

6. The app will be deployed to your connected Android/iOS device or emulator.
 

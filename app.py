import streamlit as st
import whisper
import sounddevice as sd

from scipy.io.wavfile import write
import numpy as np
import os
from pydub import AudioSegment
import sys
sys.stderr = sys.stdout

# Function to transcribe audio
def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result['text']

# Function to record audio
def record_audio(duration=5, fs=44100):
    st.write("Heya !! Your audio is being Recorded...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    write('temp_recording.wav', fs, recording)
    st.write("There you go. Recording finished.")

# Main app function
def main():
    st.title('Welcome to Audio to Text Transcription')
    st.write('Upload an audio file or record live according to your need.')

    # File uploader
    uploaded_file = st.file_uploader("Upload an audio file...", type=['mp3', 'wav', 'ogg', 'm4a'])
    if uploaded_file is not None:
        with open("temp_uploaded.wav", "wb") as f:
            f.write(uploaded_file.getbuffer())
        text = transcribe_audio("temp_uploaded.wav")
        os.remove("temp_uploaded.wav")  # Clean up
        st.write('Transcribed Text:')
        st.write(text)

    # Audio recording
    if st.button('Record'):
        record_audio()
        text = transcribe_audio("temp_recording.wav")
        os.remove("temp_recording.wav")  # Clean up
        st.write('Transcribed Text from Recording:')
        st.write(text)

if __name__ == "__main__":
    main()

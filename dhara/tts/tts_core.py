import requests
import os
import base64
import pyaudio
import wave
from pydub import AudioSegment
import io

def tts(text):
    # Eleven Labs API Key
    api_key = os.getenv("ELEVENLABS_API_KEY")

    # Define the voice ID 
    voice_id = "Xb7hH8MSUJpSbSDYk0k2"

    # The URL for the text-to-speech API
    url = f"https://api.elevenlabs/io/v1/text-to-speech/{voice_id}"

    # Define payload
    payload = {
        "output_format": "mp3_44100_192",
        "text": text,  # Use the input text here
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    # Headers for the API request
    headers = {
        "xi-api_key": api_key,
        "Content-Type": "application/json"
    }

    # Send the POST request to Eleven LABS API
    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    # Check if the request was successful
    if response.status_code == 200:
        audio_data = response.content  # Get the audio data (MP3 format)

        # Convert MP3 to wav using pydub
        audio = AudioSegment.fromfile(io.BytesIO(audio_data), format='mp3')

        # Export the audio to a BytesIO object as WAV format
        wav_io = io.BytesIO()
        audio.export(wav_io, format='wav')

        # Reset the BytesIO object to start reading from the beginning
        wav_io.seek(0)

        # Play audio using PyAudio
        def play_audio(wav_io):
            p = pyaudio.PyAudio()

            # Use Wave module to read the BytesIO as a wave file
            wave_file = wave.open(wav_io, 'rb')

            # Open an audio stream
            stream = p.open(format=p.get_format_from_width(wave_file.getsampwidth()),
                            channels=wave_file.getnchannels(),
                            rate=wave_file.getframerate(),
                            output=True)

            # Read Audio data in chunks and play
            data = wave_file.readframes(1024)
            while data:
                stream.write(data)
                data = wave_file.readframes(1024)

            # Close the stream
            stream.stop_stream()
            stream.close()
            p.terminate()

        # Play the audio from the WAV data
        play_audio(wav_io)
    else:
        print(f"Error: {response.status_code}, {response.text}")

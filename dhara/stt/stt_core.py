import requests
import os
import wave
import pyaudio

def record_audio(duration=5,output_file='recorded_audio.wav'):
    # Setting up parameters for recording
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024

    p = pyaudio.PyAudio()

    stream = p.open(
        format = FORMAT,
        channels = CHANNELS,
        rate = RATE,
        input = True,
        frames_per_buffer = CHUNK
    )
    print("Recording now...")
    frames = []

    for _ in range(0,int(RATE/CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Finished Recording.")

    # Stopping and closeing the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Saving the recorded audio file as WAV file
    with wave.open(output_file,'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsamplewidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    
    return output_file


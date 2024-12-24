from dhara.stt.stt_core.py import record_audio
from dhara.tts.tts_core.py import tts

def main():
    print("Testing DHARA Speech Engine")
    while True:

        #Step 01: Record user input
        print("\nRecording user-input")
        audio_file = record.audio(duration = 5) # Record for 5seconds
        print(f"Audio recorded: {audio_file}")


        #Step 02: Process the recorded audio (Mockup for STT)
        user_input = record_audio(audio_file)
        if user_input:
            print(f"User input: {user_input}")


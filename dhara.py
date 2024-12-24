from dhara.stt.stt_core import record_audio
from dhara.tts.tts_core import tts

print("Loading successfully!")
def main():
    print("Testing DHARA Speech Engine")
    while True:

        #Step 01: Record user input
        print("\nRecording user-input")
        audio_file = record_audio(duration = 5) # Record for 5seconds
        print(f"Audio recorded: {audio_file}")


        #Step 02: Process the recorded audio (Mockup for STT)
        user_input = record_audio(audio_file)
        if user_input:
            print(f"User input: {user_input}")

if __name__ == "__main__":
    main()
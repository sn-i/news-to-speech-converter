import azure.cognitiveservices.speech as speechsdk
import os
from dotenv import load_dotenv
import tempfile
from shutil import copyfileobj
import logging

load_dotenv()


class Tts:
    def __init__(self):
        self.speech_key = os.getenv('speech_key')
        self.service_region = os.getenv('service_region')
        self.speech_config = speechsdk.SpeechConfig(subscription=self.speech_key, region=self.service_region)
        self.speech_config.speech_synthesis_voice_name = "ka-GE-EkaNeural"
        self.speech_config.set_speech_synthesis_output_format(
            speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3)

    def convert_text_to_speech(self, text, output_file="output.mp3"):
        try:
            chunk_size = 6000
            text_chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_files = []
                for index, chunk in enumerate(text_chunks):
                    temp_filename = os.path.join(temp_dir, f"chunk_{index}.mp3")
                    audio_output = speechsdk.AudioConfig(filename=temp_filename)
                    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config,
                                                                     audio_config=audio_output)

                    result = speech_synthesizer.speak_text_async(chunk).get()

                    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                        print(f"Chunk {index + 1} synthesized successfully and saved as {temp_filename}.")
                        temp_files.append(temp_filename)
                    elif result.reason == speechsdk.ResultReason.Canceled:
                        cancellation_details = result.cancellation_details
                        print("Speech synthesis canceled:", cancellation_details.reason)
                        if cancellation_details.reason == speechsdk.CancellationReason.Error:
                            print("Error details:", cancellation_details.error_details)
                        return

                with open(output_file, "wb") as final_audio:
                    for temp_file in temp_files:
                        with open(temp_file, "rb") as temp_audio:
                            copyfileobj(temp_audio, final_audio)


            logging.info(f"Final audio content saved to {output_file}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")


# # Initialize TTS object
# tts = Tts()
#
# # Get text to convert
# text_to_convert = input("Enter the text you want to convert to speech: ")
#
# tts.convert_text_to_speech(text_to_convert)
import whisper
import sounddevice as sd
import numpy as np
import wave
import time

class VR:
    def __init__(self, duration=5, sample_rate=16000):
        self.duration = duration
        self.sample_rate = sample_rate
        self.model - whisper.load_model("base")
    
    def record_audio(self):
        print("Listening...")
        audio_data = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='int16')
        sd.wait()
        print("Finished.")
        return audio_data
    
    def save_audio(self, audio_data, filename="tmp/output.wav"):
        with wave.open(filename, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(self.sample_rate)
            wf.writeframes(audio_data)
        print(f"Audio saved to {filename}.")
    
    def transcribe_audio(self, filename="tmp/output.wav"):
        result = self.model.transcribe(filename)
        print(f"Transcription: {result["text"]}")
        return result["text"]
    
    def save_transcript(self, text, filename="tmp/speech.txt"):
        with open("./tmp/sentence.txt", "w+") as file:
            file.write(result["text"])
        print(f"Transcription saved to {filename}.")
    
    def run(self):
        audio_data = self.record_audio()
        self.save_audio(audio_data.tobytes(), "tmp/output.wav")
        transcription = self.transcribe_audio("tmp/output.wav")
        self.save_transcript(transcription, "tmp/speech.txt")

if __name__ == "__main__":
    vr = VR(duration=5)
    vr.run()



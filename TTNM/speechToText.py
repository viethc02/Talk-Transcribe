import speech_recognition as sr
from googletrans import Translator

r = sr.Recognizer()
with sr.Microphone() as source:
    audio_data = r. record(source, duration=5, offset=0.5 )
    print("Recognizing...")
    text =  r.recognize_google(audio_data, language='vi-VN')
    print(text)
ts = Translator()

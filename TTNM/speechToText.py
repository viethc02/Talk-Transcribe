import speech_recognition as sr


r = sr.Recognizer()
mic = sr.Microphone()
# ham nhận diện giọng nói chuyển thành text
# hàm trả về 1 dic trong đó key 'transcription' là text, 'error' là None nếu chuyển được giọng nói thành text
def recognize_speech_to_text(mic, r):
    with mic as source:
        # r.adjust_for_ambient_noise(source)
        audio_data = r. record(source, duration=5, offset=0.5 )
        print("Recognizing...")
    response = {
        'success' : True,
        'error' : None,
        'transcription' : None
    }
    try:
        response['transcription'] = r.recognize_google(audio_data, language= 'vi-VN')
    except sr.RequestError:
        response['success'] = False
        response['error'] = 'Api was unavailable'
    except sr.UnknownValueError:
        response['error'] = 'Unable to recognize'
    return response



example = recognize_speech_to_text(mic, r)
if not example['error']:
    text = example['transcription']
    text = text.lower()
    print(text)
    if('có' in text):
        print('Yes')
    if 'không' in text:
        print('No')
else:
    print(example['error'])

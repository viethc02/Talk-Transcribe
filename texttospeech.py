import os
from gtts import gTTS
import playsound
import sys



def texttospeech(text):
    import gtts
    output = gTTS(text, lang= "vi", slow=False)
    output.save("output.mp3")
    playsound.playsound('output.mp3', True)
    os.remove("output.mp3")

sys.modules[__name__] = texttospeech
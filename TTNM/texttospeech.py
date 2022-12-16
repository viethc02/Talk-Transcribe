from gtts import gTTS
import playsound
import sys



def texttospeech(text, lang1):
    import gtts
    language = gtts.lang.tts_langs()
    if lang1 in language.keys():
        output = gTTS(text, lang=lang1, slow=False)
        output.save("output.mp3")
        playsound.playsound('output.mp3', True)
        os.remove("output.mp3")

    else:
        text = "Please choose correct languages you want"
        output = gTTS(text, lang="en", slow=False)
        output.save("output1.mp3")
        playsound.playsound('output1.mp3', True)
        os.remove("output1.mp3")

sys.modules[__name__] = texttospeech

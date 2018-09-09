
import speech_recognition as sr
from utility.AI import textToSpeech
import playsound
from utility.animation.eyes import EYE
from utility.animation.graphics import *


class Search:
    text = ""

    @staticmethod
    def config():
        print("Keywords for the faster Joanna Response")
        print(" ")
        print("KEYWORDS                         OPERATIONS")
        print("--------                         ---------")
        print("SEARCH                           google is the saviour")
        print("FILE                             searches a file in system and Opens it")
        print("PLAY or SONG                     Plays music")
        print("WEATHER REPORT                   Tells the current weather of a place")
        print(" ")
        # Sample rate is how often values are recorded
        # EYE.eyes()
        sample_rate = 48000
        # Chunk is like a buffer. It stores 2048 samples (bytes of data)
        # here.
        # it is advisable to use powers of 2 such as 1024 or 2048
        chunk_size = 2048
        # Initialize the recognizer
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            playsound.playsound('downloads/intro-sounds/Major-Intro2.mp3', True)
            # listens for the user's input
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("This is what you said: " + text)
                # playsound.playsound('downloads/intro-sounds/sure.mp3', True)
                textToSpeech.text_converter(text)
                # return text
                # error occurs when google could not understand what was said
            except sr.UnknownValueError:
                print("Joanna could not understand what you mean")
                playsound.playsound('downloads/intro-sounds/not-understandable.mp3', True)
            except sr.RequestError as e:
                print("Joanna could not request results from Google Speech Recognition service; {0}".format(e))







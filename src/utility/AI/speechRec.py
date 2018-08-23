import speech_recognition as sr
from utility.AI import textToSpeech
import playsound


class Speech:
    text = ""

    def config(self):
        # Sample rate is how often values are recorded
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
            playsound.playsound('downloads/intro.mp3', True)
            print("**** Pick One :  Rock or Jazz ****")
            # listens for the user's input
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("This is what you said: " + text)
                textToSpeech.text_converter(text)
                # return text
                # error occurs when google could not understand what was said
            except sr.UnknownValueError:
                print("Joanna could not understand what you mean")
            except sr.RequestError as e:
                print("Joanna could not request results from Google Speech Recognition service; {0}".format(e))


s1 = Speech()
s1.config()





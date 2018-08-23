import math
import speech_recognition as sr
import playsound

operation = ""


def get_numbers():
    playsound.playsound('utility/AI/AI-sounds/calc.mp3', True)
    playsound.playsound('utility/AI/AI-sounds/operation.mp3', True)
    getting_numbers()
    if "addition" in operation or "add" in operation or "Add" in operation:
        first_number()
        # print(first_number() + sec_number())


def getting_numbers():
    sample_rate = 48000
    chunk_size = 2048
    # Initialize the recognizer
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        # listens for the user's input
        audio1 = r.listen(source)
        try:
            text = r.recognize_google(audio1)
            print("You mean: " + text)
            operation = str(text)
            return operation
        except sr.UnknownValueError:
            print("Joanna could not understand what you mean")
            playsound.playsound('downloads/intro-sounds/not-understandable.mp3', True)
        except sr.RequestError as e:
            print("Joanna could not request results from Google Speech Recognition service; {0}".format(e))


def first_number():
    playsound.playsound('utility/AI/AI-sounds/first-number.mp3', True)
    getting_numbers()
    frst = int(operation)
    return frst


def sec_number():
    playsound.playsound('utility/AI/AI-sounds/sec-number.mp3', True)
    getting_numbers()
    sec = int(operation)
    return sec

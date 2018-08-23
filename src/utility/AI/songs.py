import playsound
import speech_recognition as sr


def songs():
    playsound.playsound('downloads/intro-sounds/Rock-or-Jazz.mp3', True)
    r1 = sr.Recognizer()
    mic1 = sr.Microphone()
    with mic1 as source:
        r1.adjust_for_ambient_noise(source)
        # listens for the user's input
        audio1 = r1.listen(source)
        try:
            text1 = r1.recognize_google(audio1)
            print("You mean: " + text1)
            playsound.playsound('downloads/intro-sounds/sure.mp3', True)
            genre_option = str(text1)
            if "rock" in genre_option or "vock" in genre_option:
                playsound.playsound('downloads/intro-sounds/rock.mp3', True)
                playsound.playsound('downloads/intro-sounds/rock2.mp3', True)
                playsound.playsound('downloads/intro-sounds/rock3.mp3', True)
                playsound.playsound('downloads/songs/Kalimba.mp3', True)
            elif "Jazz" in genre_option or "jazz" in genre_option or "just" in genre_option:
                playsound.playsound('downloads/intro-sounds/jazz1.mp3', True)
                playsound.playsound('downloads/intro-sounds/rock2.mp3', True)
                playsound.playsound('downloads/intro-sounds/rock3.mp3', True)
                playsound.playsound('downloads/songs/Sleep Away.mp3', True)
        except sr.UnknownValueError:
            print("Joanna could not understand what you mean")
            playsound.playsound('downloads/intro-sounds/not-understandable.mp3', True)
        except sr.RequestError as e:
            print("Joanna could not request results from Google Speech Recognition service; {0}".format(e))

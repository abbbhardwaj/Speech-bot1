import playsound
from weather import Weather, Unit
import speech_recognition as sr


def weather_report():
    playsound.playsound('downloads/City.mp3', True)
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        # listens for the user's input
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            playsound.playsound('downloads/intro-sounds/sure.mp3', True)
            print("You mean: " + text)
            # return text
            # error occurs when google could not understand what was said
            weather = Weather(unit=Unit.CELSIUS)
            location = weather.lookup_by_location(str(text))
            condition = location.condition
            print(condition.text)
            if str(condition.text).__eq__("Mostly Cloudy"):
                playsound.playsound('downloads/weather/Mostly-Cloudy.mp3', True)
            elif str(condition.text).__eq__("Cloudy"):
                playsound.playsound('downloads/weather/Cloudy.mp3', True)
            elif str(condition.text).__eq__("Thunderstorms"):
                playsound.playsound('downloads/weather/Thunderstorms.mp3', True)
            elif str(condition.text).__eq__("Partly Cloudy"):
                playsound.playsound('downloads/weather/Partly-Cloudy.mp3', True)
            elif str(condition.text).__eq__("Mostly Clear"):
                playsound.playsound('downloads/weather/Mostly-Clear.mp3', True)
            elif str(condition.text).__eq__("Sunny"):
                playsound.playsound('downloads/weather/Sunny.mp3', True)
        except sr.UnknownValueError:
            print("Joanna could not understand what you mean")
            playsound.playsound('downloads/intro-sounds/not-understandable.mp3', True)
        except sr.RequestError as e:
            print("Joanna could not request results from Google Speech Recognition service; {0}".format(e))
        except ConnectionError:
            print("Not able to create connection")
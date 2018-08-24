from utility.AI.songs import songs
from utility.AI.weather import weather_report
from information.aboutQasource.qasource import qa_about_us
from information.aboutJoanna.joanna import about_joanna
from utility.AI.calc import get_numbers
from information.googleSearch import Google
import playsound


def text_converter(text):
    stro = str(text)
    if "song" in stro:
        songs()
    elif "file" in stro or "open" in stro:
        data = open("downloads/Blog-QA Outsourcing.docx", 'r+', encoding="ISO-8859-1").read()
        print(data)
    elif "weather" in stro:
        weather_report()
    elif "about yourself" in stro or "yourself" in stro or "you" in stro:
        about_joanna()
    elif "calculate" in stro or "calculation" in stro or "calculator" in stro:
        get_numbers()
    elif "QA" in stro or "shows" in stro or "QA source" in stro:
        qa_about_us()
    elif "search" in stro or "Search" in stro or "Find" in stro or "google" in stro or "Google" in stro:
        Google.google_search(stro)
    else:
        playsound.playsound('downloads/intro-sounds/not-understandable.mp3', True)
        # Playing the converted file
        # os.system('mpg321 Mostly-Cloudy.mp3 &')




import playsound
import docx
from weather import Weather, Unit
import speech_recognition as sr


qasource_text = "OUR MISSION is to provide our partners with quality that creates value."
text2 = "Q A source is a Leading Software Testing Company which Provides A Workplace That Facilitates"
text3 = "Hard Work , Innovation, And Engineer Retention"
text4 = "We insist you to log onto www. q a source.com for more details"


def qa_about_us():
    playsound.playsound('information/aboutQasource/qa-intro.mp3', True)
    playsound.playsound('information/aboutQasource/qa-intro1.mp3', True)
    playsound.playsound('information/aboutQasource/qaSource.mp3', True)
    playsound.playsound('information/aboutQasource/qa-intro2.mp3', True)


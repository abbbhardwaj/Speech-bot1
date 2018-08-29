from testVocab import speak_distance, speak_duration
import urllib.request
import json
import playsound
import speech_recognition as sr


def google_maps():

    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    api_key = 'AIzaSyAur0DgvVfmAKogy4Ivoxy1eauu-fJhTAE'
    playsound.playsound('maps/sounds/origin.mp3', True)
    origin = get_locations().replace(' ', '+')
    playsound.playsound('maps/sounds/destination.mp3', True)
    destination = get_locations().replace(' ', '+')

    nav_request = 'origin={}&destination={}&key={}'.format(origin, destination, api_key)

    request = endpoint + nav_request
    print(request)
    response = urllib.request.urlopen(request).read()
    directions = json.loads(response)
    # print(directions)
    routes = directions['routes']
    legs = routes[0]['legs']
    print(legs[0]['distance']['text'])
    playsound.playsound(speak_distance(legs[0]['distance']['text']), True)
    print(legs[0]['duration']['text'])
    playsound.playsound(speak_duration(legs[0]['duration']['text']), True)


def get_locations():
    r1 = sr.Recognizer()
    mic1 = sr.Microphone()
    with mic1 as source:
        r1.adjust_for_ambient_noise(source)
        # listens for the user's input
        audio1 = r1.listen(source)
        try:
            text1 = r1.recognize_google(audio1)
            print("You mean: " + text1)
            location = str(text1)
            return location
        except sr.UnknownValueError:
            print("Joanna could not understand what you mean")
            playsound.playsound('downloads/intro-sounds/not-understandable.mp3', True)
        except sr.RequestError as e:
            print("Joanna could not request results from Google Speech Recognition service; {0}".format(e))




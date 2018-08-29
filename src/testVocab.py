from gtts import gTTS

my_text = "मेरा नाम है जोअन्ना है.  आपका स्वागत है."
my_text1 = "Where do you want to go? "
t1 = "Here is the list of links I have found for you."


language = 'en'
myobj = gTTS(text=my_text1, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("maps/sounds/destination.mp3")


def run_time_text(text):
    t1 = "The answer is " + text
    language = 'en'
    myobj = gTTS(text=t1, lang=language, slow=False)
    # Saving the converted audio in a mp3 file named
    # welcome
    loc = "downloads/run-time-sounds/test1.mp3"
    myobj.save(loc)
    return loc


def speak_distance(distance):
    t1 = "Distance is " + distance
    language = 'en'
    myobj = gTTS(text=t1, lang=language, slow=False)
    # Saving the converted audio in a mp3 file named
    # welcome
    loc = "maps/sounds/distance.mp3"
    myobj.save(loc)
    return loc


def speak_duration(duration):
    t1 = "and It will take you around" + duration + " to reach there"
    language = 'en'
    myobj = gTTS(text=t1, lang=language, slow=False)
    # Saving the converted audio in a mp3 file named
    # welcome
    loc = "maps/sounds/duration.mp3"
    myobj.save(loc)
    return loc

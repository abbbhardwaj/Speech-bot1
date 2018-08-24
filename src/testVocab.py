from gtts import gTTS

my_text = "मेरा नाम है जोअन्ना है.  आपका स्वागत है."
my_text1 = "Tell me the second number"
t1 = "Here is the list of links I have found for you."



language = 'en'
myobj = gTTS(text=t1, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("information/googleSearch/sounds/search-links.mp3")


def run_time_text(text):
    t1 = "The answer is " + text
    language = 'en'
    myobj = gTTS(text=t1, lang=language, slow=False)
    # Saving the converted audio in a mp3 file named
    # welcome
    loc = "downloads/run-time-sounds/test1.mp3"
    myobj.save(loc)
    return loc


from gtts import gTTS

my_text = "मेरा नाम है जोअन्ना है.  आपका स्वागत है."
my_text1 = "Tell me the second number"
t1 = "Addition, subtraction, multiplication or division"


language = 'en'
myobj = gTTS(text=my_text1, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("utility/AI/AI-sounds/sec-number.mp3")

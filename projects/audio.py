from gtts import gTTS

import os

#from playsound import playsound

#s = gTTS("Sample Text")
#s.save('sample.mp3')
#playsound('sample.mp3')

mytext = "Emerson do Nascimento Rodrigues"


language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("som.mp3")

os.system("mpg321 som.mp3")

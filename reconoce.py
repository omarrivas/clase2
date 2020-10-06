import speech_recognition as speechRecognition
from gtts import gTTS
from playsound import playsound

reconocedor= speechRecognition.Recognizer()

with speechRecognition.Microphone() as fuente:
    print ("Diga algo: ")
    audio = reconocedor.listen(fuente)

try:
    #texto = reconocedor.recognize_google(audio)
    texto = reconocedor.recognize_google(audio, language="es-AR")
    print ("dijiste " + texto)
except:
    print ("error durante la conversion")


tts = gTTS(texto, lang='es-us')
tts.save("mensaje.mp3")
playsound('mensaje.mp3')

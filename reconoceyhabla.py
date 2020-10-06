import speech_recognition as speechRecognition
from gtts import gTTS
from playsound import playsound
import os

fin= False
while fin== False:
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

    texto= texto.lower()
    texto= texto.replace('á', 'a')
    texto = texto.replace('é', 'e')
    texto = texto.replace('í', 'i')
    texto = texto.replace('ó', 'o')
    texto = texto.replace('ú', 'u')
    if texto== "hola como estas" or texto == "hola como te va":
        tts = gTTS("Muy bien, y vos?", lang='es-us')
    elif texto== "bien" or texto == "muy bien":
        tts = gTTS("Me alegro mucho", lang='es-us')
    elif texto== "mal" or texto == "mas o menos":
        tts = gTTS("Realmente una pena, espero te mejores", lang='es-us')
    elif texto== "cancelar":
        tts = gTTS("Hasta pronto", lang='es-us')
        fin= True

    tts.save("mensaje.mp3")
    playsound('mensaje.mp3')
    os.remove("mensaje.mp3")


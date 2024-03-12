import os
import pyttsx3
import keyboard
import webbrowser
import speech_recognition as sr

r = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', int(rate) - 35)

aurkezpena = "https://docs.google.com/presentation/d/e/2PACX-1vQ5VDTkSf3A72s_K8g7mOZ0_CXVvI4pbhNfdWNyBgEBZpm1U1b-z4wvdIvDmWOYlHAfJI4HRZFHHgfd/pub?start=false&loop=false&delayms=3000&slide=id.p"
language = "basque"


def talk(message):
    engine.say(message)
    engine.runAndWait()


def listen(model):
    os.system("cls")
    mic = sr.Microphone()
    with mic as source:
        # r.adjust_for_ambient_noise(source, duration=5)
        # r.dynamic_energy_threshold = True
        print("Entzuten...")
        audio = r.listen(source)

    text = r.recognize_whisper(audio, language=language, model=model)
    return text


def main():
    start = listen("small")
    print(start)
    if "nano" in start:
        talk("Kaixo Diego!, ¿zer egin nahi duzu?")
    else:
        talk("¿Zer egin nahi duzu?")

    text = listen("small")
    print(text)
    while True:
        if "ireki" in text.lower():
            talk("Bikain, proiektua irekitzen!, Ondo izan!")
            print("Irekitzen...")
            webbrowser.open(aurkezpena)
            keyboard.press_and_release("F11")
            break
        elif "irten" in text.lower():
            talk("Agur, ondo izan")
            break
        else:
            talk("Ez zaitut ulertu, errepikatu mesedes")
            text = listen("small")


if __name__ == "__main__":
    main()

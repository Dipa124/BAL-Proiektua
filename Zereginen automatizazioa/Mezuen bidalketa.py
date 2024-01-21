import time
import keyboard
import pywhatkit
import PySimpleGUI as sg
from colorama import Fore, Style, Back

sg.theme("Reddit")
layout_l = [[sg.Text("SPAM:", p=0)],
            [sg.Text("Bidali nahi den mezua idatzi ondoren:")],
            [sg.Input("", key="-MezuaSpam-")],
            [sg.Button("Ok", key="-Ok-"), sg.Button("Salir", key="-Exit-")],
            [sg.Spin([1, 2, 3, 4, 5, 6])]
           ]

layout_r = [[sg.Text("PROGRAMATUTA:")],
            [sg.Text("Bidali nahi den mezua idatzi ondoren:")],
            [sg.Input("", key="-MezuaProg-")],
            [sg.Button("Programatu eta bidali", key="-PET-")],
            [sg.Text("".upper(), key="-Error-")],
            [sg.Text("".upper(), key="-Notes-")]
           ]
layout = [[sg.T('MEZUEN BIDALTZE AUTOMATIKOA', font='_ 14', justification='c', expand_x=True)],
          [sg.Col(layout_l, p=8), sg.VerticalSeparator(), sg.Col(layout_r, p=8)]
         ]

window = sg.Window("MezuenApp", layout)

def spam():
    time.sleep(4)

    while True:
        # keyboard.write("@IZENA\n")
        keyboard.write("Bidali nahi den textua")
        time.sleep(0.05)
        keyboard.send("enter")
        time.sleep(0.1)

        if keyboard.is_pressed("space"):
            exit()


def programatuta(zenbakia, mezua, orduak, minutuak):
    try:
        pywhatkit.sendwhatmsg(zenbakia, mezua, orduak, minutuak, wait_time=True, close_time=4)
    except:
        print(Style.BRIGHT + Fore.RED + "Ezin izan da mezua bidali" + Style.RESET_ALL)


def main():
    while True:
        event, value = window.read()

        if event == sg.WIN_CLOSED or event == "-Exit-":
            break


if __name__ == "__main__":
    main()

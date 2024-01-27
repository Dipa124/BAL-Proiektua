import time
import keyboard
import pywhatkit
import PySimpleGUI as sg
from colorama import Fore, Style, Back

orduak = ["00"]

# Interfaze grafikoaren konfigurazioa
sg.theme("Reddit")
layout = [[sg.T('MEZU PROGRAMATUAK', font=("Segoe UI", 20, "bold"), justification='c', expand_x=True)],
          [sg.Text("SPAM MEZUA:", font=("Futura", 11, "bold")),],
          [sg.Text("Bidali nahi den mezua eta errepikatu nahi den aldiak aukeratu:", font=("Futura", 11))],
          [sg.Input("", expand_x=True, key="-MezuaSpm-"),
           sg.Spin(list(range(1, 12000)), key="-Aldiak-"),
           sg.Button("BIDALI", key="-BidaliSpm-", font=("Segoe UI", 9, "bold"))],
          [sg.Text("".upper(), key="-OharraSpm-")],

          [sg.HorizontalSeparator(p=12)],

          [sg.Text("MEZU PROGRAMATUA:", font=("Futura", 11, "bold")),],
          [sg.Text("Bidali nahi den mezua eta errepikatu nahi den aldiak aukeratu:", font=("Futura", 11))],
          [sg.Input("", expand_x=True, key="-MezuaPrg-")],
          [sg.Text("Ordua aukeratu: ", font=("Futura", 11)),
           sg.Spin([str(i).zfill(2) for i in range(25)], key="-Orduak-", pad=0),
           sg.Text(":", font=("Futura", 11, "bold"), pad=0),
           sg.Spin([str(i).zfill(2) for i in range(60)], key="-Minutuak-", pad=0),
           sg.Text("Telefono zenbakia zehaztu: ", font=("Futura", 11)),
           sg.Input("", expand_x=True, key="-Zenbakia-"),
           sg.Button("BIDALI", key="-BidaliPrg-", font=("Segoe UI", 9, "bold"))
           ],
          [sg.Text("".upper(), key="-OharraPrg-")],
          ]
window = sg.Window("MezuApp", layout)

def spam(mezua, aldiak):
    time.sleep(4)
    while aldiak > 0:
        keyboard.write(mezua)
        time.sleep(0.05)
        keyboard.send("enter")
        time.sleep(0.1)
        aldiak -= 1
        if keyboard.is_pressed("space"):
            exit()


def programatuta(zenbakia, mezua, orduak, minutuak):
    try:
        pywhatkit.sendwhatmsg(zenbakia, mezua, orduak, minutuak, wait_time=30, close_time=4)
    except:
        window["-OharraPrg-"].update("Ezin izan da mezua bidali", text_color="#c40000")


def main():
    while True:
        event, value = window.read()

        if event == "-BidaliSpm-":
            window["-OharraSpm-"].update("")
            mezua_spm = value["-MezuaSpm-"]
            aldiak = int(value["-Aldiak-"])
            if mezua_spm != "" and aldiak > 0:
                try:
                    spam(mezua_spm, aldiak)
                except:
                    window["-OharraSpm-"].update("Bidalketa gelditu da", text_color="#076f8c")
            else:
                window["-OharraSpm-"].update("Sarrera okerrak, saiatu berriro", text_color="#c40000")

        if event == "-BidaliPrg-":
            window["-OharraPrg-"].update("")
            mezua_prg = value["-MezuaPrg-"]
            if mezua_prg != "":
                try:
                    orduak, minutuak = int(value["-Orduak-"]), int(value["-Minutuak-"])
                    zenbakia = value["-Zenbakia-"]
                    window["-OharraPrg-"].update("Mezua bidaltzen...", text_color="#076f8c")
                    time.sleep(2)
                    programatuta(zenbakia, mezua_prg, orduak, minutuak)
                except:
                    window["-OharraPrg-"].update("Sarrera okerrak, saiatu berriro", text_color="#c40000")
            else:
                window["-OharraPrg-"].update("Sarrera okerrak, saiatu berriro", text_color="#c40000")

        if event == sg.WIN_CLOSED or event == "-Exit-":
            break


if __name__ == "__main__":
    main()

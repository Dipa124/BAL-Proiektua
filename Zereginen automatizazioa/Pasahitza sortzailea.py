import random
import string
import PySimpleGUI as sg
import pyperclip as arbela

# Interfaze grafikoaren konfigurazioa
sg.theme("Reddit")
layout = [[sg.T('PASAHITZA SORTZAILEA', font=("Segoe UI", 20, "bold"), justification='c', expand_x=True)],
          [sg.Text("Aukeratu pasahitzaren karakter kopurua:", font=("Futura", 11))],
          [sg.Spin(list(range(101)), expand_x=True, key="-Luzeera-"),
           sg.Button("SORTU", key="-Sortu-", font=("Segoe UI", 9, "bold"))],
          [sg.HorizontalSeparator(p=12)],
          [sg.Text("Pasahitza: ", font=("Futura", 11, "bold")), sg.Input("", key="-Pasahitza-"),
           sg.Button("KOPIATU", key="-Kopiatu-", font=("Segoe UI", 9, "bold"))],
          [sg.Text("".upper(), key="-Oharra-")]
          ]
window = sg.Window("PasahitzApp", layout)


# Pasahitza sortzen duen funtzioa
def pasahitza_sortzailea(luzeera):
    pasahitza = ""
    for z in range(0, int(luzeera)):
        karakter_mota = random.choice(("zenbakia", "letra", "sinboloa"))

        if karakter_mota == "zenbakia":
            karakterra = str(random.choice(string.digits))
            pasahitza += karakterra
        elif karakter_mota == "letra":
            karakterra = random.choice(string.ascii_letters)
            pasahitza += karakterra
        elif karakter_mota == "sinboloa":
            karakterra = random.choice(string.punctuation)
            pasahitza += karakterra
    return pasahitza


# Programaren buklea
def main():
    while True:
        event, value = window.read()

        if event == sg.WIN_CLOSED or event == "-Irten-":
            break
        if event == "-Sortu-":
            try:
                luzeera = int(value["-Luzeera-"])
                window["-Oharra-"].update("")
                window["-Pasahitza-"].update("")
                window["-Pasahitza-"].update(str(pasahitza_sortzailea(luzeera)))

            except:
                window["-Oharra-"].update("Ziurtatu aukeratutako luzeera zenabki osoa dela mesedez!", text_color="#c40000")
        if event == "-Kopiatu-":
            arbela.copy(value["-Pasahitza-"])
            window["-Oharra-"].update("Pasahitza ordenagailuko arbelera kopiatu da!", text_color="#076f8c")


# Kodea executatu
if __name__ == "__main__":
    main()

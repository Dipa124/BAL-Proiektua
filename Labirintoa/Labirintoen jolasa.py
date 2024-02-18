import copy
import time
import keyboard
import Mapak as mp
from os import system
from colorama import Fore, Style


class Blokea:
    def __init__(self, testura):
        self.testura = testura

    def posizioa(self, mapa):
        for l in mapa:
            for z in l:
                if mapa[mapa.index(l)][l.index(z)] == self.testura:
                    return [mapa.index(l), l.index(z)]


class Jokalaria:
    def __init__(self, lerroa, zutabea, testura):
        self.lerroa = lerroa
        self.zutabea = zutabea
        self.testura = testura

    def behera(self):
        self.lerroa += 1

    def gora(self):
        self.lerroa -= 1

    def eskuma(self):
        self.zutabea += 1

    def ezkerra(self):
        self.zutabea -= 1


def mapa_aukeraketa():
    while True:
        mapa_aukeratua = input("Nahi duzun maparen zenbakia idatzi (0tik 6ra) edo irten (i/I): ")
        system("cls")
        match mapa_aukeratua:
            case "0":
                return mp.MAPA0
            case "1":
                return mp.MAPA1
            case "2":
                return mp.MAPA2
            case "3":
                return mp.MAPA3
            case "4":
                return mp.MAPA4
            case "5":
                return mp.MAPA5
            case "6":
                return mp.MAPA6

        if mapa_aukeratua in ["i", "I"]:
            exit()
        else:
            print(Style.BRIGHT + Fore.RED + "\nEmandako erantzuna ez da zuzena, saiatu berriro mesedez.",
                  "\nZiurtatu aukeretako bat soilik erantzun izana" + Style.RESET_ALL)


def mapa_errendatu(mapa, jokalaria):
    mapa_eguneratua = copy.deepcopy(mapa)
    mapa_eguneratua[jokalaria.lerroa][jokalaria.zutabea] = jokalaria.testura

    system("cls")
    print("\nX{}MAPA{}X".format("-" * (len(mapa[0]) - 2), "-" * (len(mapa[0]) - 2)))
    for l in mapa_eguneratua:
        print("|{}|".format("".join(map(str, l))))
    print("X{}X".format("--" * (len(mapa[0]))))


def mugimendua(mapa, jokalaria, horma, gertaera):
    # GORA
    if gertaera.name == "flecha arriba" or gertaera.name == "w":
        if 0 < jokalaria.lerroa < len(mapa):
            try:
                if mapa[jokalaria.lerroa - 1][jokalaria.zutabea] != horma.testura:
                    jokalaria.gora()
                    mapa_errendatu(mapa, jokalaria)
            except:
                pass
        else:
            print("Ezin zara gora mugitu")
    # BEHERA
    elif gertaera.name == "flecha abajo" or gertaera.name == "s":
        if 0 <= jokalaria.lerroa < len(mapa) - 1:
            try:
                if mapa[jokalaria.lerroa + 1][jokalaria.zutabea] != horma.testura:
                    jokalaria.behera()
                    mapa_errendatu(mapa, jokalaria)
            except:
                pass
        else:
            print("Ezin zara behera mugitu")
    # ESKUMA
    elif gertaera.name == "flecha derecha" or gertaera.name == "d":
        if 0 <= jokalaria.zutabea < len(mapa[0]) - 1:
            try:
                if mapa[jokalaria.lerroa][jokalaria.zutabea + 1] != horma.testura:
                    jokalaria.eskuma()
                    mapa_errendatu(mapa, jokalaria)
            except:
                pass
        else:
            print("Ezin zara eskumara mugitu")
    # EZKERRA
    elif gertaera.name == "flecha izquierda" or gertaera.name == "a":
        if 0 < jokalaria.zutabea < len(mapa[0]):
            try:
                if mapa[jokalaria.lerroa][jokalaria.zutabea - 1] != "🔳":
                    jokalaria.ezkerra()
                    mapa_errendatu(mapa, jokalaria)
            except:
                pass
        else:
            print("Ezin zara ezkerrera mugitu")


def jolasa():
    jokalaria = Jokalaria(1, 1, "🔷")
    HORMA = Blokea("🔳")
    ZORUA = Blokea("🔲")
    HELMUGA = Blokea("🚩")
    MAPA = mapa_aukeraketa()
    mapa_errendatu(MAPA, jokalaria)
    hasierako_denbora = time.perf_counter()

    while True:
        gertaera = keyboard.read_event()
        # IRTEN
        if gertaera.name == "esc":
            break
        # MUGIMENDUA
        elif gertaera.event_type == "down":
            mugimendua(MAPA, jokalaria, HORMA, gertaera)

        # HELMUGARA HELDU DEN DETEKTATU
        if MAPA[jokalaria.lerroa][jokalaria.zutabea] == HELMUGA.testura:
            bukaerako_denbora = time.perf_counter()
            denbora_totala = bukaerako_denbora - hasierako_denbora
            print("\n#{} IRABAZI DUZU {}#".format("-" * (len(MAPA[0]) - 7), "-" * (len(MAPA[0]) - 7)))
            print(f"Labirintoaren irteera topatu duzu {denbora_totala:.2f} segundotan")
            break


def main():
    jolasa()
    while True:
        zer_egin = input("Zer egin nahi duzu, irten (i/I) edo jolasten jarraitu (j/J)?: ")
        system("cls")
        if zer_egin in ["i", "I"]:
            exit()
        elif zer_egin in ["j", "J"]:
            jolasa()
        else:
            print(Style.BRIGHT + Fore.RED + "\nEmandako erantzuna ez da zuzena, saiatu berriro mesedez.",
                  "\nZiurtatu aukeretako bat soilik erantzun izana" + Style.RESET_ALL)


if __name__ == "__main__":
    main()

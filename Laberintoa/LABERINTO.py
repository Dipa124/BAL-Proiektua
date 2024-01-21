import copy
import time
import keyboard
from os import system

class Bloque:
    def __init__(self, textura):
        self.textura = textura

    def posicion(self, mapa):
        for l in mapa:
            for c in l:
                if mapa[mapa.index(l)][l.index(c)] == self.textura:
                    return [mapa.index(l), l.index(c)]


class Jugador:
    def __init__(self, linea, columna, textura):
        self.linea = linea
        self.columna = columna
        self.textura = textura

    def abajo(self):
        self.linea += 1

    def arriba(self):
        self.linea -= 1

    def derecha(self):
        self.columna += 1

    def izquierda(self):
        self.columna -= 1


jugador = Jugador(1, 1, "🔷")
MURO = Bloque("🔳")
SUELO = Bloque("🔲")
META = Bloque("🚩")
MAPA = [["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
        ["🔳", "🔲", "🔲", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔳", "🔲", "🔳", "🔲", "🔳", "🔲", "🔳"],
        ["🔳", "🔲", "🔲", "🔲", "🔲", "🔳", "🔲", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔳", "🔲", "🔳"],
        ["🔳", "🔳", "🔲", "🔳", "🔳", "🔳", "🔲", "🔳", "🔳", "🔳", "🔳", "🔲", "🔳", "🔳", "🔲", "🔳"],
        ["🔳", "🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔳", "🔲", "🔳", "🔲", "🔳", "🔲", "🔲", "🔲", "🔳"],
        ["🔳", "🔲", "🔲", "🔳", "🔲", "🔳", "🔲", "🔲", "🔲", "🔳", "🔲", "🔳", "🔲", "🔳", "🔲", "🔳"],
        ["🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔳", "🔲", "🔳"],
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔲", "🔳"],
        ["🔳", "🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔳", "🔲", "🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔳"],
        ["🔳", "🔳", "🔲", "🔳", "🔲", "🔳", "🔲", "🔲", "🔲", "🔳", "🔲", "🔳", "🔲", "🔳", "🔲", "🔳"],
        ["🔳", "🔲", "🔲", "🔲", "🔲", "🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔳", "🔲", "🔳"],
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔲", "🔳", "🔳", "🔳", "🔳", "🔲", "🔳"],
        ["🔳", "🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔳", "🔲", "🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔳"],
        ["🔳", "🔳", "🚩", "🔳", "🔲", "🔳", "🔲", "🔲", "🔲", "🔳", "🔲", "🔲", "🔲", "🔳", "🔲", "🔳"],
        ["🔳", "🔲", "🔲", "🔲", "🔲", "🔳", "🔲", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔳", "🔲", "🔳"],
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"]]

posicion_meta = META.posicion(MAPA)

def renderizar_mapa(mapa, jugador):
    mapa_actualizado = copy.deepcopy(mapa)
    mapa_actualizado[jugador.linea][jugador.columna] = jugador.textura

    system("cls")
    print("\nX{}MAPA{}X".format("-"*(len(mapa[0])-2), "-"*(len(mapa[0])-2)))
    for l in mapa_actualizado:
        print("|{}|".format("".join(map(str, l))))
    print("X{}X".format("--"*(len(mapa[0]))))


def movimiento(mapa, jugador, muro, evento):
        # ARRIBA
        if evento.name == "flecha arriba" or evento.name == "w":
            if 0 < jugador.linea < len(mapa):
                try:
                    if mapa[jugador.linea - 1][jugador.columna] != muro.textura:
                        jugador.arriba()
                        renderizar_mapa(mapa, jugador)
                except:
                    pass
            else:
                print("No te puedes mover arriba")
        # ABAJO
        elif evento.name == "flecha abajo" or evento.name == "s":
            if 0 <= jugador.linea < len(mapa) - 1:
                try:
                    if mapa[jugador.linea + 1][jugador.columna] != muro.textura:
                        jugador.abajo()
                        renderizar_mapa(mapa, jugador)
                except:
                    pass
            else:
                print("No te puedes mover abajo")
        # DERECHA
        elif evento.name == "flecha derecha" or evento.name == "d":
            if 0 <= jugador.columna < len(mapa[0]) - 1:
                try:
                    if mapa[jugador.linea][jugador.columna + 1] != muro.textura:
                        jugador.derecha()
                        renderizar_mapa(mapa, jugador)
                except:
                    pass
            else:
                print("No te puedes mover a la derecha")
        # IZQUIERDA
        elif evento.name == "flecha izquierda" or evento.name == "a":
            if 0 < jugador.columna < len(mapa[0]):
                try:
                    if mapa[jugador.linea][jugador.columna - 1] != "🔳":
                        jugador.izquierda()
                        renderizar_mapa(mapa, jugador)
                except:
                    pass
            else:
                print("No te puedes mover a la izquierda")


def main():
    renderizar_mapa(MAPA, jugador)
    tiempo_inicio = time.perf_counter()

    while True:
        evento = keyboard.read_event()
        # SALIR
        if evento.name == "esc":
            break
        # MOVIMIENTO
        elif evento.event_type == "down":
            movimiento(MAPA, jugador, MURO, evento)
        if MAPA[jugador.linea][jugador.columna] == META.textura:
            tiempo_final = time.perf_counter()
            tiempo_total = tiempo_final - tiempo_inicio
            print("\n#{} HAS GANADO {}#".format("-" * (len(MAPA[0]) - 6), "-" * (len(MAPA[0]) - 6)))
            print(f"Has completado el nivel en: {tiempo_total:.2f}s")
            break


if __name__ == "__main__":
    main()

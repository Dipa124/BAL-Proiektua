import tkinter as tk

class Laberinto:
    def __init__(self, root, filas=16, columnas=16):
        self.root = root
        self.root.title("Mapa sortzailea")

        self.canvas = tk.Canvas(root, borderwidth=0, highlightthickness=0, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.filas = filas
        self.columnas = columnas

        self.mapa = [["🔳" for _ in range(columnas)] for _ in range(filas)]

        self.inicializar_botones()

        self.horma_activada = True
        self.helmuga_activada = False

        self.dibujar_mapa()

    def inicializar_botones(self):
        self.entry_filas = tk.Entry(self.root, width=5)
        self.entry_filas.insert(0, str(self.filas))
        self.entry_filas.pack(side=tk.LEFT, padx=5)

        self.entry_columnas = tk.Entry(self.root, width=5)
        self.entry_columnas.insert(0, str(self.columnas))
        self.entry_columnas.pack(side=tk.LEFT, padx=5)

        self.boton_actualizar = tk.Button(self.root, text="Actualizar Dimensiones", command=self.actualizar_dimensiones)
        self.boton_actualizar.pack(side=tk.LEFT, padx=5)

        self.boton_horma = tk.Button(self.root, text="Horma", command=self.usar_horma)
        self.boton_horma.pack(side=tk.LEFT, padx=5)

        self.boton_zorua = tk.Button(self.root, text="Zorua", command=self.usar_zorua)
        self.boton_zorua.pack(side=tk.LEFT, padx=5)

        self.boton_helmuga = tk.Button(self.root, text="Helmuga", command=self.poner_helmuga)
        self.boton_helmuga.pack(side=tk.LEFT, padx=5)

        self.boton_esportatu = tk.Button(self.root, text="Esportatu", command=self.exportar_mapa)
        self.boton_esportatu.pack(side=tk.LEFT, padx=5)

        self.canvas.bind("<B1-Motion>", self.pintar_casilla)

    def pintar_casilla(self, event):
        tamano_cuadrado = min(self.canvas.winfo_width() / self.columnas, self.canvas.winfo_height() / self.filas)
        if 0 <= event.x < self.columnas * tamano_cuadrado and 0 <= event.y < self.filas * tamano_cuadrado:
            fila = int(event.y // tamano_cuadrado)
            columna = int(event.x // tamano_cuadrado)

            if self.es_borde(fila, columna):
                return

            if self.helmuga_activada:
                self.mapa[fila][columna] = "🚩"
            elif self.horma_activada:
                self.mapa[fila][columna] = "🔳"
            else:
                self.mapa[fila][columna] = "🔲"

            self.dibujar_mapa()

    def es_borde(self, fila, columna):
        return fila == 0 or fila == self.filas - 1 or columna == 0 or columna == self.columnas - 1

    def usar_horma(self):
        self.horma_activada = True
        self.helmuga_activada = False

    def usar_zorua(self):
        self.horma_activada = False
        self.helmuga_activada = False

    def poner_helmuga(self):
        self.horma_activada = False
        self.helmuga_activada = True

    def dibujar_mapa(self):
        self.canvas.delete("all")

        tamano_cuadrado = min(self.canvas.winfo_width() / self.columnas, self.canvas.winfo_height() / self.filas)

        for fila in range(self.filas):
            for columna in range(self.columnas):
                x1 = columna * tamano_cuadrado
                y1 = fila * tamano_cuadrado
                x2 = x1 + tamano_cuadrado
                y2 = y1 + tamano_cuadrado

                color = "black" if self.mapa[fila][columna] == "🔳" else "white" if self.mapa[fila][columna] != "🚩" else "red"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

                if self.mapa[fila][columna] != "🔳" and not self.helmuga_activada:
                    self.canvas.create_text(x1 + tamano_cuadrado / 2, y1 + tamano_cuadrado / 2,
                                            text=self.mapa[fila][columna], font=("Helvetica", int(tamano_cuadrado / 2)))

    def exportar_mapa(self):
        print("Mapa = [")
        for fila in self.mapa:
            print(f'    {fila},')
        print("]")

    def actualizar_dimensiones(self):
        try:
            nuevas_filas = int(self.entry_filas.get())
            nuevas_columnas = int(self.entry_columnas.get())
            if nuevas_filas > 0 and nuevas_columnas > 0:
                self.filas = nuevas_filas
                self.columnas = nuevas_columnas
                self.mapa = [["🔳" for _ in range(self.columnas)] for _ in range(self.filas)]
                self.dibujar_mapa()
        except ValueError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = Laberinto(root)
    root.mainloop()

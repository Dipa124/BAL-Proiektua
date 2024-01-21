import pygame
import sys

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
CIAN = (0, 255, 255)
VERDE = (0, 255, 0)

# Tamaño del mapa
ANCHO_MAPA = 16
ALTO_MAPA = 16
TAMANO_BLOQUE = 40

# Definir el mapa
MAPA = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Inicializar Pygame
pygame.init()

# Crear la pantalla
ANCHO_PANTALLA = ANCHO_MAPA * TAMANO_BLOQUE
ALTO_PANTALLA = ALTO_MAPA * TAMANO_BLOQUE
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego de Laberinto")

# Coordenadas iniciales del jugador
jugador_x = 1
jugador_y = 1

# Función para dibujar el mapa
def dibujar_mapa():
    for y in range(ALTO_MAPA):
        for x in range(ANCHO_MAPA):
            if MAPA[y][x] == 1:
                pygame.draw.rect(pantalla, NEGRO, (x * TAMANO_BLOQUE, y * TAMANO_BLOQUE, TAMANO_BLOQUE, TAMANO_BLOQUE))
            elif MAPA[y][x] == 2:
                pygame.draw.rect(pantalla, VERDE, (x * TAMANO_BLOQUE, y * TAMANO_BLOQUE, TAMANO_BLOQUE, TAMANO_BLOQUE))


# Función principal del juego
def main():
    global jugador_x, jugador_y

    completado = False  # Variable para verificar si el jugador ha completado el laberinto

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mover al jugador
            if evento.type == pygame.KEYDOWN:
                nueva_x = jugador_x
                nueva_y = jugador_y

                if evento.key == pygame.K_LEFT:
                    nueva_x -= 1
                elif evento.key == pygame.K_RIGHT:
                    nueva_x += 1
                elif evento.key == pygame.K_UP:
                    nueva_y -= 1
                elif evento.key == pygame.K_DOWN:
                    nueva_y += 1

                # Verificar si la nueva posición es válida antes de mover al jugador
                if 0 <= nueva_x < ANCHO_MAPA and 0 <= nueva_y < ALTO_MAPA and (MAPA[nueva_y][nueva_x] == 0 or MAPA[nueva_y][nueva_x] == 2):
                    jugador_x = nueva_x
                    jugador_y = nueva_y

                    # Verificar si el jugador ha llegado a la bandera
                    if MAPA[jugador_y][jugador_x] == 2:
                        completado = True

        # Limpiar la pantalla
        pantalla.fill(BLANCO)

        # Dibujar el mapa
        dibujar_mapa()

        # Dibujar al jugador (un círculo cian)
        pygame.draw.circle(pantalla, CIAN, (jugador_x * TAMANO_BLOQUE + TAMANO_BLOQUE // 2, jugador_y * TAMANO_BLOQUE + TAMANO_BLOQUE // 2), TAMANO_BLOQUE // 2)

        # Mostrar un mensaje de "Completado" si el jugador ha llegado a la bandera
        if completado:
            fuente = pygame.font.Font(None, 36)
            mensaje_completado = fuente.render("Completado", True, VERDE)
            pantalla.blit(mensaje_completado, (ANCHO_PANTALLA // 2 - 80, ALTO_PANTALLA // 2 - 20))

        pygame.display.flip()

if __name__ == "__main__":
    main()

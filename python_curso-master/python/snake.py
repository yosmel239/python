# snake.py
# Juego del gusanito (Snake) utilizando Pygame
# --------------------------------------------------
# Mecánicas:
#  - Movimiento en cuadrícula con flechas
#  - No se puede invertir la dirección de golpe
#  - Crece al comer manzana roja
#  - Termina al chocar contra paredes o su propio cuerpo
#  - Reinicio con la tecla 'R' tras Game Over
# Aspecto:
#  - Fondo negro, gusanito verde, manzana roja
#  - Puntuación en la esquina superior

import pygame
import sys
import random

# ----- CONSTANTES DE CONFIGURACIÓN -----
ANCHO = 600
ALTO = 400
TAM_CELDA = 20                # tamaño de cada cuadrado en la rejilla
FPS = 10                      # velocidad del juego (frames por segundo)

# colores RGB
NEGRO  = (0, 0, 0)
VERDE  = (0, 255, 0)
ROJO   = (255, 0, 0)
BLANCO = (255, 255, 255)

# direcciones
IZQUIERDA = (-1, 0)
DERECHA   = (1, 0)
ARRIBA    = (0, -1)
ABAJO     = (0, 1)

# ----- FUNCIONES AUXILIARES -----
def generar_manzana(snake):
    """Genera una posición aleatoria para la manzana
       que no colisione con el cuerpo de la serpiente."""
    cols = ANCHO // TAM_CELDA
    filas = ALTO // TAM_CELDA
    while True:
        x = random.randrange(cols) * TAM_CELDA
        y = random.randrange(filas) * TAM_CELDA
        if (x, y) not in snake:
            return x, y

def dibujar_texto(superficie, texto, tamaño, color, pos):
    """Dibuja texto en la superficie dada."""
    fuente = pygame.font.SysFont(None, tamaño)
    img = fuente.render(texto, True, color)
    superficie.blit(img, pos)

# ----- CLASE PRINCIPAL DEL JUEGO -----
class SnakeGame:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        """Inicializa o reinicia el estado del juego."""
        centro_x = ANCHO // 2
        centro_y = ALTO // 2
        self.snake = [(centro_x, centro_y)]    # lista de segmentos (x,y)
        self.direccion = DERECHA               # empieza moviendo a la derecha
        self.manzana = generar_manzana(self.snake)
        self.score = 0
        self.game_over = False

    def manejar_eventos(self):
        """Procesa los eventos de teclado."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if not self.game_over:
                    if evento.key == pygame.K_LEFT and self.direccion != DERECHA:
                        self.direccion = IZQUIERDA
                    elif evento.key == pygame.K_RIGHT and self.direccion != IZQUIERDA:
                        self.direccion = DERECHA
                    elif evento.key == pygame.K_UP and self.direccion != ABAJO:
                        self.direccion = ARRIBA
                    elif evento.key == pygame.K_DOWN and self.direccion != ARRIBA:
                        self.direccion = ABAJO
                else:
                    # reiniciar con R
                    if evento.key == pygame.K_r:
                        self.reset()

    def actualizar(self):
        """Actualiza la posición de la serpiente y verifica colisiones."""
        if self.game_over:
            return

        # calcula nueva cabeza
        cabeza_x, cabeza_y = self.snake[0]
        dx, dy = self.direccion
        nueva_cabeza = (cabeza_x + dx * TAM_CELDA,
                        cabeza_y + dy * TAM_CELDA)

        # colisión contra paredes
        if (nueva_cabeza[0] < 0 or nueva_cabeza[0] >= ANCHO or
            nueva_cabeza[1] < 0 or nueva_cabeza[1] >= ALTO):
            self.game_over = True
            return

        # colisión contra el propio cuerpo
        if nueva_cabeza in self.snake:
            self.game_over = True
            return

        # inserta nueva cabeza
        self.snake.insert(0, nueva_cabeza)

        # si come manzana, aumenta puntuación y genera otra
        if nueva_cabeza == self.manzana:
            self.score += 1
            self.manzana = generar_manzana(self.snake)
        else:
            # si no comió, quita la cola (movimiento normal)
            self.snake.pop()

    def dibujar(self):
        """Dibuja todos los elementos en pantalla."""
        self.ventana.fill(NEGRO)

        # serpiente
        for segmento in self.snake:
            pygame.draw.rect(self.ventana, VERDE,
                             pygame.Rect(segmento[0], segmento[1],
                                         TAM_CELDA, TAM_CELDA))

        # manzana
        mx, my = self.manzana
        pygame.draw.rect(self.ventana, ROJO,
                         pygame.Rect(mx, my, TAM_CELDA, TAM_CELDA))

        # puntuación
        dibujar_texto(self.ventana, f"Puntos: {self.score}", 24, BLANCO, (5, 5))

        # mensaje de Game Over
        if self.game_over:
            texto = "GAME OVER - Presiona R para reiniciar"
            ancho_texto = pygame.font.SysFont(None, 36).size(texto)[0]
            dibujar_texto(self.ventana, texto, 36, BLANCO,
                          ((ANCHO - ancho_texto) // 2, ALTO // 2 - 20))

        pygame.display.flip()

    def run(self):
        """Bucle principal del juego."""
        while True:
            self.manejar_eventos()
            self.actualizar()
            self.dibujar()
            self.clock.tick(FPS)

# ----- PUNTO DE ENTRADA -----
if __name__ == "__main__":
    juego = SnakeGame()
    juego.run()
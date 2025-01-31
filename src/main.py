import pygame
from piano import Piano

# Inicializar pygame
pygame.init()

# Configurar pantalla
ANCHO, ALTO = 500, 300
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Piano Virtual")

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
MORADO = (138, 43, 226)  # Color de texto

# Cargar fuente
pygame.font.init()
fuente = pygame.font.Font(None, 80)  # Tamaño de fuente grande

# Crear objeto piano
piano = Piano()

# Diccionario de notas para mostrar en pantalla
notas_texto = {
    "a": "Do",
    "s": "Re",
    "d": "Mi",
    "f": "Fa",
    "g": "Sol",
    "h": "La",
    "j": "Si",
}

# Variable para mostrar la nota presionada
nota_actual = ""
tiempo_nota = 0  # Tiempo que la nota permanecerá en pantalla

# Bucle principal
ejecutando = True
while ejecutando:
    pantalla.fill(BLANCO)  # Limpiar pantalla con color blanco

    # Mostrar la última nota presionada por un corto tiempo
    if nota_actual:
        texto = fuente.render(nota_actual, True, MORADO)
        pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))
        
        # Controlar el tiempo de visualización de la nota
        if pygame.time.get_ticks() - tiempo_nota > 1000:  # 1000 ms = 1 segundo
            nota_actual = ""

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            tecla = evento.unicode
            if tecla in piano.notas:
                piano.play(tecla)
                nota_actual = notas_texto[tecla]  # Actualizar el texto con la nota correspondiente
                tiempo_nota = pygame.time.get_ticks()  # Guardar el tiempo en que se presionó la tecla

    pygame.display.flip()  # Actualizar pantalla

pygame.quit()

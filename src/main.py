import pygame
from piano import Piano

# Crear objeto piano
piano = Piano()

# Configurar pantalla
pygame.init()
pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Piano Virtual")

# Loop principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            piano.play(evento.unicode)

pygame.quit()

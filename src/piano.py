import pygame

class Piano:
    def __init__(self, sound_folder="sounds/"):
        pygame.init()
        self.notas = {
            "a": pygame.mixer.Sound(f"{sound_folder}do.wav"),
            "s": pygame.mixer.Sound(f"{sound_folder}re.wav"),
            "d": pygame.mixer.Sound(f"{sound_folder}mi.wav"),
            "f": pygame.mixer.Sound(f"{sound_folder}fa.wav"),
            "g": pygame.mixer.Sound(f"{sound_folder}sol.wav"),
            "h": pygame.mixer.Sound(f"{sound_folder}la.wav"),
            "j": pygame.mixer.Sound(f"{sound_folder}si.wav"),
        }

    def play(self, key):
        if key in self.notas:
            self.notas[key].play()

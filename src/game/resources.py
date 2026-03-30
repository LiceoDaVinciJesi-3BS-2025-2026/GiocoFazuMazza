import pygame
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent

def get_path(folder, filename):
    path = BASE_PATH / folder / filename
    if not path.exists():
        raise FileNotFoundError(f"File NON trovato: {path}")
    return str(path)

def get_image(filename):
    return pygame.image.load(get_path("images", filename))

def get_sound(filename):
    return pygame.mixer.Sound(get_path("sounds", filename))

def get_music(filename):
    pygame.mixer.music.load(get_path("sounds", filename))
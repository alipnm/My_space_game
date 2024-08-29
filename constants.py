import pygame
pygame.init()
screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
clock = pygame.time.Clock()
FPS = 60
GAME_FONT = pygame.font.Font("assets/game font.otf", 24)
fire_sound = pygame.mixer.Sound("assets/bullet fire.wav")
fire_sound.set_volume(0.1)
score_sound = pygame.mixer.Sound("assets/Score.wav")
live_lose_sound = pygame.mixer.Sound("assets/live lose.mp3")
game_over_sound = pygame.mixer.Sound("assets/game_over.wav")
pygame.mixer.music.load("assets/music.wav")
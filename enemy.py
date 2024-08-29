from random import choice
from pygame.sprite import Sprite
from constants import *
class Enemy(Sprite):
    def __init__(self, x : int, y : int, group : pygame.sprite.Group):
        super().__init__()
        self.image = pygame.image.load("assets/enemy.png")
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = choice([5, 7, 10])
        if self.speed == 5:
            self.hard = 1
        elif self.speed == 7:
            self.hard = 2
        else:
            self.hard = 3
        group.add(self)
    def __str__(self) -> str:
        return "Enemy"
    def update(self):
        self.rect.y += self.speed
        self.mask = pygame.mask.from_surface(self.image)
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()
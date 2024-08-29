from constants import *
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self, x : int, y : int, group : pygame.sprite.Group):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png")
        self.rect = self.image.get_rect(centerx=x, top=y)
        self.mask = pygame.mask.from_surface(self.image)
        group.add(self)
    def __str__(self) -> str:
        return "Bullet -> Player -> spaceship"
    def update(self):
        self.rect.y -= 10
        self.mask = pygame.mask.from_surface(self.image)
        if self.rect.top <= 0:
            self.kill()
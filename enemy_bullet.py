from pygame.sprite import Group
from bullet import Bullet
from constants import *
class EnemyBullet(Bullet):
    def __init__(self, x: int, y: int, group: Group):
        super().__init__(x, y, group)
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect(centerx=x, top=y)
        self.mask = pygame.mask.from_surface(self.image)
    def __str__(self) -> str:
        return "Bullet -> Shooter enemy -> Enemy"
    def update(self):
        self.rect.y += 20
        self.mask = pygame.mask.from_surface(self.image)
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()
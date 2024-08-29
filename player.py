from pygame.sprite import Sprite
from bullet import Bullet
from constants import *
class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect(bottom=SCREEN_HEIGHT, centerx=SCREEN_WIDTH / 2)
        self.mask = pygame.mask.from_surface(self.image)
        self.timer = pygame.time.get_ticks()
    def __str__(self) -> str:
        return "Player -> spaceship"
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
    def fire(self, bullet_group : pygame.sprite.Group):
        if pygame.time.get_ticks() - self.timer >= 500:
            self.timer = pygame.time.get_ticks()
            fire_sound.play()
            Bullet(self.rect.centerx, self.rect.top, bullet_group)
    def draw(self):
        self.mask = pygame.mask.from_surface(self.image)
        screen.blit(self.image, self.rect)
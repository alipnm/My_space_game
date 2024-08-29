from constants import *
from enemy_bullet import EnemyBullet
from enemy import Enemy
class ShooterEnemy(Enemy):
    def __init__(self, x: int, y: int, group: pygame.sprite.Group):
        super().__init__(x, y, group)
        self.image = pygame.image.load("assets/enemy shooter.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5
        self.hard = 10
        self.timer = pygame.time.get_ticks()
    def __str__(self) -> str:
        return "Shooter enemy -> Enemy"
    def fire(self, enemy_bullet_group : pygame.sprite.Group):
        if pygame.time.get_ticks() - self.timer >= 900:
            self.timer = pygame.time.get_ticks()
            fire_sound.play()
            EnemyBullet(self.rect.centerx, self.rect.top, enemy_bullet_group)
    def update(self, score : int, enemy_bullet_group : pygame.sprite.Group):
        self.rect.y += 5
        self.mask = pygame.mask.from_surface(self.image)
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()
            if score > 0:
                score -= 1
        self.fire(enemy_bullet_group)
        return score
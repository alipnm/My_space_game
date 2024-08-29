from os.path import exists
from random import randint
from constants import *
from enemy import Enemy
from player import Player
from shooter_enemy import ShooterEnemy
score = 0
lives = 5
if exists("assets/highscore.txt"):
    with open("assets/highscore.txt", 'r') as f:
        highscore = int(f.read())
else:
    highscore = 0
def starter():
    screen.fill((0,0,0))
    pygame.display.update()
    timer = pygame.time.get_ticks()
    while pygame.time.get_ticks() - timer < 1000:
        screen.fill((0,0,0))
        txt = GAME_FONT.render("The game is started.", True, (255,0,0))
        rct = txt.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
        screen.blit(txt, rct)
        pygame.display.update()
    screen.fill((0,0,0))
    pygame.display.update()
player = Player()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
shooter_enemy_group = pygame.sprite.Group()
shooter_enemy_bullet_group = pygame.sprite.Group()
if randint(1, 2) == 1:
    Enemy(randint(0, 1440), 0, enemy_group)
else:
    ShooterEnemy(randint(0, 1440), 0, shooter_enemy_group)
score_text = GAME_FONT.render(f"Score:{score}", True, (255,0,0))
score_rect = score_text.get_rect(centerx=SCREEN_WIDTH / 4)
lives_text = GAME_FONT.render(f"Lives:{lives}", True, (255,0,0))
lives_rect = lives_text.get_rect(centerx=SCREEN_WIDTH / 4 * 2)
highscore_text = GAME_FONT.render(f"Highscore:{highscore}", True, (255,0,0))
highscore_rect = highscore_text.get_rect(centerx=SCREEN_WIDTH / 4 * 3)
pygame.mixer.music.play(-1)
starter()
def game_over():
    global score, lives, score_text, score_rect, lives_text, lives_rect
    with open("assets/highscore.txt", 'w') as f:
        f.write(str(highscore))
    br = False
    game_over_sound.play()
    score = 0
    lives = 5
    bullet_group.empty()
    enemy_group.empty()
    shooter_enemy_group.empty()
    shooter_enemy_bullet_group.empty()
    player.__init__()
    game_over_text = GAME_FONT.render("""Game over! press 's' to start again. better luck next time.""", True, (255,0,0))
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                elif event.key == pygame.K_s:
                    game_over = False
                    score_text = GAME_FONT.render(f"Score:{score}", True, (255,0,0))
                    score_rect = score_text.get_rect(centerx=SCREEN_WIDTH / 4)
                    lives_text = GAME_FONT.render(f"Lives:{lives}", True, (255,0,0))
                    lives_rect = lives_text.get_rect(centerx=SCREEN_WIDTH / 4 * 2)
                    pygame.mixer.music.play(-1)
                    starter()
                    br = True
        screen.fill((0,0,0))
        if not br:
            game_over_text = GAME_FONT.render("""Game over! press 's' to start again. better luck next time.""", True, (255,0,0))
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
            screen.blit(game_over_text, game_over_rect)
        pygame.display.update()
def check_collisions():
    global score, lives, highscore
    for bullet in bullet_group:
        for enemy in enemy_group:
            if pygame.sprite.collide_mask(bullet, enemy):
                enemy.kill()
                bullet.kill()
                score += enemy.hard
                if score > highscore:
                    highscore = score
                score_sound.play()
        for shooter_enemy in shooter_enemy_group:
            if pygame.sprite.collide_mask(bullet, shooter_enemy):
                shooter_enemy.kill()
                bullet.kill()
                score += shooter_enemy.hard
                if score > highscore:
                    highscore = score
                score_sound.play()
    for shooter_enemy_bullet in shooter_enemy_bullet_group:
        if pygame.sprite.collide_mask(player, shooter_enemy_bullet):
            shooter_enemy_bullet.kill()
            live_lose_sound.play()
            lives -= 1
            if lives == 0:
                game_over()
        for bullet in bullet_group:
            if pygame.sprite.collide_mask(shooter_enemy_bullet, bullet):
                shooter_enemy_bullet.kill()
                bullet.kill()
                score_sound.play()
                score += 1
        for enemy in enemy_group:
            if pygame.sprite.collide_mask(enemy, shooter_enemy_bullet):
                enemy.kill()
                shooter_enemy_bullet.kill()
                score_sound.play()
                score += 1
    for enemy in enemy_group:
        if pygame.sprite.collide_mask(enemy, player):
            enemy.kill()
            live_lose_sound.play()
            lives -= 1
            if lives == 0:
                game_over()
    for shooter_enemy in shooter_enemy_group:
        if pygame.sprite.collide_mask(shooter_enemy, player):
            shooter_enemy.kill()
            live_lose_sound.play()
            lives -= 1
            if lives == 0:
                game_over()
timer = pygame.time.get_ticks()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                with open("assets/highscore.txt", 'w') as f:
                    f.write(str(highscore))
                running = False
    screen.fill((0,0,0))
    check_collisions()
    if pygame.time.get_ticks() - timer >= 900:
        timer = pygame.time.get_ticks()
        if randint(1, 2) == 2:
            Enemy(randint(0, 1440), 0, enemy_group)
        else:
            ShooterEnemy(randint(0, 1440), 0, shooter_enemy_group)
    player.move()
    if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP]:
        player.fire(bullet_group)
    bullet_group.update()
    enemy_group.update()
    for e in shooter_enemy_group:
        score = e.update(score, shooter_enemy_bullet_group)
    shooter_enemy_bullet_group.update()
    score_text = GAME_FONT.render(f"Score:{score}", True, (255,0,0))
    score_rect.centerx = SCREEN_WIDTH / 4
    lives_text = GAME_FONT.render(f"Lives:{lives}", True, (255,0,0))
    lives_rect.centerx = SCREEN_WIDTH / 4 * 2
    highscore_text = GAME_FONT.render(f"Highscore:{highscore}", True, (255,0,0))
    highscore_rect.centerx = SCREEN_WIDTH / 4 * 3
    screen.blit(score_text, score_rect)
    screen.blit(lives_text, lives_rect)
    screen.blit(highscore_text, highscore_rect)
    player.draw()
    bullet_group.draw(screen)
    enemy_group.draw(screen)
    shooter_enemy_group.draw(screen)
    shooter_enemy_bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
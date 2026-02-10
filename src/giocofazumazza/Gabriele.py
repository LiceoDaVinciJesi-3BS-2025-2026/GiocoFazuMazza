import pygame
import random

pygame.init()

# ------------------ COSTANTI ------------------
SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000
FPS = 60

# ------------------ SCHERMO ------------------
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("this game is too MASSIVE")

# ------------------ IMMAGINI ------------------
imgSfondo = pygame.image.load("place.jpg")
imgSfondo = pygame.transform.scale(imgSfondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

imgPlayer = pygame.image.load("Invincible.png")
imgPlayer = pygame.transform.scale(imgPlayer, (40, 40))

imgEnemy = pygame.image.load("Conquest.jpg")
imgEnemy = pygame.transform.scale(imgEnemy, (100, 100))

# ------------------ PLAYER ------------------
player_size = 40
player_rect = pygame.Rect(
    SCREEN_WIDTH // 2,
    SCREEN_HEIGHT // 2,
    player_size,
    player_size
)
player_speed = 8

# ------------------ NEMICI ------------------
enemies = []
enemy_speed = 3

ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 1000)

# ------------------ PROIETTILI NEMICI ------------------
enemy_bullets = []
bullet_size = 10
bullet_speed = 6
shoot_delay = 60
frame_count = 0

# ------------------ CLOCK ------------------
clock = pygame.time.Clock()
running = True

# ================== GAME LOOP ==================
while running:
    clock.tick(FPS)

    # -------- EVENTI --------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == ADD_ENEMY:
            x = random.randint(0, SCREEN_WIDTH - 100)
            y = random.randint(0, SCREEN_HEIGHT // 3)
            enemies.append(pygame.Rect(x, y, 100, 100))

    # -------- INPUT PLAYER --------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < SCREEN_WIDTH:
        player_rect.x += player_speed
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN] and player_rect.bottom < SCREEN_HEIGHT:
        player_rect.y += player_speed

    # -------- SPARO NEMICI --------
    frame_count += 1
    if frame_count >= shoot_delay:
        for enemy in enemies:
            bullet = pygame.Rect(
                enemy.centerx,
                enemy.bottom,
                bullet_size,
                bullet_size
            )
            enemy_bullets.append(bullet)
        frame_count = 0

    # -------- MUOVI PROIETTILI --------
    for bullet in enemy_bullets[:]:
        bullet.y += bullet_speed
        if bullet.top > SCREEN_HEIGHT:
            enemy_bullets.remove(bullet)

        # COLLISIONE PROIETTILE → PLAYER
        if bullet.colliderect(player_rect):
            print("💀 GAME OVER")
            running = False

    # -------- COLLISIONE PLAYER → NEMICI --------
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            print("💀 GAME OVER")
            running = False

    # -------- DISEGNO --------
    screen.blit(imgSfondo, (0, 0))

    screen.blit(imgPlayer, player_rect)

    for enemy in enemies:
        screen.blit(imgEnemy, enemy)

    for bullet in enemy_bullets:
        pygame.draw.rect(screen, (255, 0, 0), bullet)

    pygame.display.flip()

pygame.quit()

        


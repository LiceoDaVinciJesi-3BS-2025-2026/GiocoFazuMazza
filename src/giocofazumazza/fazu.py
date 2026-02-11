import pygame
import random

pygame.init()

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("this game is too MASSIVE")

imgSfondo = pygame.image.load("place.jpg")
imgSfondo = pygame.transform.scale(imgSfondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

imgBees = pygame.image.load("bees.png")
imgBees = pygame.transform.scale(imgBees, (40, 40))

imgConquest = pygame.image.load("Conquest.jpg") 
imgConquest = pygame.transform.scale(imgConquest,(100,100))

ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 1000)

enemies = []
player_bullets = []
enemy_bullets = []

x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2
w, h = 40, 40
speed = 10

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            
            # 🔫 Sparo giocatore con SPAZIO
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(x + w//2 - 5, y, 10, 20)
                player_bullets.append(bullet)

        if event.type == ADD_ENEMY:
            enemy_width = 100
            enemy_height = 100

            posx = random.randint(0, SCREEN_WIDTH - enemy_width)
            side_margin = 300  

            posx = random.randint(side_margin, SCREEN_WIDTH - enemy_width - side_margin)

            posy = random.randint(120, 250)

            enemies.append(pygame.Rect(posx, posy, enemy_width, enemy_height)) 

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - w:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < SCREEN_HEIGHT - h:
        y += speed

    screen.blit(imgSfondo, (0, 0))

    player = pygame.Rect(x, y, w, h)
    screen.blit(imgBees, (x, y))

    # 🔫 Movimento proiettili giocatore
    for bullet in player_bullets[:]:
        bullet.y -= 12
        pygame.draw.rect(screen, (255, 255, 0), bullet)
        if bullet.y < 0:
            player_bullets.remove(bullet)

    # 🔫 Movimento proiettili nemici
    for bullet in enemy_bullets[:]:
        bullet.y += 15
        pygame.draw.rect(screen, (255, 0, 0), bullet)
        if bullet.y > SCREEN_HEIGHT:
            enemy_bullets.remove(bullet)

        if bullet.colliderect(player):
            print("HAI PERSO! COLPITO!")
            running = False

    # 👾 Nemici
    for enemy in enemies[:]:
        screen.blit(imgConquest, (enemy.x, enemy.y))

        # Nemico spara casualmente
        if random.randint(0, 150) < 2:
            bullet = pygame.Rect(enemy.x + 50, enemy.y + 100, 10, 12)
            enemy_bullets.append(bullet)

        # Collisione con proiettili giocatore
        for bullet in player_bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                player_bullets.remove(bullet)
                break

        if player.colliderect(enemy):
            print("HAI PERSO!")
            running = False

    pygame.display.flip()

pygame.quit()
  
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
imgBees = pygame.transform.scale(imgBees, (30, 30))

imgConquest = pygame.image.load("Conquest.jpg") 
imgConquest = pygame.transform.scale(imgConquest,(100,100))

ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 1000)

enemies = []

x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2
w, h = 40, 20
speed = 8

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == ADD_ENEMY:
            posx = random.randint(0, SCREEN_WIDTH - 20)
            posy = random.randint(0, SCREEN_HEIGHT - 20)
            enemies.append((posx, posy))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        w, h = 40, 20
        x -= speed
    if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - w:
        w, h = 40, 20
        x += speed
    if keys[pygame.K_UP] and y > 0:
        w, h = 20, 40
        y -= speed
    if keys[pygame.K_DOWN] and y < SCREEN_HEIGHT - h:
        w, h = 20, 40
        y += speed

    # sfondo
    screen.blit(imgSfondo, (0, 0))

    # player
    player = pygame.Rect(x, y, w, h)
    screen.blit(imgBees, (x, y))

    # nemici (visibili!)
    # nemici con immagine
    for posx, posy in enemies:
        en = screen.blit(imgConquest, (posx, posy))

        if player.colliderect(en):
            print("HAI PERSO!")
            running = False


    pygame.display.flip()

pygame.quit()



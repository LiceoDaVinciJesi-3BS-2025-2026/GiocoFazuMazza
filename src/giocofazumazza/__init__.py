import pygame
import random

pygame.init()

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("this game is too MASSIVE")

imgSfondo = pygame.image.load("place.jpg")
imgSfondo = pygame.transform.scale(imgSfondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

imgInvincible = pygame.image.load("Invincible.png")
imgInvincible = pygame.transform.scale(imgInvincible, (30, 30))

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
    screen.blit(imgInvincible, (x, y))

    # nemici (visibili!)
    # nemici con immagine
    for posx, posy in enemies:
        en = screen.blit(imgConquest, (posx, posy))

        if player.colliderect(en):
            print("HAI PERSO!")
            running = False


    pygame.display.flip()

pygame.quit()



  # cerchio ROSSO di raggio 80 al centro dello screen
    # c è il "rettangolo" che contiene il cerchio disegnato
#    c = pygame.draw.circle(screen, "red", (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), 80)

    # rettangolo BLUE che va dal punto (600,400) lungo 180, largo 100
    # r è il rettangolo che contiene il rettangolo disegnato
#    r = pygame.draw.rect(screen, "blue", (600, 400, 180, 100))

    # linea VERDE dal punto... al punto ... di spessore ...
    # l è il "rettangolo" che contiene la linea disegnata 
#    l = pygame.draw.line(screen, "green", (600, 100), (700, 300), 8)

    # ellisse VIOLA contenuto nel rettangolo che parte da (100,400) lungo 60, largo 90. Di spessore...
    # el è il rettangolo che contiene l'ellisse disegnata
#    el = pygame.draw.ellipse(screen, "purple" , (100, 400, 60, 90), 8)

    # poligono GIALLO (riempito) che collega i punti...
    # pol è il rettangolo che contiene il poligono disegnato
#    pol = pygame.draw.polygon(screen, "yellow",((146, 0), (291, 106),(236, 277), (56, 277), (0, 106)))


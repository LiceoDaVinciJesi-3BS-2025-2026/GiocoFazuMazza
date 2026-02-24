
import pygame
import random

# -------------------------------------------------------------------------------------------------------------- #
# ------------------------------------- LEVEL 3 ---------------------------------------------------------------- #

def level3():
    imgSpazio = pygame.image.load("spazio.jpg")
    imgSpazio = pygame.transform.scale(imgSpazio, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    imgBees = pygame.image.load("bees.png")
    imgBees = pygame.transform.scale(imgBees, (45, 45))

    imgThrugg = pygame.image.load("thrugg.png")
    imgThrugg = pygame.transform.scale(imgThrugg, (250, 250))
    
    ADD_ENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_ENEMY, 1000)
    
    #Thrugg
    thrugg_x = SCREEN_WIDTH // 2 - imgThrugg.get_width() // 2
    thrugg_y = 50
    thrugg_speed = 15
    thrugg_direction = 1  # 1 = destra, -1 = sinistra
    thruggBullets = []
    clock = pygame.time.Clock()
    running = True 
    
    enemies = []
    player_bullets = []
    enemy_bullets = []

    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    w, h = 40, 40
    speed = 10   

    clock = pygame.time.Clock()
    running = True
    x = SCREEN_WIDTH // 2 - imgThrugg.get_width() // 2
    y = 50
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #Thrugg si muove
        thrugg_x += thrugg_direction * thrugg_speed
        if thrugg_x <= 0:
            thrugg_x = 0
            thrugg_direction *= -1
        
        if thrugg_x + imgThrugg.get_width() >= SCREEN_WIDTH:
            thrugg_x = SCREEN_WIDTH - imgThrugg.get_width()
            thrugg_direction *= -1
        screen.blit(imgSpazio, (0, 0))
        screen.blit(imgThrugg, (thrugg_x, thrugg_y))
        pygame.display.flip()
        
        #Thrugg spara
        if random.randint(0, 50) < 5:   
            bullet = pygame.Rect(
                thrugg_x + imgThrugg.get_width() // 2 - 5,
                thrugg_y + imgThrugg.get_height(),
                10, 20
            )
            thruggBullets.append(bullet)
        
        for bullet in thruggBullets:
            bullet.y += 10
        thruggBullets = [b for b in thruggBullets if b.y < SCREEN_HEIGHT]

                # 🔫 Sparo giocatore con SPAZIO
                # if event.key == pygame.K_SPACE:
                    #bullet = pygame.Rect(x + w//2 - 5, y, 10, 20)
                    #player_bullets.append(bullet)
    running = True
    while running:
        #screen.blit(imgSpazio, (0, 0))
        screen.blit(imgThrugg, (thrugg_x, thrugg_y))
        for bullet in thruggBullets:
            pygame.draw.rect(screen, (255, 255, 0), bullet)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                    
# -------------------------------------------------------------------------------------------------------------- #
# ------------------------------------- HOME ------------------------------------------------------------------- #
def home_screen():
    font = pygame.font.SysFont("comicsansms", 100)
    small_font = pygame.font.SysFont("comicsansms", 60)

    while True:
        screen.fill((20, 20, 30))

        title = font.render("THIS GAME IS TOO MASSIVE", True, (255, 255, 0))
        level3_text = small_font.render("Premi 3 per Livello 3", True, (255, 255, 255))
        quit_text = small_font.render("Premi ESC per uscire", True, (200, 200, 200))

        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 200))
        screen.blit(level3_text, (SCREEN_WIDTH//2 - level3_text.get_width()//2, 500))
        screen.blit(quit_text, (SCREEN_WIDTH//2 - quit_text.get_width()//2, 600))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    level3()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()


# -------------------------------------------------------------------------------------------------------------- #
# ------------------------------------- MAIN ------------------------------------------------------------------- #
def main():

    pygame.init()

    SCREEN_WIDTH = 1900
    SCREEN_HEIGHT = 1000

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("this game is too MASSIVE")

    home_screen()   # ← IMPORTANTE


# -------------------------------------------------------------------------------------------------------------- #
# ------------------------------------- EXE -------------------------------------------------------------------- #
if __name__ == "__main__":
    main()
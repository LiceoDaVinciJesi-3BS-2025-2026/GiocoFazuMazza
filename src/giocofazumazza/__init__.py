
import pygame
import random
# -------------------------------------------------------------------------------------------------------------- #
# ------------------------------------- MAIN ------------------------------------------------------------------- #
def main():

    pygame.init()

    SCREEN_WIDTH = 1900
    SCREEN_HEIGHT = 1000

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("this game is too MASSIVE")

    home_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
# -------------------------------------------------------------------------------------------------------------- #
# ------------------------------------- HOME ------------------------------------------------------------------- #
def home_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
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
                    level3(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
# -------------------------------------------------------------------------------------------------------------- #
# ------------------------------------- LEVEL 3 ---------------------------------------------------------------- #

def level3(screen, SCREEN_WIDTH, SCREEN_HEIGHT):

    imgSpazio = pygame.image.load("spazio.jpg")
    imgSpazio = pygame.transform.scale(imgSpazio, (SCREEN_WIDTH, SCREEN_HEIGHT))

    imgThrugg = pygame.image.load("Thrugg.png")
    imgThrugg = pygame.transform.scale(imgThrugg, (250, 250))

    thrugg_x = SCREEN_WIDTH // 2 - imgThrugg.get_width() // 2
    thrugg_y = 50
    thrugg_speed = 15
    thrugg_direction = 1

    thruggBullets = []

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Movimento
        thrugg_x += thrugg_direction * thrugg_speed
        if thrugg_x <= 0 or thrugg_x + imgThrugg.get_width() >= SCREEN_WIDTH:
            thrugg_direction *= -1

        # Sparo
        if random.randint(0, 10) < 5:
            bullet = pygame.Rect(
                thrugg_x + imgThrugg.get_width() // 2 - 5,
                thrugg_y + imgThrugg.get_height(),
                10, 20
            )
            thruggBullets.append(bullet)

        # Movimento proiettili
        for bullet in thruggBullets:
            bullet.y += 10

        thruggBullets = [b for b in thruggBullets if b.y < SCREEN_HEIGHT]

        # Disegno
        screen.blit(imgSpazio, (0, 0))
        screen.blit(imgThrugg, (thrugg_x, thrugg_y))

        for bullet in thruggBullets:
            pygame.draw.rect(screen, (255, 255, 0), bullet)

        pygame.display.flip()
# -------------------------------------------------------------------------------------------------------------- #
# ------------------------------------- EXE -------------------------------------------------------------------- #
if __name__ == "__main__":
    main()
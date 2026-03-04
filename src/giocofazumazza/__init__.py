import pygame
import random

# -------------------------------------------------------------------------------------------------------------- #
# ------------------------------------- MAIN ------------------------------------------------------------------- #
def main():

    pygame.init()

    SCREEN_WIDTH = 1300     #1900
    SCREEN_HEIGHT = 760    #1000

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

# ------------------------------------- LEVEL 3 ---------------------------------------------------------------- #

def level3(screen, SCREEN_WIDTH, SCREEN_HEIGHT):

    imgSpazio = pygame.image.load("spazio.jpg")
    imgSpazio = pygame.transform.scale(imgSpazio, (SCREEN_WIDTH, SCREEN_HEIGHT))

    imgThrugg = pygame.image.load("Thrugg.png")
    imgThrugg = pygame.transform.scale(imgThrugg, (250, 250))
    
    imgBees = pygame.image.load("bees.png")
    imgBees = pygame.transform.scale(imgBees, (60, 60))

    # -------------------- PLAYER & BOSS STATS --------------------
    bees_max_life = 50
    bees_life = bees_max_life
    thrugg_max_life = 100
    thrugg_life = thrugg_max_life

    heal_amount = 8

    # -------------------- movimento personaggi --------------------
    thrugg_x = SCREEN_WIDTH // 2 - imgThrugg.get_width() // 2
    thrugg_y = 50
    thrugg_speed = 5
    thrugg_direction = 1

    bees_x = SCREEN_WIDTH // 2
    bees_y = SCREEN_HEIGHT - 150
    bees_speed = 8

    # -------------------- proiettili personaggi --------------------
    player_bullets = []
    thruggBullets = []
    boss_bullet_speed = 400

    boss_shoot_delay = 130
    boss_last_shot = 0

    # -------------------- POWERUPS --------------------
    powerups = []
    double_shot = False
    double_timer = 0

    shield_active = False
    shield_timer = 0
    
    heal_active = False
    heal_timer = 0
    # -------------------- UTILS --------------------
    font_life = pygame.font.SysFont("comicsansms", 40)
    clock = pygame.time.Clock()
    running = True

#--------------------------------gioco--------------------------------------#
    
    while running:
        delta_time = clock.tick(60) / 1000
        current_time = pygame.time.get_ticks()

        # -------------------- EVENTS --------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_SPACE:
                    if double_shot:
                        bullet1 = pygame.Rect(bees_x + 10, bees_y, 10, 20)
                        bullet2 = pygame.Rect(bees_x + imgBees.get_width() - 20, bees_y, 10, 20)
                        player_bullets.extend([bullet1, bullet2])
                    else:
                        bullet = pygame.Rect(
                            bees_x + imgBees.get_width() // 2 - 5,
                            bees_y,
                            10,
                            20
                        )
                        player_bullets.append(bullet)

        # -------------------- PLAYER MOVEMENT --------------------
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and bees_x > 0:
            bees_x -= bees_speed
        if keys[pygame.K_RIGHT] and bees_x < SCREEN_WIDTH - imgBees.get_width():
            bees_x += bees_speed
        if keys[pygame.K_UP] and bees_y > 0:
            bees_y -= bees_speed
        if keys[pygame.K_DOWN] and bees_y < SCREEN_HEIGHT - imgBees.get_height():
            bees_y += bees_speed

        bees_rect = pygame.Rect(bees_x, bees_y, imgBees.get_width(), imgBees.get_height())

        # -------------------- BOSS MOVEMENT --------------------
        thrugg_x += thrugg_direction * thrugg_speed
        if thrugg_x <= 0 or thrugg_x + imgThrugg.get_width() >= SCREEN_WIDTH:
            thrugg_direction *= -1

        thrugg_rect = pygame.Rect(thrugg_x, thrugg_y, imgThrugg.get_width(), imgThrugg.get_height())

        # -------------------- PLAYER BULLETS --------------------
        for bullet in player_bullets[:]:
            bullet.y -= 600 * delta_time

            if thrugg_rect.colliderect(bullet):
                thrugg_life -= 1
                player_bullets.remove(bullet)

            elif bullet.y < 0:
                player_bullets.remove(bullet)

        # -------------------- BOSS SHOOT --------------------
        if current_time - boss_last_shot > boss_shoot_delay:
            bullet_rect = pygame.Rect(
                thrugg_x + imgThrugg.get_width() // 2 - 5,
                thrugg_y + imgThrugg.get_height(),
                10,
                20
            )

            thruggBullets.append({
                "rect": bullet_rect,
                "y": float(bullet_rect.y)
            })

            boss_last_shot = current_time

        # -------------------- BOSS BULLETS --------------------
        new_bullets = []

        for bullet in thruggBullets:
            bullet["y"] += boss_bullet_speed * delta_time
            bullet["rect"].y = int(bullet["y"])

            if bees_rect.colliderect(bullet["rect"]):
                if not shield_active:
                    bees_life = max(0, bees_life - 5)
            elif bullet["rect"].y < SCREEN_HEIGHT:
                new_bullets.append(bullet)

        thruggBullets = new_bullets

    # -------------------- POWERUP SPAWN --------------------
        if random.randint(0, 190) == 0:
            power_type = random.choice(["double", "shield", "heal"])
            power_rect = pygame.Rect(random.randint(50, SCREEN_WIDTH - 50), 0, 40, 40)
            powerups.append({"rect": power_rect, "type": power_type})

    # -------------------- durata power up in game --------------------
        if double_shot and current_time - double_timer > 5000:
            double_shot = False

        if shield_active and current_time - shield_timer > 7000:
            shield_active = False
        
        if heal_active and current_time - heal_timer > 3000:
            heal_active = False

# -------------------- disegno --------------------------------------------#
        screen.blit(imgSpazio, (0, 0))
        screen.blit(imgThrugg, (thrugg_x, thrugg_y))
        screen.blit(imgBees, (bees_x, bees_y))
        
        # Mark con scudo attivo...che forza 
        if shield_active:
            center = (
                bees_x + imgBees.get_width() // 2,
                bees_y + imgBees.get_height() // 2
            )

            # cerchio esterno trasparente (glow)
            pygame.draw.circle(screen, (0, 255, 255), center, imgBees.get_width() + 5, 2)
            pygame.draw.circle(screen, (0, 200, 255), center, imgBees.get_width(), 10)
        
        # Boss life bar
        boss_ratio = thrugg_life / thrugg_max_life
        pygame.draw.rect(screen, (120, 0, 0), (SCREEN_WIDTH//2 - 300, 20, 600, 40))
        pygame.draw.rect(screen, (255, 0, 0), (SCREEN_WIDTH//2 - 300, 20, 600 * boss_ratio, 40))
        pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH//2 - 300, 20, 600, 40), 4)

        # Player life bar
        life_ratio = bees_life / bees_max_life
        pygame.draw.rect(screen, (100, 0, 0), (50, 50, 300, 30))
        pygame.draw.rect(screen, (0, 255, 0), (50, 50, 300 * life_ratio, 30))
        pygame.draw.rect(screen, (255, 255, 255), (50, 50, 300, 30), 3)

        # Draw bullets
        for bullet in player_bullets:
            pygame.draw.rect(screen, (255, 255, 0), bullet)

        for bullet in thruggBullets:
            pygame.draw.rect(screen, (255, 0, 0), bullet["rect"])

        # Power up
        new_powerups = []

        for power in powerups:
            power["rect"].y += 5

            if bees_rect.colliderect(power["rect"]):

                if power["type"] == "double":
                    double_shot = True
                    double_timer = pygame.time.get_ticks()

                elif power["type"] == "shield":
                    shield_active = True
                    shield_timer = pygame.time.get_ticks()

                elif power["type"] == "heal":
                    bees_life = min(bees_max_life, bees_life + heal_amount)

            else:
                if power["rect"].y < SCREEN_HEIGHT:
                    new_powerups.append(power)

            # Disegno powerup
            if power["type"] == "double":
                color = (200, 0, 255)
            elif power["type"] == "shield":
                color = (0, 255, 255)
            elif power["type"] == "heal":
                color = (0, 255, 0)

            pygame.draw.rect(screen, color, power["rect"])

        powerups = new_powerups
                    
        if bees_life <= 0:
            print("GAME OVER")
            running = False

        if thrugg_life <= 0:
            print("YOU WIN!")
            running = False

        pygame.display.flip()
# -------------------------------------------------------------------------------------------------------------- #
# ------------------------------------- EXE -------------------------------------------------------------------- #
if __name__ == "__main__":
    main()
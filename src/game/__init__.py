import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("this game is too MASSIVE")

clock = pygame.time.Clock()

# --------------------- HOME ---------------------
def home_screen():
    font = pygame.font.SysFont("comicsansms", 100)
    small_font = pygame.font.SysFont("comicsansms", 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    level1()
                if event.key == pygame.K_2:
                    level2()
                if event.key == pygame.K_3:
                    level3()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill((20, 20, 30))

        title = font.render("THIS GAME IS TOO MASSIVE", True, (255, 255, 0))
        level1_text = small_font.render("Press 1 for Level 1", True, (255, 255, 255))
        level2_text = small_font.render("Press 2 for Level 2", True, (255, 255, 255))
        level3_text = small_font.render("Press 3 for Level 3", True, (255, 255, 255))
        quit_text = small_font.render("Press ESC to quit", True, (200, 200, 200))

        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 200))
        screen.blit(level1_text, (SCREEN_WIDTH // 2 - level1_text.get_width() // 2, 500))
        screen.blit(level2_text, (SCREEN_WIDTH // 2 - level2_text.get_width() // 2, 550))
        screen.blit(level3_text, (SCREEN_WIDTH // 2 - level3_text.get_width() // 2, 600))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 650))

        pygame.display.flip()
        clock.tick(60)

# --------------------- LIVELLO 1 ---------------------
def level1():
    pygame.mixer.music.load("mega.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    lose_sound = pygame.mixer.Sound("CECIL.mp3")
    lose_sound.set_volume(0.7)

    imgSfondo = pygame.image.load("place.jpg")
    imgSfondo = pygame.transform.scale(imgSfondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

    imgBees = pygame.image.load("bees.png")
    imgBees = pygame.transform.scale(imgBees, (40, 40))

    imgConquest = pygame.image.load("Conquest.png")
    imgConquest = pygame.transform.scale(imgConquest, (100, 100))

    ADD_ENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_ENEMY, 1000)

    enemies = []
    player_bullets = []
    enemy_bullets = []

    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    w, h = 40, 40
    speed = 10

    punti = 0
    running = True
    font = pygame.font.SysFont("comicsansms", 32)

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.pause()
                    running = False

                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(x + w // 2 - 5, y, 10, 20)
                    player_bullets.append(bullet)

            if event.type == ADD_ENEMY:
                posx = random.randint(300, SCREEN_WIDTH - 300)
                posy = random.randint(120, 250)
                enemies.append(pygame.Rect(posx, posy, 100, 100))

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

        for bullet in player_bullets[:]:
            bullet.y -= 12
            pygame.draw.rect(screen, (255, 255, 0), bullet)
            if bullet.y < 0:
                player_bullets.remove(bullet)

        for bullet in enemy_bullets[:]:
            bullet.y += 15
            pygame.draw.rect(screen, (255, 255, 255), bullet)
            if bullet.y > SCREEN_HEIGHT:
                enemy_bullets.remove(bullet)

            if bullet.colliderect(player):
                testo_sconfitta = font.render("YOU LOST", True, (255, 0, 0))
                screen.blit(testo_sconfitta, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
                pygame.display.flip()
                lose_sound.play()
                pygame.mixer.music.pause()
                pygame.time.delay(5000)
                running = False

        for enemy in enemies[:]:
            screen.blit(imgConquest, (enemy.x, enemy.y))

            if random.randint(0, 150) < 2:
                bullet = pygame.Rect(enemy.x + 50, enemy.y + 100, 10, 12)
                enemy_bullets.append(bullet)

            for bullet in player_bullets[:]:
                if enemy.colliderect(bullet):
                    enemies.remove(enemy)
                    player_bullets.remove(bullet)
                    punti += 100
                    break

            if player.colliderect(enemy):
                testo_sconfitta = font.render("YOU LOST", True, (255, 0, 0))
                screen.blit(testo_sconfitta, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
                pygame.display.flip()
                pygame.mixer.music.pause()
                lose_sound.play()
                pygame.time.delay(5000)
                running = False

        testo_punti = font.render("Punti: " + str(punti), True, (255, 0, 0))
        screen.blit(testo_punti, (SCREEN_WIDTH - 250, 20))

        pygame.display.flip()

        if punti >= 2000:
            testo_vittoria = font.render("YOU WON", True, (255, 255, 0))
            screen.blit(testo_vittoria, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.mixer.music.pause()
            pygame.time.delay(3000)
            running = False

    pygame.time.set_timer(ADD_ENEMY, 0)

# --------------------- LEVEL 2 ---------------------
def level2():
    pygame.mixer.music.load("collapse.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    pretty_sound = pygame.mixer.Sound("pretty.mp3")
    pretty_sound.set_volume(0.7)

    sure_sound = pygame.mixer.Sound("sure.mp3")
    sure_sound.set_volume(0.7)

    stake_sound = pygame.mixer.Sound("stake.mp3")
    stake_sound.set_volume(0.7)

    screen_shake = 0
    flash_alpha = 0
    flash_color = (255, 0, 0)
    floating_texts = []

    hp_1 = 200
    difesa_1 = 10
    attack_1 = 50

    hp_2 = 600
    difesa_2 = 5
    attack_2 = 30

    invincible_x = 300
    omniman_x = 800

    animating = False
    animating2 = False
    animation_target = None
    animation_target2 = None
    animation_speed = 20

    invincible_img = pygame.image.load("invincible.png").convert_alpha()
    omniman_img = pygame.image.load("omniman.png").convert_alpha()

    invincible_img = pygame.transform.scale(invincible_img, (300, 350))
    omniman_img = pygame.transform.scale(omniman_img, (400, 400))

    player_acted = False
    doge = False
    battle_message = ""
    battle_message2 = ""

    font = pygame.font.SysFont("comicsansms", 32)
    small_font = pygame.font.SysFont("arial", 18)
    message_font = pygame.font.SysFont("arial", 22)
    dmg_font = pygame.font.SysFont("arial", 28, bold=True)

    def add_floating_text(text, x, y, color=(255, 50, 50)):
        floating_texts.append({
            "text": text,
            "x": x,
            "y": y,
            "alpha": 255,
            "color": color
        })

    def draw_fight_screen():
        nonlocal flash_alpha, screen_shake

        offset_x = random.randint(-screen_shake, screen_shake) if screen_shake > 0 else 0
        offset_y = random.randint(-screen_shake, screen_shake) if screen_shake > 0 else 0

        screen.fill((255, 255, 255))

        screen.blit(invincible_img, (invincible_x + offset_x, 120 + offset_y))
        screen.blit(omniman_img, (omniman_x + offset_x, 0 + offset_y))

        if battle_message:
            text = message_font.render(battle_message, True, (0, 0, 0))
            screen.blit(text, (550, 530))

        if battle_message2:
            text = message_font.render(battle_message2, True, (0, 0, 0))
            screen.blit(text, (550, 600))

        pygame.draw.rect(screen, (0, 0, 0), (1100, 50, 300, 100), 3)
        name_text = font.render("Omni Man", True, (0, 0, 0))
        screen.blit(name_text, (1110, 60))

        hp_bar_width = int((hp_2 / 600) * 200)
        pygame.draw.rect(screen, (255, 0, 0), (1110, 100, max(0, hp_bar_width), 20))

        pygame.draw.rect(screen, (0, 0, 0), (50, 300, 300, 100), 3)
        player_text = font.render("Invincible", True, (0, 0, 0))
        screen.blit(player_text, (60, 310))

        hp_bar_width_player = int((hp_1 / 200) * 200)
        pygame.draw.rect(screen, (0, 255, 0), (60, 350, max(0, hp_bar_width_player), 20))

        pygame.draw.rect(screen, (0, 0, 0), (0, 500, 1500, 250), 3)

        move1 = small_font.render("1 - Attack", True, (0, 0, 0))
        move2 = small_font.render("2 - Dodge", True, (0, 0, 0))
        move3 = small_font.render("3 - Defence", True, (0, 0, 0))
        move4 = small_font.render("4 - Special", True, (0, 0, 0))

        screen.blit(move1, (50, 580))
        screen.blit(move2, (50, 680))
        screen.blit(move3, (300, 580))
        screen.blit(move4, (300, 680))

        if flash_alpha > 0:
            flash_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            flash_surf.fill((*flash_color, int(flash_alpha)))
            screen.blit(flash_surf, (0, 0))
            flash_alpha = max(0, flash_alpha - 15)

        for ft in floating_texts[:]:
            surf = dmg_font.render(ft["text"], True, ft["color"])
            surf.set_alpha(ft["alpha"])
            screen.blit(surf, (ft["x"], ft["y"]))
            ft["y"] -= 2
            ft["alpha"] -= 6
            if ft["alpha"] <= 0:
                floating_texts.remove(ft)

        if screen_shake > 0:
            screen_shake -= 1

        pygame.display.flip()

    def turn_bot():
        nonlocal hp_2, hp_1, difesa_2, difesa_1, doge, battle_message2
        nonlocal animating2, animation_target2, screen_shake, flash_alpha, flash_color

        move = random.randint(1, 4)

        if move == 1:
            difesa_2 = 20
            battle_message2 = "Omniman used DEFENCE! He takes less damage this turn."

        elif move == 2:
            if not doge:
                animating2 = True
                sure_sound.play()
                animation_target2 = "bot_attack"
                critico = random.randint(1, 100)
                if critico <= 10:
                    danno = attack_2 * 2 - difesa_1
                    hp_1 -= danno
                    battle_message2 = f"OMNIMAN CRITICAL! You took {danno} damage, {hp_1} hp left"
                    screen_shake = 15
                    flash_color = (200, 0, 0)
                    flash_alpha = 180
                    add_floating_text(f"CRIT! -{danno}", invincible_x, 100, color=(220, 0, 0))
                else:
                    danno = attack_2 - difesa_1
                    hp_1 -= danno
                    battle_message2 = f"Omniman attacks! You took {danno} damage, {hp_1} hp left"
                    screen_shake = 10
                    flash_color = (200, 0, 0)
                    flash_alpha = 150
                    add_floating_text(f"-{danno}", invincible_x, 100, color=(220, 0, 0))
            else:
                battle_message2 = "Omniman tried to attack, but you dodged!"

        elif move == 3:
            hp_2 += 20
            battle_message2 = f"Omniman healed 20 HP! {hp_2} hp remaining."

        elif move == 4:
            if not doge:
                animating2 = True
                sure_sound.play()
                animation_target2 = "bot_attack"
                dmg = random.randint(30, 90)
                danno = dmg - difesa_1
                hp_1 -= danno
                battle_message2 = f"OMNIMAN SPECIAL! You took {danno} damage, {hp_1} hp left"
                screen_shake = 12
                flash_color = (200, 0, 0)
                flash_alpha = 160
                add_floating_text(f"SPECIAL! -{danno}", invincible_x, 100, color=(220, 0, 0))
            else:
                battle_message2 = "Omniman tried to use Special, but you dodged!"

        doge = False
        difesa_1 = 10

    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.pause()
                    running = False

                if not player_acted:
                    if event.key == pygame.K_1:
                        animating = True
                        animation_target = "player_attack"
                        critico = random.randint(1, 100)
                        if critico <= 10:
                            damage = (attack_1 * 2) - difesa_2
                            hp_2 -= damage
                            battle_message = f"CRITICAL! You did {damage} damage, {hp_2} hp left for Omniman"
                            screen_shake = 15
                            flash_color = (255, 0, 0)
                            flash_alpha = 180
                            add_floating_text(f"CRIT! -{damage}", omniman_x + 50, 60, color=(255, 0, 0))
                        else:
                            damage = attack_1 - difesa_2
                            hp_2 -= damage
                            battle_message = f"Invincible attacks! {damage} damage, {hp_2} hp left for Omniman"
                            screen_shake = 8
                            flash_color = (255, 100, 0)
                            flash_alpha = 120
                            add_floating_text(f"-{damage}", omniman_x + 100, 80, color=(255, 60, 0))
                        difesa_2 = 5
                        player_acted = True

                    elif event.key == pygame.K_2:
                        valore = random.randint(1, 50)
                        if valore >= 25:
                            doge = True
                            battle_message = "YOU USED DODGE AND SUCCEEDED!"
                        else:
                            doge = False
                            battle_message = "YOU USED DODGE BUT FAILED!"
                        player_acted = True
                        difesa_2 = 5

                    elif event.key == pygame.K_3:
                        difesa_1 = 20
                        battle_message = "YOU USED DEFENCE! -10 damage taken this turn!"
                        player_acted = True
                        difesa_2 = 5

                    elif event.key == pygame.K_4:
                        animating = True
                        animation_target = "player_attack"
                        numero = random.randint(20, 110)
                        danno = numero - difesa_2
                        hp_2 -= danno
                        battle_message = f"SPECIAL ATTACK! {danno} damage, {hp_2} hp left for Omniman"
                        screen_shake = 15
                        flash_color = (255, 0, 0)
                        flash_alpha = 180
                        add_floating_text(f"SPECIAL! -{danno}", omniman_x + 50, 60, color=(255, 0, 0))
                        player_acted = True
                        difesa_2 = 5

        # Animazione attacco giocatore
        if animating:
            if animation_target == "player_attack":
                if invincible_x < omniman_x - 100:
                    invincible_x += animation_speed
                else:
                    invincible_x = 300
                    animating = False

        # Animazione attacco bot
        if animating2:
            if animation_target2 == "bot_attack":
                if omniman_x > invincible_x + 100:
                    omniman_x -= animation_speed
                else:
                    omniman_x = 800
                    animating2 = False

        draw_fight_screen()

        # Controlla vittoria/sconfitta
        if hp_2 <= 0:
            testo_vittoria = font.render("YOU WON", True, (255, 255, 0))
            screen.blit(testo_vittoria, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pretty_sound.play()
            pygame.mixer.music.pause()
            pygame.time.delay(3000)
            running = False

        if hp_1 <= 0:
            testo_sconfitta = font.render("YOU LOST", True, (255, 0, 0))
            screen.blit(testo_sconfitta, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            stake_sound.play()
            pygame.mixer.music.pause()
            pygame.time.delay(5000)
            running = False

        # Turno del bot dopo che il giocatore ha agito
        if player_acted and not animating:
            pygame.time.delay(500)
            turn_bot()
            player_acted = False

# --------------------- LEVEL 3 ---------------------
def level3():
    font = pygame.font.SysFont("comicsansms", 100)

    pygame.mixer.music.load("Finale.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    shoot_sound = pygame.mixer.Sound("job.mpeg")
    shoot_sound.set_volume(0.7)

    imgSpazio = pygame.image.load("spazio.jpg")
    imgSpazio = pygame.transform.scale(imgSpazio, (SCREEN_WIDTH, SCREEN_HEIGHT))

    imgThrugg = pygame.image.load("Thrugg.png")
    imgThrugg = pygame.transform.scale(imgThrugg, (250, 250))

    imgBees = pygame.image.load("bees.png")
    imgBees = pygame.transform.scale(imgBees, (60, 60))

    bees_max_life = 50
    bees_life = bees_max_life
    thrugg_max_life = 500
    thrugg_life = thrugg_max_life

    heal_amount = 8

    thrugg_x = SCREEN_WIDTH // 2 - imgThrugg.get_width() // 2
    thrugg_y = 50
    thrugg_speed = 5
    thrugg_direction = 1

    bees_x = SCREEN_WIDTH // 2
    bees_y = SCREEN_HEIGHT - 150
    bees_speed = 8

    player_bullets = []
    thruggBullets = []
    boss_bullet_speed = 400

    boss_shoot_delay = 130
    boss_last_shot = 0

    powerups = []
    double_shot = False
    double_timer = 0

    shield_active = False
    shield_timer = 0

    running = True

    while running:
        delta_time = clock.tick(60) / 1000
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.pause()
                    running = False

                if event.key == pygame.K_SPACE:
                    shoot_sound.play()
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

        thrugg_x += thrugg_direction * thrugg_speed
        if thrugg_x <= 0 or thrugg_x + imgThrugg.get_width() >= SCREEN_WIDTH:
            thrugg_direction *= -1

        thrugg_rect = pygame.Rect(thrugg_x, thrugg_y, imgThrugg.get_width(), imgThrugg.get_height())

        for bullet in player_bullets[:]:
            bullet.y -= int(600 * delta_time)

            if thrugg_rect.colliderect(bullet):
                thrugg_life -= 1
                player_bullets.remove(bullet)
            elif bullet.y < 0:
                player_bullets.remove(bullet)

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

        if random.randint(0, 190) == 0:
            power_type = random.choice(["double", "shield", "heal"])
            power_rect = pygame.Rect(random.randint(50, SCREEN_WIDTH - 50), 0, 40, 40)
            powerups.append({"rect": power_rect, "type": power_type})

        if double_shot and current_time - double_timer > 5000:
            double_shot = False

        if shield_active and current_time - shield_timer > 7000:
            shield_active = False

        # Disegno
        screen.blit(imgSpazio, (0, 0))
        screen.blit(imgThrugg, (thrugg_x, thrugg_y))
        screen.blit(imgBees, (bees_x, bees_y))

        if shield_active:
            center = (
                bees_x + imgBees.get_width() // 2,
                bees_y + imgBees.get_height() // 2
            )
            pygame.draw.circle(screen, (0, 255, 255), center, imgBees.get_width() + 5, 2)
            pygame.draw.circle(screen, (0, 200, 255), center, imgBees.get_width(), 10)

        boss_ratio = thrugg_life / thrugg_max_life
        pygame.draw.rect(screen, (120, 0, 0), (SCREEN_WIDTH // 2 - 300, 20, 600, 40))
        pygame.draw.rect(screen, (255, 0, 0), (SCREEN_WIDTH // 2 - 300, 20, int(600 * boss_ratio), 40))
        pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH // 2 - 300, 20, 600, 40), 4)

        life_ratio = bees_life / bees_max_life
        pygame.draw.rect(screen, (100, 0, 0), (50, 50, 300, 30))
        pygame.draw.rect(screen, (0, 255, 0), (50, 50, int(300 * life_ratio), 30))
        pygame.draw.rect(screen, (255, 255, 255), (50, 50, 300, 30), 3)

        for bullet in player_bullets:
            pygame.draw.rect(screen, (255, 255, 0), bullet)

        for bullet in thruggBullets:
            pygame.draw.rect(screen, (255, 0, 0), bullet["rect"])

        new_powerups = []
        for power in powerups:
            power["rect"].y += 5

            if power["type"] == "double":
                color = (200, 0, 255)
            elif power["type"] == "shield":
                color = (0, 255, 255)
            else:
                color = (0, 255, 0)

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
                    pygame.draw.rect(screen, color, power["rect"])
                    new_powerups.append(power)

        powerups = new_powerups

        if bees_life <= 0:
            testo_sconfitta = font.render("YOU LOST", True, (255, 0, 0))
            screen.blit(testo_sconfitta, (SCREEN_WIDTH // 2 - testo_sconfitta.get_width() // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.mixer.music.pause()
            pygame.time.delay(3000)
            running = False

        if thrugg_life <= 0:
            testo_vittoria = font.render("YOU WON", True, (255, 255, 0))
            screen.blit(testo_vittoria, (SCREEN_WIDTH // 2 - testo_vittoria.get_width() // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.mixer.music.pause()
            pygame.time.delay(3000)
            running = False

        if bees_rect.colliderect(thrugg_rect):
            testo_sconfitta = font.render("YOU LOST", True, (255, 0, 0))
            screen.blit(testo_sconfitta, (SCREEN_WIDTH // 2 - testo_sconfitta.get_width() // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.mixer.music.pause()
            pygame.time.delay(3000)
            running = False

        pygame.display.flip()

    home_screen()
def main() -> None:
    home_screen()

if __name__ == "__main__":
    main()

def main() -> None:
    import pygame
    import random
    import sys

    pygame.init()

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
            screen.fill((20, 20, 30))

            title = font.render("THIS GAME IS TOO MASSIVE", True, (255, 255, 0))
            level1_text = small_font.render("Press 1 for Level 1", True, (255, 255, 255))
            level2_text = small_font.render("Press 2 for Level 2", True, (255, 255, 255))
            quit_text = small_font.render("Press ESC to quit", True, (200, 200, 200))

            screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 200))
            screen.blit(level1_text, (SCREEN_WIDTH//2 - level1_text.get_width()//2, 500))
            screen.blit(level2_text, (SCREEN_WIDTH//2 - level2_text.get_width()//2, 550))
            screen.blit(quit_text, (SCREEN_WIDTH//2 - quit_text.get_width()//2, 600))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        level1()
                    if event.key == pygame.K_2:
                        level2()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    # --------------------- LIVELLO 1 ---------------------
    def level1():

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
                        running = False

                    if event.key == pygame.K_SPACE:
                        bullet = pygame.Rect(x + w//2 - 5, y, 10, 20)
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

            # Proiettili giocatore
            for bullet in player_bullets[:]:
                bullet.y -= 12
                pygame.draw.rect(screen, (255, 255, 0), bullet)
                if bullet.y < 0:
                    player_bullets.remove(bullet)

            # Proiettili nemici
            for bullet in enemy_bullets[:]:
                bullet.y += 15
                pygame.draw.rect(screen, (255, 255, 255), bullet)
                if bullet.y > SCREEN_HEIGHT:
                    enemy_bullets.remove(bullet)

                if bullet.colliderect(player):
                    testo_sconfitta = font.render("YOU LOST", True, (255, 0, 0))
                    screen.blit(testo_sconfitta, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    running = False

            # Nemici
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
                    pygame.time.delay(3000)
                    running = False

            testo_punti = font.render("Punti: " + str(punti), True, (255, 0, 0))
            screen.blit(testo_punti, (SCREEN_WIDTH - 250, 20))

            pygame.display.flip()

            if punti >= 2000:
                testo_vittoria = font.render("YOU WON", True, (255, 255, 0))
                screen.blit(testo_vittoria, (SCREEN_WIDTH // 2 - 100 , SCREEN_HEIGHT // 2))
                pygame.display.flip()
                pygame.time.delay(3000)
                running = False

        pygame.time.set_timer(ADD_ENEMY, 0)
        home_screen()


    def level2():
        
        import random

        nome_player = "invincible"
        hp_1 = 200
        difesa_1 = 10
        attack_1 = 50

        nome_bot = "omni man"
        hp_2 = 600
        difesa_2 = 5
        attack_2 = 30
        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Invincible vs Omni-Man")
        clock = pygame.time.Clock()
                
        invincible_img = pygame.image.load("invincible.png").convert_alpha()
        omniman_img = pygame.image.load("omniman.png").convert_alpha()

        invincible_img = pygame.transform.scale(invincible_img, (250, 350))
        omniman_img = pygame.transform.scale(omniman_img, (400, 400))
            
        player_acted = False
        doge = False
        battle_message = ""
        battle_message2 = ""
        text = ""
        
        def draw_fight_screen():
            nonlocal battle_message, battle_message2
            
            screen.fill((255, 255, 255))

            font = pygame.font.SysFont("arial", 25)
            small_font = pygame.font.SysFont("arial", 18)
            
            screen.blit(invincible_img, (300, 120))
            screen.blit(omniman_img, (800, 0))
            
            if battle_message != "":
                message_font = pygame.font.SysFont("arial", 22)
                text = message_font.render(battle_message, True, (0,0,0))
                screen.blit(text, (550, 530))
            
            if battle_message2 != "":
                message_font = pygame.font.SysFont("arial", 22)
                text = message_font.render(battle_message2, True, (0,0,0))
                screen.blit(text, (550, 600))

            pygame.draw.rect(screen, (0,0,0), (1100, 50, 300, 100), 3)
            name_text = font.render("omni man", True, (0,0,0))
            screen.blit(name_text, (1110, 60))

            hp_bar_width = int((hp_2 / 500) * 200)
            pygame.draw.rect(screen, (255,0,0), (1110, 100, hp_bar_width, 20))

            pygame.draw.rect(screen, (0,0,0), (50, 300, 300, 100), 3)
            player_text = font.render("Invincible", True, (0,0,0))
            screen.blit(player_text, (60, 310))

            hp_bar_width_player = int((hp_1 / 200) * 200)
            pygame.draw.rect(screen, (0,255,0), (60, 350, hp_bar_width_player, 20))

            pygame.draw.rect(screen, (0,0,0), (0, 500, 1500, 250), 3)

            move1 = small_font.render("1 - Attacck", True, (0,0,0))
            move2 = small_font.render("2 - doge", True, (0,0,0))
            move3 = small_font.render("3 - Defence", True, (0,0,0))
            move4 = small_font.render("4 - Special", True, (0,0,0))

            screen.blit(move1, (50, 580))
            screen.blit(move2, (50, 680))
            screen.blit(move3, (300, 580))
            screen.blit(move4, (300, 680))
            

            pygame.display.flip()
            
        def turn_player():
            small_font = pygame.font.SysFont("arial", 18)
            
            nonlocal hp_1, hp_2, difesa_1, doge, player_acted, battle_message, difesa_2
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        critico = random.randint(1,100)
                        if critico <= 10:
                            hp_2 -= (attack_1*2) - difesa_2
                            damage = (attack_1*2) - difesa_2
                            battle_message = f" YOU DID CRITICAL DAMAGE you did {damage} damage, {hp_2} hp left for omniman"
 
                            
                        else:
                            hp_2 -= attack_1 - difesa_2
                            damage = attack_1 - difesa_2
                            battle_message = f" INVINCIBLE USE ATTACK you did {damage} damage, {hp_2} hp left for omnniman"
                            
# hai il 50% di possibilita di schivare il prossimo attacco del nemico se il turno precedende eri riuscito a schivare
                        difesa_2 = 5
# se il bot aveva usato defence, il prossimo turno la sua difesa torna normale
                        if doge == True:
                            if random.randint(1,2) == 1:
                                doge = False
#abbiamo fatto il nostro turno quindi il bot ora puo avere il suo avendo player acted su TRUE
                        player_acted = True

                    if event.key == pygame.K_2:
                        valore = random.randint(1,50)
                        
# niente ho risolto

                        if valore >= 25:
                            doge = True
                            battle_message = "YOU USED DOGE, AND YOU SUCCEED"
                        else:
                            doge = False
                            battle_message = "YOU USED DOGE BUT FAILED"
                        difesa_2 = 5
                            
                        player_acted = True

                    if event.key == pygame.K_3:
                        difesa_1 = 20
                        battle_message = "YOU USED DEFENCE, YOU TAKE 10 LESS DAMAGE AND 5 LESS FOR THE NEXT TURN!"
                        player_acted = True
                        difesa_2 = 5
                        if doge == True:
                            if random.randint(1,2) == 1:
                                doge = False

                    if event.key == pygame.K_4:
                        numero = random.randint(20,110) 
                        hp_2 -= numero - difesa_2
                        danno = numero - difesa_2
                        battle_message = f" YOU USED SPECIAL AND DID {danno} DAMAGE, {hp_2} hp left for omaniman"
                        player_acted = True
                        difesa_2 = 5
                        if doge == True:
                            if random.randint(1,2) == 1:
                                doge = False
        
        def turn_bot():
            nonlocal hp_2, hp_1, difesa_2, difesa_1, doge, battle_message2

            move = random.randint(1,4)

            if move == 1:
                difesa_2 = 20
                battle_message2 = "OMNIMAN USED DEFENCE, HE WILL TAKE 10 LESS DAMAGE FOR THIS TURN"

            elif move == 2:
                if not doge:
                    critico = random.randint(1,100)
                    if critico <= 10:
                        hp_1 -= attack_2*2 - difesa_1
                        danno = attack_2*2 - difesa_1
                        battle_message2 = f"OMNIMAN DID CRITICAL DAMAGE, YOU TOOK {danno} DAMAG, {hp_1} hp left for invincible"
                    
                    else:
                        hp_1 -= attack_2 - difesa_1
                        danno = attack_2 - difesa_1
                        battle_message2 = f"OMNIMAN USE ATTACK, YOU TOOK {danno} DAMAGE, {hp_1} hp left for invincible"
                     
                if doge == True:
                    battle_message2 = "OMNIMAN TRIED TO ATTACK, BUT YOU DOGED!"
                    
            elif move == 3:
                hp_2 += 20
                battle_message2 = f"OMNIMAN HEALED HIMSELF OF 20 HP!, {hp_2} hp left for omniman"
             
            elif move == 4:
                if not doge:
                    dmg = random.randint(30,90)
                    hp_1 -= dmg - difesa_1
                    danno = dmg - difesa_1
                    battle_message2 = f"OMNIMAN USE SPECIAL, YOU TOOK {danno} DAMAGE, {hp_1} hp left for invincible"
                if doge == True:
                    battle_message2 = "OMNIMAN TRIED TO ATTACK, BUT YOU DOGED!"
                

        while True:
            font = pygame.font.SysFont("comicsansms", 32)
            clock.tick(60)   # ← rallenta il loop
            
            turn_player()
            draw_fight_screen()
            
            if hp_2 <= 0:
                clock.tick(60)
                testo_vittoria = font.render("YOU WON", True, (255, 255, 0))
                screen.blit(testo_vittoria, (SCREEN_WIDTH // 2 - 100 , SCREEN_HEIGHT // 2))
                pygame.display.flip()
                pygame.time.delay(3000)
                break
            

            if player_acted:  # ← il bot gioca SOLO dopo di te
                pygame.time.delay(1000)
                turn_bot()
                player_acted = False

            if difesa_1 > 10:
                difesa_1 -= 5

            if hp_1 <= 0:
                testo_sconfitta = font.render("YOU LOST", True, (255, 0, 0))
                screen.blit(testo_sconfitta, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
                pygame.display.flip()
                pygame.time.delay(3000)
                break
            
        home_screen()

        

    # --------------------- START ---------------------
    home_screen()

if __name__ == "__main__":
    main()

            


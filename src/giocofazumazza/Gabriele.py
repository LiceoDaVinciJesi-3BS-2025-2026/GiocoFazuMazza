def main():
    import pygame
    import random

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
            level1_text = small_font.render("Premi 1 per Livello 1", True, (255, 255, 255))
            level2_text = small_font.render("Premi 2 per Livello 2", True, (255, 255, 255))
            quit_text = small_font.render("Premi ESC per uscire", True, (200, 200, 200))

            screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 200))
            screen.blit(level1_text, (SCREEN_WIDTH//2 - level1_text.get_width()//2, 500))
            screen.blit(level2_text, (SCREEN_WIDTH//2 - level2_text.get_width()//2, 550))  
            screen.blit(quit_text, (SCREEN_WIDTH//2 - quit_text.get_width()//2, 600))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        level1()
                    if event.key == pygame.K_2:
                        level2
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()


    # --------------------- LIVELLO 1 ---------------------
    def level1():

        imgSfondo = pygame.image.load("place.jpg")
        imgSfondo = pygame.transform.scale(imgSfondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

        imgBees = pygame.image.load("bees.png")
        imgBees = pygame.transform.scale(imgBees, (40, 40))

        imgConquest = pygame.image.load("Conquest.png") 
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
        
        punti = 0
        running = True
        font = pygame.font.SysFont("comicsansms", 32)


        while running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                    if event.key == pygame.K_SPACE:
                        bullet = pygame.Rect(x + w//2 - 5, y, 10, 20)
                        player_bullets.append(bullet)

                if event.type == ADD_ENEMY:
                    enemy_width = 100
                    enemy_height = 100
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
                    running = False
                    stato_perdita = True
                    
                    if stato_perdita:
                        imgSfondo = pygame.image.load("place.jpg")
                        imgSfondo = pygame.transform.scale(imgSfondo, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        
                        font_perdita = pygame.font.SysFont("comicsansms", 120)
                        testo_perdita = font_perdita.render("YOU LOST", True, (255,0,0))
                        screen.blit(testo_perdita,
                                    (SCREEN_WIDTH//2 - testo_perdita.get_width()//2,
                                     SCREEN_HEIGHT//2 - testo_perdita.get_height()//2))
                        pygame.display.flip()
                        pygame.time.wait(3000)

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
                    running = False
                    stato_perdita = True
                    
                    if stato_perdita:
                        imgSfondo = pygame.image.load("place.jpg")
                        imgSfondo = pygame.transform.scale(imgSfondo, (SCREEN_WIDTH, SCREEN_HEIGHT))
                        
                        font_perdita = pygame.font.SysFont("comicsansms", 120)
                        testo_perdita = font_perdita.render("YOU LOST", True, (255,0,0))
                        screen.blit(testo_perdita,
                                    (SCREEN_WIDTH//2 - testo_perdita.get_width()//2,
                                     SCREEN_HEIGHT//2 - testo_perdita.get_height()//2))
                        pygame.display.flip()
                        pygame.time.wait(3000)
            
            testo_punti = font.render("Punti: " + str(punti), True, (255, 0, 0))
            screen.blit(testo_punti, (SCREEN_WIDTH - 250, 20))
            
            if punti >= 2000:
                running = False
                stato_vittoria = True
                
                if stato_vittoria:
                    imgSfondo = pygame.image.load("place.jpg")
                    imgSfondo = pygame.transform.scale(imgSfondo, (SCREEN_WIDTH, SCREEN_HEIGHT))
                    
                    font_vittoria = pygame.font.SysFont("comicsansms", 120)
                    testo_vittoria = font_vittoria.render("YOU WON!!", True, (255,255,0))
                    screen.blit(testo_vittoria,
                                (SCREEN_WIDTH//2 - testo_vittoria.get_width()//2,
                                 SCREEN_HEIGHT//2 - testo_vittoria.get_height()//2))
                    pygame.display.flip()
                    pygame.time.wait(3000)


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
            pygame.draw.rect(screen, (255, 255, 255), bullet)

        pygame.display.flip()

        pygame.quit()
        pygame.display.flip()

        pygame.time.set_timer(ADD_ENEMY, 0)
        home_screen()

    def level2():
        import random
    # ====== dati giocatore ======
        nome = "invincible"
        hp_1 = 200
        difesa_1 = 10
        attack_1 = 50
    #    while True:
    #        doge_1 = random.randint(1,10)
    #        if doge_1 <= 5:
    #            doge = True
    #        if doge_2 > 5:
    #            doge = False
        nome = "omni man"
        hp_2 = 500
        difesa_2 = 5
        attack_2 = 30
        
        def turn_player():
            if event.key == pygame.K_1:
                critico =  random.randint(1,100)
                if critico >= 10:
                    hp_2 -= (attack*2) + difesa_2
                else:
                    hp_2 -= attack + difesa_2
            if event.key == pygame.k_2:
                doge = random.randint(1,50)
                if doge >= 50:
                    doge = True
                else:
                    doge = False
            if event.key == pygame.K_3:
                difesa_1 = 20
            if event.key == pygame.k_4:
                hp_2 -= random.randint(10,70) + difesa_2
        
        def turn_bot():
            move = random.randint(1,4)
            while True:
                if move == 1:
                    difesa_2 = 20
                    break
                elif move == 2:
                    if doge == True:
                        break
                    critico = random.randint(10,100)
                    if critico >= 10:
                        hp_1 -= attack_2*2 + difesa_1
                        break
                    else:
                        hp_1 -= attack_2 + difesa_1
                        break
                elif move == 3:
                    hp_2 += 20
                    break
                elif move == 4:
                    if doge == True:
                        break
                    hp_1 -= random.randint(30,60) + difesa_1
                    break
                
        while True:
            turn_player()
            turn_bot()
            
            if difesa_1 > 10:
                difesa -= 5
            if difesa_2 > 5:
                difesa -= 5
            if doge == True:
                doge_2 = random.randint(1,3)
                if doge_2 == 1:
                    doge = False
                else:
                    ""
            if hp_1 == 0:
                print("YOU LOST")
                break
            if hp_2 == 0:
                print("YOU WON!")
                   

    # --------------------- START ---------------------
    home_screen()


            


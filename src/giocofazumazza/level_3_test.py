import pygame
pygame.init()

    
def ciao():
    import random

    nome_player = "invincible"
    hp_1 = 200
    difesa_1 = 10
    attack_1 = 50

    nome_bot = "omni man"
    hp_2 = 600
    difesa_2 = 5
    attack_2 = 30
    
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Invincible vs Omni-Man")
    clock = pygame.time.Clock()
        
    player_acted = False
    doge = False
    
    def draw_fight_screen():
        screen.fill((255, 255, 255))

        font = pygame.font.SysFont("arial", 25)
        small_font = pygame.font.SysFont("arial", 18)

        pygame.draw.rect(screen, (0,0,0), (450, 50, 300, 100), 3)
        name_text = font.render("omni man", True, (0,0,0))
        screen.blit(name_text, (460, 60))

        hp_bar_width = int((hp_2 / 500) * 200)
        pygame.draw.rect(screen, (255,0,0), (460, 100, hp_bar_width, 20))

        pygame.draw.rect(screen, (0,0,0), (50, 300, 300, 100), 3)
        player_text = font.render("Invincible", True, (0,0,0))
        screen.blit(player_text, (60, 310))

        hp_bar_width_player = int((hp_1 / 200) * 200)
        pygame.draw.rect(screen, (0,255,0), (60, 350, hp_bar_width_player, 20))

        pygame.draw.rect(screen, (0,0,0), (0, 450, 800, 150), 3)

        move1 = small_font.render("1 - Attacco", True, (0,0,0))
        move2 = small_font.render("2 - Schiva", True, (0,0,0))
        move3 = small_font.render("3 - Difesa", True, (0,0,0))
        move4 = small_font.render("4 - Speciale", True, (0,0,0))

        screen.blit(move1, (50, 470))
        screen.blit(move2, (50, 500))
        screen.blit(move3, (300, 470))
        screen.blit(move4, (300, 500))

        pygame.display.flip()
        
    def turn_player():
        nonlocal hp_1, hp_2, difesa_1, doge, player_acted
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    critico = random.randint(1,100)
                    if critico <= 10:
                        hp_2 -= (attack_1*2) - difesa_2
                    else:
                        hp_2 -= attack_1 - difesa_2
                    player_acted = True

                if event.key == pygame.K_2:
                    valore = random.randint(1,50)
                    doge = True if valore >= 25 else False
                    player_acted = True

                if event.key == pygame.K_3:
                    difesa_1 = 20
                    player_acted = True

                if event.key == pygame.K_4:
                    hp_2 -= random.randint(10,100) - difesa_2
                    player_acted = True
    
    def turn_bot():
        nonlocal hp_2, hp_1, difesa_2, difesa_1, doge

        move = random.randint(1,4)

        if move == 1:
            difesa_2 = 20

        elif move == 2:
            if not doge:
                critico = random.randint(1,100)
                if critico <= 10:
                    hp_1 -= attack_2*2 - difesa_1
                else:
                    hp_1 -= attack_2 - difesa_1

        elif move == 3:
            hp_2 += 20

        elif move == 4:
            if not doge:
                hp_1 -= random.randint(30,90) - difesa_1

    while True:
        clock.tick(60)   # ← rallenta il loop
        draw_fight_screen()
        turn_player()

        if player_acted:   # ← il bot gioca SOLO dopo di te
            turn_bot()
            player_acted = False

        if difesa_1 > 10:
            difesa_1 -= 5
        if difesa_2 > 5:
            difesa_2 -= 5

        if doge:
            if random.randint(1,3) == 1:
                doge = False

        if hp_1 <= 0:
            print("YOU LOST")
            break
        if hp_2 <= 0:
            print("YOU WON!")
            break

    pygame.quit()

ciao()
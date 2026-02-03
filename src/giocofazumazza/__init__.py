def main() -> None:
    import pygame

    pygame.init()

    screen = pygame.display.set_mode( (800, 600) )

    pygame.display.set_caption("this game is too MASSIVE")

    running = True

    Titlefont = pygame.font.SysFont('Impact', 100)
    Normalfont = pygame.font.SysFont('Impact', 30)

    game_end = Titlefont.render("Hai Perso", True, "red")
    close_tip = Normalfont.render("Click ESC to exit", True, "blue","yellow")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        pygame.display.flip()


    screen.blit(game_end, (100,100))
    screen.blit(close_tip, (100,300))
        
    pygame.quit()
                

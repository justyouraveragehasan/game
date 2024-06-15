import pygame, sys

from core import graphics

def main_menu() -> None:
    pass 

def game() -> None:
    #initial pygame init shit
    WIDTH = 1920
    HEIGHT = 1080
    FPS = 30

    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Game")
    clock = pygame.time.Clock()
   
    # Gameloop 
    run = True

    state = "Game" 
    state = "Menu"

    while run:
        #set fps
        clock.tick(FPS)

        #draw screen
        match state:
            case "Menu":
                graphics.draw_main_menu(screen,WIDTH,HEIGHT)
                button1 = pygame.Rect(WIDTH/2 -200,HEIGHT/2,400,100)
                pygame.draw.rect(screen,(255,0,255),button1)
            case "Game":
                graphics.draw_game_screen(screen,WIDTH,HEIGHT)
            case _:
                print("How did we get here?!")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    state = "Game"

        pygame.display.flip()


if __name__ == "__main__":
    game()



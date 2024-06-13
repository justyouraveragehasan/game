import pygame

from core import graphics

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
                graphics.main_menu(screen,WIDTH,HEIGHT)
            case "Game":
                graphics.game_screen(screen,WIDTH,HEIGHT)
            case _:
                print("How did we get here?!")

        pygame.display.flip()


if __name__ == "__main__":
    game()



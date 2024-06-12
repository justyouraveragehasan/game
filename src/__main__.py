import pygame

def draw_menu_screen() -> None:
    pass

def draw_game_screen() -> None:
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
    state = "Menu"

    while run:
        #set fps
        clock.tick(FPS)

        #draw screen
        match state:
            case "Menu":
                draw_menu_screen()
            case "Game":
                draw_game_screen()
            case _:
                print("How did we get here?!")

        pygame.display.flip()


if __name__ == "__main__":
    game()



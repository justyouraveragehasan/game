import pygame

def game() -> None:

    WIDTH = 360
    HEIGHT = 480
    FPS = 30

    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Game")
    clock = pygame.time.Clock()
    
    while True:
        clock.tick()
        screen.fill((0,0,0))
        pygame.display.flip()



def main() -> None:
    print("Hello World!")
    game()
    return None

if __name__ == "__main__":
    main()


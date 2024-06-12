import pygame

def game() -> None:

    WIDTH = 1920
    HEIGHT = 1080
    FPS = 30

    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Game")
    clock = pygame.time.Clock()
    
    while True:
        #set fps
        clock.tick(FPS)

        #draw screen
        screen.fill((255,255,255))
        pygame.display.flip()



def main() -> None:
    print("Hello World!")
    game()
    return None

if __name__ == "__main__":
    main()




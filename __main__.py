import pygame, sys

from core import graphics

#initial pygame init shit
WIDTH = 1920
HEIGHT = 1080
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

def main_menu() -> None:
    while True:
        clock.tick(FPS)
        graphics.draw_main_menu(screen,WIDTH,HEIGHT)
        button1 = pygame.Rect(WIDTH/2 -200,HEIGHT/2,400,100)
        pygame.draw.rect(screen,(255,0,255),button1)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    game()

        pygame.display.flip()

    

def game() -> None:
    running = True
    while running:
        clock.tick(FPS)
        graphics.draw_game_screen(screen,WIDTH,HEIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()



if __name__ == "__main__":
    game()



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
        
        isoblock = pygame.image.load("resources/big_test_cube.png").convert_alpha()
        
        #this shit works
        #testblock = isoblock.get_rect()
        #testblock.center = (200,300)

        #testblock2 = isoblock.get_rect()
        #testblock2.center = (250,325)

        #
        #testblock3 = isoblock.get_rect()
        #testblock3.center = (150,325)


        #testblock4 = isoblock.get_rect()
        #testblock4.center = (200,350)



        #screen.blit(isoblock,testblock)
        #screen.blit(isoblock,testblock2)
        #screen.blit(isoblock,testblock3)
        #screen.blit(isoblock,testblock4)
        #block1 = pygame.Rect(WIDTH/2 -200,HEIGHT/2,100,100)
        
        coords = [100,100]
        
        for i in range(0,15):
            if i != 6:
                for j in range(0,8):
                    screen.blit(isoblock,coords)
                    coords[1] += 25
                    coords[0] -= 50
                    screen.blit(isoblock,coords)
                    coords[0] += 100
                    screen.blit(isoblock,coords)
                    coords[0] -= 50
                    coords[1] += 25
                    screen.blit(isoblock,coords)
                    coords[1] -= 50
                    coords[0] += 200
                coords[0] -= 1600
                if i%2 == 0:
                    coords[0] += 100
                else:
                    coords[0] -= 100
                coords[1] += 50
            else:
                coords[0] += 200
                coords[1] += 100

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()



if __name__ == "__main__":
    game()



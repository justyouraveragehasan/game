import pygame

def main_menu(screen,WIDTH,HEIGHT) -> None:
    bg = pygame.image.load('resources/main_menu_bg.png')
    bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))

    screen.blit(bg, (0,0))
    #test button
    button1 = pygame.Rect(WIDTH/2 -200,HEIGHT/2,400,100)
    pygame.draw.rect(screen,(255,0,255),button1)


def game_screen(screen,WIDTH,HEIGHT) -> None:
    bg = pygame.image.load('resources/windows_xp_background.jpg')
    bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
    screen.blit(bg, (0,0))

import pygame

def draw_main_menu(screen,WIDTH,HEIGHT) -> None:
    bg = pygame.image.load('resources/main_menu_bg.png')
    bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))

    screen.blit(bg, (0,0))
    #test button


def draw_game_screen(screen,WIDTH,HEIGHT) -> None:
    #bg = pygame.image.load('resources/windows_xp_background.jpg')
    #bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
    #screen.blit(bg, (0,0))

    screen.fill((0,0,0))

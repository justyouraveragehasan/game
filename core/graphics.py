import pygame

def draw_main_menu(screen,WIDTH,HEIGHT) -> None:
    bg = pygame.image.load('resources/main_menu_bg.png').convert_alpha()
    bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))

    screen.blit(bg, (0,0))
    #test button


def draw_game_screen(screen,WIDTH,HEIGHT) -> None:
    bg = pygame.image.load('resources/windows_xp_background.jpg')
    bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
    screen.blit(bg, (0,0))

    screen.fill((0,0,0))

        
    isoblock = pygame.image.load("resources/big_test_cube.png").convert_alpha()
    f = open('resources/map.txt')
    map_data = [[int(c) for c in row] for row in f.read().split('\n')]# I took this from online, it takes each row into an array and takes each tile as an element for a nice 2d array.
    print(map_data)                                                   # because of the \n check it always has an empty list at the end
    f.close()

    for y, row in enumerate(map_data):
            for x, tile in enumerate(row): #enumerate is op, if you use enumerate x is the count and tile is the value so its like for tile in row and for i in range 0,len(row) at the same time
                if tile > 0:
                    screen.blit(isoblock, (400 + x * 50 - y * 50, 100 + x * 25 + y * 25)) #x offset is 50, y offset is 25 
                    if tile > 1:
                        screen.blit(isoblock, (400 + x * 50 - y * 50, 100 + x * 25 + y * 25 -49)) #y offset is 49 pixels for second layer because the top layer would be covered
                    if tile > 2:
                        screen.blit(isoblock, (400 + x * 50 - y * 50, 100 + x * 25 + y * 25 -49*2)) #y offset is 49*2 pixels for third layer because the top layer would be covered

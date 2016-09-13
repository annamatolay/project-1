import pygame
from common import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((win_x, win_y))

clock = pygame.time.Clock()
player = Player(screen=screen, img='player_white2.png', p_x=30, p_y=450)
run = True
while run is True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        print(event)

    screen.fill(colors['WHITE'])

    player.render()
    player.move()

    pressed = pygame.key.get_pressed()

    pygame.display.update()

    clock.tick(60)
pygame.quit()

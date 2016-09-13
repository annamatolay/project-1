import pygame
from common import *
from player import *
from thing import *

pygame.init()

screen = pygame.display.set_mode((win_x, win_y))

clock = pygame.time.Clock()
player = Player(screen=screen, img='player_white.png', p_x=30, p_y=450)
run = True
while run is True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        print(event)

    screen.fill(colors['WHITE'])

    Object(screen=screen, color=colors['BLACK'], x=200, y=444, width=30, height=90).render_gate()

    player.render()
    player.move()

    pygame.display.update()

    clock.tick(60)
pygame.quit()

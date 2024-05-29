import pygame
from screen_el import (
    bg_1
)
from utils import quit_the_game

clock = pygame.time.Clock()
pygame.init()
running = True

screen = pygame.display.set_mode((995, 664))
pygame.display.set_caption('Простая игра!!!')

while running:
    screen.blit(bg_1, (0, 0))

    pygame.display.update()
    quit_the_game()

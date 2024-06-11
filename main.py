import pygame
from screen_el import (
    bg_1
)
from utils import quit_the_game
from spritesheet import Spritesheet

clock = pygame.time.Clock()
pygame.init()
running = True

screen = pygame.display.set_mode((995, 664))
pygame.display.set_caption('Простая игра!!!')

my_sprite = Spritesheet('images/elf.png')
train1 = my_sprite.get_sprite(10, 10, 80, 90)

while running:
    screen.blit(bg_1, (0, 0))
    screen.blit(train1, (15, 480))

    pygame.display.update()
    quit_the_game()

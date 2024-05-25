import pygame as pg
from screen_el import (
    bg_1
)

clock = pg.time.Clock()
pg.init()
running = True

screen = pg.display.set_mode((995, 664))
pg.display.set_caption('Простая игра!!!')

while running:
    screen.blit(bg_1, (0, 0))

    pg.display.update()
    
import pygame


class Spritesheet:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.spritesheet = pygame.image.load(filename).convert()

    def get_sprite(self, x, y, w, h) -> None:
        sprite = pygame.Surface((w, h), pygame.SRCALPHA, 32)
        sprite = sprite .convert_alpha()
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(
            self.spritesheet, (0, 0), (x, y, w, h)
            )
        return sprite

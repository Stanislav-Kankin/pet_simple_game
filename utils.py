import pygame


def quit_the_game() -> None:
    """
    Корректное закрытие окна игры на крестик
    """
    for event in pygame.event.get():  # Список всех доступных событий
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()




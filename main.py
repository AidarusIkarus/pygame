import pygame
import math


def sphere():
    screen.fill(pygame.Color('yellow'))
    for x in range(size[0] // num):
        for y in range(size[1] // num):
            pygame.draw.polygon(screen, pygame.Color('orange'), (
                (x * num + num / 2, y * num), (x * num, y * num + num / 2), (x * num + num / 2, y * num + num),
                (x * num + num, y * num + num / 2)))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Ромбики')

    try:
        num = int(input())
    except ValueError:
        raise ValueError('Неправильный формат ввода')

    size = (300, 300)  # размер окна
    screen = pygame.display.set_mode(size)
    sphere()
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

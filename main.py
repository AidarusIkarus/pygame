import pygame
import os


def bricks():
    x = 150 - width * 0.75
    y = 150 - width / 4
    half_width = width / 2

    color_front = pygame.Color('white')
    color_upper = pygame.Color('white')
    color_side = pygame.Color('white')
    hsv = pygame.Color('white').hsva

    color_front.hsva = (hue, hsv[1] + 100, hsv[2] - 25, hsv[3])
    color_upper.hsva = (hue, hsv[1] + 100, hsv[2], hsv[3])
    color_side.hsva = (hue, hsv[1] + 100, hsv[2] - 50, hsv[3])

    pygame.draw.polygon(screen, color_front, ((x, y), (x + width, y), (x + width, y + width), (x, y + width)))
    pygame.draw.polygon(screen, color_upper, (
        (x + half_width, y - half_width), (x + half_width + width, y - half_width), (x + width, y), (x, y)))
    pygame.draw.polygon(screen, color_side, (
        (x + width, y), (x + half_width + width, y - half_width), (x + half_width + width, y + half_width),
        (x + width, y + width)))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Куб')

    try:
        width, hue = map(int, input().split())
    except ValueError:
        raise ValueError('Неправильный формат ввода')
    if width % 4 != 0 or width > 100 or hue < 0 or hue > 360:
        raise ValueError('Неправильный формат ввода')

    size = (300, 300)
    screen = pygame.display.set_mode(size)
    bricks()
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

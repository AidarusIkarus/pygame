import pygame


def rectangle():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (1, 1, width - 1, height - 1))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Прямоугольник')

    try:
        x, y = map(int, input().split())
    except ValueError:
        raise ValueError('Неправильный формат ввода')

    width, height = x, y
    screen = pygame.display.set_mode((width, height))
    rectangle()
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

import pygame


def sphere():
    screen.fill((0, 0, 0))
    step = 150 // num
    for i in range(0, num):
        pygame.draw.ellipse(screen, (255, 255, 255), (i * step, 0, 300 - i * 2 * step, 300), 1)
        pygame.draw.ellipse(screen, (255, 255, 255), (0, i * step, 300, 300 - i * 2 * step), 1)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Сфера')

    try:
        num = int(input())
    except ValueError:
        raise ValueError('Неправильный формат ввода')

    size = (300, 300)
    screen = pygame.display.set_mode(size)
    sphere()
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

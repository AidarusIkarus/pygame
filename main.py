import pygame


def chess():
    screen.fill((0, 0, 0))
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    for i in range(1, num + 1):
        color = colors[(i - 1) % 3]
        pygame.draw.circle(screen, color, (num * width, num * width), i * width, width)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Мишень')

    try:
        width, num = map(int, input().split())
    except ValueError:
        raise ValueError('Неправильный формат ввода')

    size = (2 * num * width, 2 * num * width)
    screen = pygame.display.set_mode(size)
    chess()
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

import pygame


def chess():
    screen.fill((0, 0, 0))
    cell = size // num
    colors = [(255, 255, 255), (0, 0, 0)]
    for x in range(num):
        for y in range(num):
            color = colors[(x + y) % 2]
            pygame.draw.rect(screen, color, (x * cell, y * cell, cell, cell))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шахматная клетка')

    try:
        size, num = map(int, input().split())
    except ValueError:
        raise ValueError('Неправильный формат ввода')

    screen = pygame.display.set_mode((size, size))
    chess()
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

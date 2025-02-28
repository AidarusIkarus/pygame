import pygame


def bricks():
    white = (255, 255, 255)
    screen.fill(white)

    for y in range(0, size[1], 17):
        for x in range(0, size[0], 32):
            if y % 2 == 0:
                x -= 15
            pygame.draw.rect(screen, pygame.Color('red'), (x, y, 30, 15))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Кирпичи')

    # try:
    #     num = int(input())
    # except ValueError:
    #     raise ValueError('Неправильный формат ввода')

    size = (300, 200)
    screen = pygame.display.set_mode(size)
    bricks()
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

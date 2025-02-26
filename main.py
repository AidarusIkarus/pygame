import pygame

def cross():
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), 5)
    pygame.draw.line(screen, (255, 255, 255), (width, 0), (0, height), 5)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Крест')

    try:
        x, y = map(int, input().split())
    except ValueError:
        raise ValueError('Неправильный формат ввода')

    width, height = x, y
    screen = pygame.display.set_mode((width, height))
    cross()
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

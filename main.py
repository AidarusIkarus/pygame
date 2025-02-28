import pygame
import os

radius = float(0)


def circle():
    global radius
    screen.fill(pygame.Color('blue'))
    if boolean:
        pygame.draw.circle(screen, 'yellow', (x, y), int(radius))
        radius += 10 * clock.tick() / 1000


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтый круг')
    size = (300, 300)

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    boolean = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                radius = float(0)
                x, y = event.pos
                boolean = True

        circle()
        pygame.display.flip()
    pygame.quit()

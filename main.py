import pygame
import os

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шарики')
    size = (300, 300)

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    boolean = False
    radius = 10
    circles = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x < radius:
                    x = radius
                if y < radius:
                    y = radius
                circles.append([x, y, 1, -1])

        screen.fill('black')
        dt = clock.tick() / 1000
        for elem in circles:
            cur_x, cur_y, x_dir, y_dir = elem
            pygame.draw.circle(screen, 'white', (int(cur_x), int(cur_y)), radius)
            elem[0] -= x_dir * 100 / 1.414 * dt
            elem[1] += y_dir * 100 / 1.414 * dt
            if cur_x < radius:
                elem[0] = radius
                elem[2] = -elem[2]

            if cur_x > size[0] - radius:
                elem[0] = size[0] - radius
                elem[2] = -elem[2]

            if cur_y < radius:
                elem[1] = radius
                elem[3] = -elem[3]

            if cur_y > size[1] - radius:
                elem[1] = size[1] - radius
                elem[3] = -elem[3]
        pygame.display.flip()
    pygame.quit()

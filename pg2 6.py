import pygame
import math

change_speed = 50 / 60

if __name__ == '__main__':
    pygame.init()
    size = 201, 201
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Вентилятор")
    clock = pygame.time.Clock()

    angle = -90
    running = True
    speed = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    speed -= change_speed
                elif event.button == 3:
                    speed += change_speed

        screen.fill('black')
        angle += speed

        for blade_angle in range(0, 360, 120):
            left = (angle - 15 + blade_angle) * math.pi / 180
            right = (angle + 15 + blade_angle) * math.pi / 180
            x_left = size[0] // 2 + 70 * math.cos(left)
            y_left = size[1] // 2 + 70 * math.sin(left)
            x_right = size[0] // 2 + 70 * math.cos(right)
            y_right = size[1] // 2 + 70 * math.sin(right)

            pygame.draw.polygon(screen, pygame.Color('white'),
                                ((size[0] // 2, size[1] // 2), (x_left, y_left), (x_right, y_right)))

        pygame.draw.circle(screen, pygame.Color('white'), (size[0] // 2, size[1] // 2), 10)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

import pygame


def scale(center, value):
    x_center, y_center = center
    new_points = []
    for x, y in points:
        new_x = (x - x_center) * value + x_center
        new_y = (y - y_center) * value + y_center
        new_points.append((new_x, new_y))
    return new_points


if __name__ == '__main__':
    pygame.init()
    size = 501, 501
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Zoom")
    clock = pygame.time.Clock()

    with open("points.txt", "r") as file:
        inp = map(lambda x: str.replace(x, ",", "."), file.read().split(", "))
        points = list(map(lambda x: list(map(float, x[1:-1].split(";"))), inp))

    points = list(map(lambda x: [x[0] + size[0] // 2, (-x[1]) + size[1] // 2], points))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    points = scale((size[0] // 2, size[1] // 2), 1.1)
                elif event.y < 0:
                    points = scale((size[0] // 2, size[1] // 2), 0.9)

        screen.fill('black')
        pygame.draw.polygon(screen, pygame.Color('white'), points, 1)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

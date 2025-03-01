import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('К щелчку')
    size = (501, 501)

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    x, y = int(501 / 2), int(501 / 2)
    dest_x, dest_y = x, y

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                dest_x, dest_y = event.pos

        dif_x, dif_y = x - dest_x, y - dest_y
        if x != dest_x or y != dest_y:
            if dif_x < 0:
                x += 1
            elif dif_x > 0:
                x -= 1
            if dif_y < 0:
                y += 1
            elif dif_y > 0:
                y -= 1
        else:
            pass
        x, y = int(x), int(y)

        pygame.draw.circle(screen, 'red', (x, y), 20)
        pygame.display.flip()
        screen.fill('black')
        clock.tick(60)

    pygame.quit()

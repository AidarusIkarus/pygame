import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Перетаскивание')
    size = (300, 300)

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    boolean = False
    x, y = 0, 0
    prev_x, prev_y, new_x, new_y = 0, 0, 0, 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x < event.pos[0] < x + 100 and y < event.pos[1] < y + 100:
                    boolean = True

            if event.type == pygame.MOUSEMOTION:
                if boolean:
                    new_x, new_y = event.rel
                    x += new_x
                    y += new_y
            if event.type == pygame.MOUSEBUTTONUP:
                boolean = False
        screen.fill('black')

        pygame.draw.rect(screen, 'green', (x, y, 100, 100))
        pygame.display.flip()
    pygame.quit()

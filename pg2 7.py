import pygame


if __name__ == '__main__':
    pygame.init()
    size = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Прямоугольники с Ctrl+Z")
    clock = pygame.time.Clock()
    rectangles = []
    toDraw = False
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    toDraw = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    toDraw = True
                    rectangles.append([*event.pos, *event.pos])
            if event.type == pygame.KEYDOWN:
                mods = pygame.key.get_mods()
                if event.key == pygame.K_z and (mods & pygame.KMOD_CTRL) and rectangles:
                    rectangles.pop(-1)

        screen.fill((0, 0, 0))

        if toDraw:
            pos = pygame.mouse.get_pos()
            rectangles[-1] = [rectangles[-1][0], rectangles[-1][1], *pos]

        for x1, y1, x2, y2 in rectangles:
            height = min(y2 - y1, -10) if y2 - y1 < 0 else max(y2 - y1, 10)
            width = min(x2 - x1, -10) if x2 - x1 < 0 else max(x2 - x1, 10)
            pygame.draw.rect(screen, 'white', pygame.Rect(x1, y1, width, height), 5, 5)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

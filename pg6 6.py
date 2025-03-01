import pygame


class Rect(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.Surface((20, 20))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, *args):
        self.rect.y += 50 / 60
        if pygame.sprite.spritecollideany(self, platforms):
            self.rect.y -= 50 / 60

    def move(self, dx):
        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, platforms):
            self.rect.x -= dx


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = pygame.Surface((50, 10))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect(topleft=(x, y))


if __name__ == '__main__':
    pygame.init()
    rectangle = None
    platforms = pygame.sprite.Group()
    size = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Платформы")
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    platforms.add(Platform(*event.pos))
                elif event.button == 3:
                    rectangle = Rect(*event.pos)
            elif event.type == pygame.KEYDOWN and rectangle:
                if event.key == pygame.K_LEFT:
                    rectangle.move(-10)
                elif event.key == pygame.K_RIGHT:
                    rectangle.move(10)

        screen.fill('black')
        if rectangle:
            rectangle.update()
            screen.blit(rectangle.image, rectangle.rect)
        platforms.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

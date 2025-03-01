import os
import sys
import pygame
import random


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Bomb(pygame.sprite.Sprite):
    bomb1_image = load_image("bomb1.png")
    bomb2_image = load_image("bomb2.png")

    def __init__(self, elems, *group):
        super().__init__(*group)
        self.image = Bomb.bomb1_image
        self.rect = self.image.get_rect()
        while True:
            self.rect.x = random.randrange(size[0] - self.rect.width)
            self.rect.y = random.randrange(size[1] - self.rect.height)
            if not any(self.rect.colliderect(p) for p in elems):
                elems.append(self.rect.copy())
                break

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.bomb2_image


if __name__ == '__main__':
    pygame.init()
    all_sprites = pygame.sprite.Group()
    size = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Boom them all — 2")
    clock = pygame.time.Clock()
    elems = []
    for i in range(10):
        Bomb(elems, all_sprites)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)

        screen.fill('black')
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

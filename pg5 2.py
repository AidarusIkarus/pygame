import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':

    pygame.init()
    creature_image = load_image("hero.png")
    creature_rect = creature_image.get_rect(topleft=(0, 0))
    size = 300, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Герой двигается!")

    while pygame.event.wait().type != pygame.QUIT:
        screen.fill('white')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            creature_rect.y -= 10
        if keys[pygame.K_DOWN]:
            creature_rect.y += 10
        if keys[pygame.K_LEFT]:
            creature_rect.x -= 10
        if keys[pygame.K_RIGHT]:
            creature_rect.x += 10

        screen.blit(creature_image, creature_rect)
        pygame.display.flip()

    pygame.quit()

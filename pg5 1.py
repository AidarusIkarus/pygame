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
    pygame.mouse.set_visible(False)
    size = 800, 600
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Свой курсор мыши")
    cursor_img = load_image("arrow.png")
    cursor_rect = cursor_img.get_rect()

    while pygame.event.wait().type != pygame.QUIT:
        screen.fill('black')
        if pygame.mouse.get_focused():
            cursor_rect.topleft = pygame.mouse.get_pos()
            screen.blit(cursor_img, cursor_rect)
        pygame.display.flip()

    pygame.quit()

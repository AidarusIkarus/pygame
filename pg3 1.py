import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_width = 50

    def set_view(self, left, top, cell_width):
        self.left = left
        self.top = top
        self.cell_width = cell_width

    def render(self, screen):
        top_rect = self.top
        left_rect = self.left
        for x in self.board:
            for y in range(len(x)):
                pygame.draw.rect(screen, pygame.Color('white'), (left_rect, top_rect, self.cell_width, self.cell_width),
                                 1)
                left_rect += self.cell_width

            top_rect += self.cell_width
            left_rect = self.left


if __name__ == '__main__':
    pygame.init()
    size = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Инициализация игры")
    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('black')
        board.render(screen)
        pygame.display.flip()

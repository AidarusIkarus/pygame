import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left_rect = 10
        self.top_rect = 10
        self.cell_width = 50

    def set_view(self, left_rect, top_rect, cell_width):
        self.left_rect = left_rect
        self.top_rect = top_rect
        self.cell_width = cell_width

    def render(self, screen):
        top_rect = self.top_rect
        left_rect = self.left_rect
        for h in self.board:
            for i in range(len(h)):
                pygame.draw.rect(screen, pygame.Color('white'), (left_rect, top_rect, self.cell_width, self.cell_width), 1)
                left_rect += self.cell_width
            top_rect += self.cell_width
            left_rect = self.left_rect


if __name__ == '__main__':
    pygame.init()
    size = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Координаты клетки")
    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x_pos = (x - board.left_rect) // board.cell_width
                y_pos = (y - board.top_rect) // board.cell_width
                if 0 <= x_pos <= board.width - 1 and 0 <= y_pos <= board.height - 1:
                    print((x_pos, y_pos))
                else:
                    print(None)
        screen.fill('black')
        board.render(screen)
        pygame.display.flip()

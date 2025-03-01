import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        self.left_rect = 10
        self.top_rect = 10
        self.cell_size = 50
        self.colours = {0: pygame.Color('white'), 1: pygame.Color('red'), 2: pygame.Color('blue')}

    def set_view(self, left_rect, top_rect, cell_size):
        self.left_rect = left_rect
        self.top_rect = top_rect
        self.cell_size = cell_size

    def render(self, screen):
        top_rect = self.top_rect
        left_rect = self.left_rect
        for h in self.board:
            for i in range(len(h)):
                pygame.draw.rect(screen, pygame.Color('white'), (left_rect, top_rect, self.cell_size, self.cell_size),
                                 1)
                if h[i]:
                    pygame.draw.rect(screen, self.colours[h[i]],
                                     (left_rect + 1, top_rect + 1, self.cell_size - 2, self.cell_size - 2))
                left_rect += self.cell_size
            top_rect += self.cell_size
            left_rect = self.left_rect

    def change(self, cur_x, cur_y):
        if self.board[cur_y][cur_x] < 2:
            self.board[cur_y][cur_x] += 1
        else:
            self.board[cur_y][cur_x] = 0


if __name__ == '__main__':
    pygame.init()
    size = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Реакция на события от мыши")
    board = Board(5, 7)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                cur_x = (x - board.left_rect) // board.cell_size
                cur_y = (y - board.top_rect) // board.cell_size
                if 0 <= cur_x <= board.width - 1 and 0 <= cur_y <= board.height - 1:
                    board.change(cur_x, cur_y)

        screen.fill('black')
        board.render(screen)
        pygame.display.flip()

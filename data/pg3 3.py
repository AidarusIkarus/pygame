import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        self.left_rect = 10
        self.top_rect = 10
        self.cell_size = 50

    def set_view(self, left_rect, top_rect, cell_size):
        self.left_rect = left_rect
        self.top_rect = top_rect
        self.cell_size = cell_size

    def render(self, screen):
        top_rect = self.top_rect
        left_rect = self.left_rect
        for h in self.board:
            for i in range(len(h)):
                if h[i] == 0:
                    pygame.draw.rect(screen, pygame.Color('white'),
                                     (left_rect, top_rect, self.cell_size, self.cell_size), 1)
                else:
                    pygame.draw.rect(screen, pygame.Color('white'),
                                     (left_rect, top_rect, self.cell_size, self.cell_size))
                left_rect += self.cell_size
            top_rect += self.cell_size
            left_rect = self.left_rect

    def change(self, cur_x, cur_y):
        for row in range(len(self.board)):
            if row != cur_y:
                if self.board[row][cur_x] == 0:
                    self.board[row][cur_x] = 1
                else:
                    self.board[row][cur_x] = 0
            else:
                for i in range(len(self.board[row])):
                    if self.board[row][i] == 0:
                        self.board[row][i] = 1
                    else:
                        self.board[row][i] = 0


if __name__ == '__main__':
    pygame.init()
    size = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Чёрное в белое и наоборот")
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
                    print((cur_x, cur_y))
                    board.change(cur_x, cur_y)
                else:
                    print(None)

        screen.fill('black')
        board.render(screen)
        pygame.display.flip()

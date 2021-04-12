from.constants import RED, SQUARE_SIZE, BLACK, WHITE
import pygame


class Piece:
    PADDING = 20
    OUTLINE = 4
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        # if self.color == RED:
        #     self.direction = -1
        # else:
        #     self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    # calucalte x & y postion base on row and column we are in
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle( win, WHITE, (self.x, self.y), radius + self.OUTLINE )
        pygame.draw.circle(win, self.color, (self.x, self.y), radius )

    # move
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos() # tells you the postion on where you should be

    def __repr__(self):
        return str(self.color)

    '''
           
from .constants import RED, SQUARE_SIZE, BLACK, WHITE
import pygame


class Piece:
    PADDING = 20
    OUTLINE = 4

    def __init__(self, row, col, color, player):
        self.row = row
        self.col = col
        self.color = color
        self.player = player

        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    # calucalte x & y postion base on row and column we are in
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, WHITE, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    # move
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()  # tells you the postion on where you should be

    def __repr__(self):
        return str(self.color)

    '''

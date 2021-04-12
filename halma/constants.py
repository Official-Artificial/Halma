import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH//COLS
N_PIECES_PER_PLAYER = 15
# 10 x 10 = 15 pieces each
# 16 x 16 =  19 pieces each
# 8 x 8 =  10 pieces each

# rgb
RED = (255, 0, 0)
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BROWN = (205, 133, 63)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)  # what squares a person can move to
GREY = (128, 128, 128)
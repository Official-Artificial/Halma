# import pygame
# from halma.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, GREEN
# from halma.board import Board
# from halma.game import Game
#
# FPS = 60
#
# WIN = pygame.display.set_mode( (WIDTH, HEIGHT) )
# pygame.display.set_caption( 'Halma' )
#
# # user being able to move pieces by clicking
# def get_row_col_from_mouse(pos):
#     x, y = pos
#     row = y // SQUARE_SIZE
#     col = x // SQUARE_SIZE
#     return row, col
#
# def main():
#     run = True
#     clock = pygame.time.Clock()
#     game = Game(WIN)
#
#     # piece = board.get_piece(0,0)
#     # board.move(piece, 6, 7)
#
#     while run:
#         clock.tick( FPS )
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 pos = pygame.mouse.get_pos()
#                 row, col = get_row_col_from_mouse(pos)
#                 game.select(row, col)
#
#         game.update()
#
#     pygame.quit()
#
# if __name__ == "__main__":
#     main()
#
#
#

import pygame
from halma.constants import WIDTH, HEIGHT, SQUARE_SIZE
from halma.board import Board

FPS = 60

WIN = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Halma' )

# user being able to move pieces by clicking
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    # piece = board.get_piece(0,0)
    # board.move(piece, 6, 7)

    while run:
        clock.tick( FPS )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 4, 7)

        board.draw( WIN )
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

    '''
    
import pygame
import random
from halma.constants import WIDTH, HEIGHT, SQUARE_SIZE
from halma.board import Board

FPS = 60

WIN = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Halma' )

# user being able to move pieces by clicking
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
  	playerTurn = random.randint(0, 1)
    if playerTurn == 0:
      splayer = 'G'
    else:
      player = 'R'
    
    run = True
    clock = pygame.time.Clock()
    board = Board()

    # piece = board.get_piece(0,0)
    # board.move(piece, 6, 7)

    while run:
        clock.tick( FPS )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 4, 7)
            
              

        board.draw( WIN )
        pygame.display.update()
        # if True then while loop is broken and the game ends
        if board.winLoss():
          break

    pygame.quit()

if __name__ == "__main__":
    main()
    '''
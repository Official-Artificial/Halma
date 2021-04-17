import pygame
import random
from halma.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, RED, GREEN
from halma.board import Board
import easygui
from minimax.algorithm import simple_move
from minimax.algorithm import minimax
from halma.game import Game

FPS = 60

WIN = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Halma' )

# TODO: Get this from command line argument (sys.argv[])
IS_PLAYER2_AI = True

# user being able to move pieces by clicking
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    board = Board()
    piece = None
    availMoves = []
    selectedPiece = False
    currColor = None
    playerTurn = random.randint(0, 1)
    if playerTurn == 0:
      easygui.msgbox( 'Green Goes First', 'Game Start' )
      board.player = GREEN
    else:
       easygui.msgbox( 'Red Goes First', 'Game Start' )
       board.player = RED

    run = True
    clock = pygame.time.Clock()


    # piece = board.get_piece(0,0)
    # board.move(piece, 6, 7)

    def getTile(x,y):
        holder = board.get_piece(x,y)
        if holder == board.player:
            #add highlight
            board.availMoves(x,y, [], [])
            #outline available move

    while run:
        clock.tick( FPS )

        # if game.turn == GREEN:
        #     value, new_board = minimax(game.get_board(), 3, GREEN, game)
        #     game.ai_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if selectedPiece == True:
                    print(selectedPiece)
                    newPos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse( newPos )
                    if((row,col) in availMoves):
                        board.move(piece, row, col)
                        piece.color = currColor
                        selectedPiece = False
                        if board.player == GREEN:
                            board.player = RED
                        else:
                            board.player = GREEN
                        board.draw( WIN )
                    else:
                        easygui.msgbox( 'Invalid Move', 'Error!' )
                        print('Invalid Move')

                    ## TODO: MAKE THIS WORK
                    if IS_PLAYER2_AI == True:
                        piece, row, col = simple_move(board, board.player)
                        board.move(piece, row, col )
                        piece.color = currColor
                        selectedPiece = False
                        if board.player == GREEN:
                            totalMovesG += 1
                            board.player = RED
                        else:
                            totalMovesR += 1
                            board.player = GREEN
                        board.draw( WIN )

                else:
                    print(selectedPiece)
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    if board.get_piece(row, col).color == board.player:
                        availMoves = []
                        availMoves = board.availMoves(row, col, availMoves, [])
                        # for i in availMoves:
                        #     if board.get_piece(i[0], i[1]) != 0:
                        #         availMoves.remove(i)
                        piece = board.get_piece(row, col)
                        currColor = piece.color
                        piece.color = WHITE
                        selectedPiece = True
                    else:
                        easygui.msgbox( 'Not your turn', 'Error!' )
                        print('Not your turn')

        board.draw( WIN )
        pygame.display.update()
        # if True then while loop is broken and the game ends
        # if board.checkWin(curreGreen=10, winAmount=10):
            # break

    pygame.quit()

if __name__ == "__main__":
    main()

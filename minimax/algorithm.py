from copy import deepcopy
from halma.constants import COLS, ROWS, N_PIECES_PER_PLAYER
import random
import pygame

RED = (255, 0, 0)
GREEN = (0, 128, 0)

# takes in some board which is telling us the details of all the pieces on their
#
def minimax(position, depth, max_player, game):
    if depth == 0 or position.checkWin() != None:
        return position.evaluate(), position

    # decide if we need to maximize or minimize
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, GREEN, game ):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval,  best_move
    else:
        minEval = float( 'inf' )
        best_move = None
        for move in get_all_moves( position, RED, game ):
            evaluation = minimax( move, depth - 1, True, game )[0]
            minEval = min( minEval, evaluation )
            if minEval == evaluation:
                best_move = move

        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    # if skip:
    #     continue

    return board

def get_all_moves(board, color, game):
    moves = [] # store the new board
    for piece in board.get_all_pieces(color):
        valid_moves = board.availMoves(piece) # getting valid moves for that color
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves

# displaying how the AI is thinking on its move
def draw_moves(game, board, piece):
    valid_moves = board.availMoves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #  pygame.time.delay(100)


def simple_move(board, color):
    all_pieces = board.get_all_pieces(color)
    all_move_sets = {piece: board.availMoves(piece.row, piece.col, [], []) for piece in all_pieces}
    valid_move_set = {piece:move_set for piece, move_set in all_move_sets.items() if len(move_set) != 0}
    piece, this_move_set = random.choice(list(valid_move_set.items()))
    row, col = random.choice(this_move_set)
    return piece, row, col

# PSEUDO CODE !!
def alpha_beta_search(postion, depth, alpha, beta, max_player ):
    pass
    '''
   
    // Maximizing the Player 
    if depth  == 0 is a terminal node then 
    return static evaluation of postion 
    
    if max_player:
        max_Eval = ( -inf ) 
        for each piece in postion do:
            evaluate = minimax(psotion, depth - 1, alpha, beta, False) 
            max_Eval = max( max_Eval, evaluate) 
            alpha = max(alpha, max_Eval)
            if beta <= alpha
                break 
        return max_Eval 
    else:
    // Minimizing the Player 
    min_Eval = ( inf ) 
        for each piece in postion do:
            evaluate = minimax(psotion, depth - 1, alpha, beta, True) 
            min_Eval = max( max_Eval, eva) 
            beta = min(alpha, min_Eval)
            if beta <= alpha
                break 
        return minEva 
    '''




def winningUtility(board):
 pass
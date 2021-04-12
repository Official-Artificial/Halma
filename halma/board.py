import pygame
import easygui
from.constants import BLACK, ROWS, WHITE, SQUARE_SIZE, COLS, RED, BROWN, GREEN, N_PIECES_PER_PLAYER, BLUE
from.piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.green_left = 10
        self.red_pieces_place = 0
        self.green_pieces_place = 0
        self.redCamp = []
        self.greenCamp = []
        self.create_board()

    # drawing the board
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2 ):
                pygame.draw.rect(win, BROWN, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # move method
    def move(self, piece, row, col):
        # swap postions
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def nextMoves(self, player=1):
        moves = []
        for y in range(SQUARE_SIZE):#self.boardLW):
            for x in range(SQUARE_SIZE):#self.boardLW):
                if self.board[x][y] [1]!= player:
                    continue
                moves += self.availMoves(x, y, [], [])
        return moves

    def availMoves(self, x, y, moves, skip_tiles):
        for tempY in range(-1, 2):
            for tempX in range(-1, 2):
                newX = x + tempX
                newY = y + tempY
                if ((newX == x and newY == y) or newX < 0 or newY < 0 or newX >= SQUARE_SIZE or newY >= SQUARE_SIZE):
                    continue
                if (newX, newY) != (x,y):
                    moves += [(newX, newY)]
                skip_tiles += [(x, y)]
        return moves


    def get_piece(self, row, col):
        return self.board[row][col]

    def get_n_diagonals_per_player(self):
        total_diagonals = ROWS + COLS - 1
        N_Diagonals = 1
        n_pieces = 0
        while N_PIECES_PER_PLAYER > n_pieces:
            n_pieces += N_Diagonals
            N_Diagonals += 1
        return N_Diagonals -1

    # placing the pieces on the board
    def create_board(self):
        total_diagonals = ROWS + COLS - 1
        diagonals_per_player = self.get_n_diagonals_per_player()
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                    if row + col <= diagonals_per_player - 1:
                        self.board[row].append(Piece(row, col, RED))
                        self.red_pieces_place += 1

                    elif row + col >= total_diagonals - diagonals_per_player:
                        self.board[row].append( Piece( row, col, GREEN) )
                        self.green_pieces_place += 1
                #     self.board[row].append(Piece(row, col, GREEN))
                    else:
                        self.board[row].append(0)  # blank space

        count = 0
        from_bottom_left = True
        while self.red_pieces_place > N_PIECES_PER_PLAYER:
            if from_bottom_left:
                row_index = diagonals_per_player - 1 - count
                col_index = count
            else:
                row_index = count
                col_index = diagonals_per_player - 1 - count
                count += 1

            self.board[row_index][col_index] = 0
            self.red_pieces_place -= 1
            from_bottom_left = not from_bottom_left

        count = 0
        from_top_right = True
        while self.green_pieces_place > N_PIECES_PER_PLAYER:
            if from_top_right:
                row_index = ROWS - (diagonals_per_player) + count
                col_index = COLS - 1 - count
            else:
                col_index = ROWS - (diagonals_per_player) + count
                row_index = COLS - 1 - count
                count +=1
            self.board[row_index][col_index] = 0
            self.green_pieces_place -= 1
            from_top_right = not from_top_right

    # drawing all the pieces in the squares ( win = window )
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    # checking to see who has won the game
    def checkWin(currRed, curreGreen, winAmount):
        if currRed == winAmount:
            easygui.msgbox( 'Green Wins!', 'msgTitle' )
            return True
        elif curreGreen == winAmount:
            easygui.msgbox( 'Red Wins!', 'msgTitle' )
            return True
        else:
             return False
# #
# class Board:
#     def __init__(self):
#         self.board = []
#         self.boardLW = 8
#         self.currPlayer = "G"
#         self.nextMoves()
#         self.selected_piece = None
#         self.red_left = self.green_left = 10
#         self.red_pieces_place = 0
#         self.green_pieces_place = 0
#         self.create_board()
#         self.redCamp = []
#         self.greenCamp = []
#
#     # drawing the board
#     def draw_squares(self, win):
#         win.fill( BLACK )
#         for row in range( ROWS ):
#             for col in range( row % 2, COLS, 2 ):
#                 pygame.draw.rect( win, BROWN, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE) )
#
#     def select(self, row, col):
#         if self.selected:
#             result = self._move( row, col )
#             if not result:
#                 self.selected = None
#                 self.select( row, col )
#
#         piece = self.board.get_piece( row, col )
#         if piece != 0 and piece.color == self.turn:
#             self.selected = piece
#             self.valid_moves = self.board.get_valid_moves( piece )
#
#             # move method
#
#     def move(self, piece, row, col):
#         # check for invalid moves
#         if row < 0 or row >= 8 or col < 0 or col >= 8:
#             easygui.msgbox( 'Invalid Move!', 'Invalid Move!' )
#
#         # possibleMoves = nextMoves(
#             # swap postions
#             self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][
#             piece.col]
#         piece.move( row, col )
#
#         # once mouse is clicked row and col is
#
#         # Finds the current player and finds available moves from current position
#
#     def nextMoves(self, player):
#         moves = []
#         for y in range( self.boardLW ):
#             for x in range( self.boardLW ):
#                 if self.board[x][y][1] != player:
#                     continue
#                 moves += self.availMoves( x, y, [], [] )
#         return moves
#
#     # Searches for available moves at the given position
#     def availMoves(self, x, y, moves, skip_tiles):
#         for tempY in range( -1, 2 ):
#             for tempX in range( -1, 2 ):
#                 newX = x + tempX
#                 newY = y + tempY
#                 if ((newX == x and newY == y) or newX < 0 or newY < 0 or newX >= self.boardLW or newY >= self.boardLW):
#                     continue
#                 if self.board[newX][newY][1] == 0:
#                     moves += [((x, y), (newX, newY))]
#                 skip_tiles += [(x, y)]
#         return moves
#
#     def getHops(x, y):
#         jumps = []
#
#     for x in range( -1, 2 ):
#         for y in range( -1, 2 ):
#             if ((newX == x and newY == y) or newX < 0 or newY < 0 or newX >= self.boardLW or newY >= self.boardLW):
#                 continue
#
#         # drawing valid moves (highlighting where the piece can move to)
#
#     def draw_valid_moves(self, moves):
#         for move in moves:
#             row, col = move
#             pygame.draw.circle( self.win, BLUE,
#                                 (col * SQUARE_SIZE + SQAURE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15 )
#
#     def get_piece(self, row, col):
#         return self.board[row][col]
#
#     def get_n_diagonals_per_player(self):
#         total_diagonals = ROWS + COLS - 1
#         N_Diagonals = 1
#         n_pieces = 0
#         while N_PIECES_PER_PLAYER > n_pieces:
#             n_pieces += N_Diagonals
#             N_Diagonals += 1
#         return N_Diagonals - 1
#
#     # placing the pieces on the board
#     def create_board(self):
#         total_diagonals = ROWS + COLS - 1
#         diagonals_per_player = self.get_n_diagonals_per_player()
#         for row in range( ROWS ):
#             self.board.append( [] )
#             for col in range( COLS ):
#                 if row + col <= diagonals_per_player - 1:
#                     self.board[row].append( Piece( row, col, RED, player="player 1" ) )
#                     self.red_pieces_place += 1
#
#                 elif row + col >= total_diagonals - diagonals_per_player:
#                     self.board[row].append( Piece( row, col, GREEN, player="player 2" ) )
#                     self.green_pieces_place += 1
#                 #     self.board[row].append(Piece(row, col, GREEN))
#                 else:
#                     self.board[row].append( 0 )  # blank space
#
#         count = 0
#         from_bottom_left = True
#         while self.red_pieces_place > N_PIECES_PER_PLAYER:
#             if from_bottom_left:
#                 row_index = diagonals_per_player - 1 - count
#                 col_index = count
#             else:
#                 row_index = count
#                 col_index = diagonals_per_player - 1 - count
#                 count += 1
#
#             self.board[row_index][col_index] = 0
#             self.red_pieces_place -= 1
#             from_bottom_left = not from_bottom_left
#
#         count = 0
#         from_top_right = True
#         while self.green_pieces_place > N_PIECES_PER_PLAYER:
#             if from_top_right:
#                 row_index = ROWS - (diagonals_per_player) + count
#                 col_index = COLS - 1 - count
#             else:
#                 col_index = ROWS - (diagonals_per_player) + count
#                 row_index = COLS - 1 - count
#                 count += 1
#             self.board[row_index][col_index] = 0
#             self.green_pieces_place -= 1
#             from_top_right = not from_top_right
#
#     def get_valid_moves(self, piece):
#         moves = {}
#         left = piece.col - 1
#         right = piece.col + 1
#         row = piece.row
#
#         if piece.color == RED:
#             moves.update( self._transverse_left( row - 1, max( row - 3, -1 ), -1, piece.color, left ) )
#             moves.update( self._transverse_right( row - 1 ), max( row - 3, -1 ), -1, piece.color, right ))
#             if piece.color == GREEN:
#                 moves.update( self._transverse_left( row + 1, max( row + 3, ROWS ), 1, piece.color, left ) )
#             moves.update( self._transverseright( row + 1, max( row + 3, ROWS ), 1, piece.color, right ) )
#
#         return moves
#
#     # piece moving left transversal
#     def _transverse_left(self, start, stop, step, color, left, skipped=[])
#         moves = {}
#         last = []
#         for row in range( start, stop, step ):
#             if left < 0:
#                 break
#
#             current = self.board[row][left]
#             if current == 0:
#                 if skipped and not last:
#                     break
#             elif skipped:
#                 moves[(row, left)] = last + skipped
#             else:
#                 moves[(row, left)] = last
#
#             if last:
#                 if step == -1:
#                     row = max( row - 3, 0 )
#                 else:
#         row = min( row + 3, ROWS )
#
#
#             moves.update( self._traverse_left( row + step, row, step, color, left - 1, skipped=last ) )
#             moves.update( self._traverse_right( row + step, row, step, color, left + 1, skipped=last ) )
#         break
#         elif current.color == color:
#         break
#         else:
# last = [current]
# left -= 1
# return moves
#
#
# # piece moving right transversal
# def _transverse_right(self, start, stop, step, color, right, skipped=[])
#     moves = {}
#     last = []
#     for row in range( start, stop, step ):
#         if right >= COLS:
#             break
#
#         current = self.board[row][left]
#         if current == 0:
#             if skipped and not last:
#                 break
#     elif skipped:
#     moves[(row, right)] = last + skipped
#
# else:
# moves[(row, right)] = last
#
# if last:
#     if step == -1:
#         row = max( row - 3, 0 )
#     else:
#         row = min( row + 3, ROWS )
# moves.update( self._traverse_left( row + step, row, step, color, right - 1, skipped=last ) )
# moves.update( self._traverse_right( row + step, row, step, color, right + 1, skipped=last ) )
# break
# elif current.color == color:
# break
# else:
# last = [current]
# left -= 1
# return moves
#
#
# # detects who is the winner with the given board
# def winLoss(self):
#     # Title of the pop up window
#     msgTitle = "Winner"
#     # variables to see how many colors are at each others camp
#     # greenAtRedCamp = 0
#     # redAtGreenCamp = 0
#
#     # looks at red corner
#     # How many rows this will go through
#     for rowLength in range( 0, (COLS // 2) ):
#         # length of the row becomes shorter so that the pieces are placed in a triangle form
#         for colLength in range( 0, (ROWS - rowLength) ):
#             self.redCamp.append( (rowLength, colLength) )
#
#     for rows in range( ROWS // 2 ):
#         rowNum = (COLS // 2) - ((COLS // 2) - rows)
#         # this will start at the right and move its way left
#         rowLength = ROWS - 1 - rows
#         rowLengthLimit = ROWS
#         for colLength in range( rowLength, rowLengthLimit ):
#             self.greenCamp.append( (rowNum, colLength) )
#
#     for coord in self.greenCamp:
#         # checks to make sure that the red piece is in the green corner
#         if not self.get_piece( coord[0], coord[1] ):
#             # if one of the pieces is not in the green camp then red is not the winner
#             break
#         else:
#             easygui.msgbox( "Red Wins!", msgTitle )
#             return True
#
#     for coord in self.redCamp:
#         # check to make sure that the green piece is in the red corner
#         if not self.get_piece( coord[0], coord[1] ):
#             # if one of the pieces is not in the red camp then green is not the winner
#             break
#         else:
#             easygui.msgbox( "Green Wins!", msgTitle )
#             return True
#
#     return False
#
#
# # drawing all the pieces in the squares ( win = window )
# def draw(self, win):
#     self.draw_squares( win )
#     for row in range( ROWS ):
#         for col in range( COLS ):
#             piece = self.board[row][col]
#             if piece != 0:
#                 piece.draw( win )
#
#
# def checkWin(currRed, curreGreen, winAmount):
#     if currRed == winAmount:
#         easygui.msgbox( 'Green Wins!', msgTitle )
#         return True
#
#     else if currGreen == winAmount:
#         easygui.msgbox( 'Red Wins!', msgTitle )
#         return True
#
#     else:
#     return False

import pygame
import easygui
from.constants import BLACK, ROWS, SQUARE_SIZE, COLS, RED, BROWN, GREEN, N_PIECES_PER_PLAYER, BLUE
from.piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.moves = []
        self.player = GREEN
        self.selected_piece = None
        self.red_left = self.green_left = 10
        self.red_pieces_place = 0
        self.green_pieces_place = 0
        self.movePieces = 0
        self.redCamp = []
        self.greenCamp = []
        self.create_board()

    # drawing the board
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2 ):
                pygame.draw.rect(win, BROWN, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def drawV(self,win,moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(win, GREY,(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15 )

    # returns some postive or negative number score of this board
    def evalute(self):
        return self.green_left - self.red_left

    # return the pieces of a certian color
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    # move method
    def move(self, piece, row, col):
        # swap postions
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def nextMoves(self, player=1):
        moves = []
        for y in range(SQUARE_SIZE):
            for x in range(SQUARE_SIZE):
                if self.board[x][y] [1]!= player:
                    continue
                moves += self.availMoves(x, y, [], [])
        return moves

    def availMoves(self, x, y, moves, skip_tiles):
        for tempY in range(-1, 2):
            for tempX in range(-1, 2):
                newX = x + tempX
                newY = y + tempY
                if ((newX == x and newY == y) or newX < 0 or newY < 0 or newX >= ROWS - 1 or newY >= COLS -1):
                    continue
                if (newX, newY) != (x,y):
                    moves += [(newX, newY)]
        bad_moves = []
        for i in moves:
             if self.get_piece(i[0], i[1]) != 0:
                 bad_moves.append(i)
        for move in bad_moves:
            moves.remove(move)
        self.moves = []
        self.moves = moves
        return moves

    def get_piece(self, row, col):
        try:
            return self.board[row][col]
        except:
            print( "index out of bounds" )

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
        self.drawV( win, self.moves )
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def winLoss(self):
        # Title of the pop up window
        # variables to see how many colors are at each others camp
        greenAtRedCamp = 0
        redAtGreenCamp = 0
        counter = 0

        # looks at red corner
        # How many rows this will go through
        for rowLength in range( 0, (COLS // 2) ):
            # length of the row becomes shorter so that the pieces are placed in a triangle form
            for colLength in range( 0, (ROWS // 2 - rowLength) ):
                self.redCamp.append( (rowLength, colLength) )

        for counter in range( 0, COLS // 2 + 1 ):
            beginningRow = ((COLS // 2) * 2) - ((COLS // 2) - counter) - 1
            beginningCol = (COLS - 1) - counter
            for col in range( COLS - 1, beginningCol, -1 ):
                self.greenCamp.append( (beginningRow, col) )

        for coord in self.greenCamp:
            boardPiece = self.get_piece(coord[0], coord[1])
            # checks to make sure that the red piece is in the green corner
            if boardPiece.color == RED:
                redAtGreenCamp += 1
            elif boardPiece.color == GREEN:
                # if one of the pieces is not in the green camp then red is not the winner
                break

        for coord in self.redCamp:
            boardPiece = self.get_piece(coord[0], coord[1])
            # check to make sure that the green piece is in the red corner
            if boardPiece.color == GREEN:
                greenAtRedCamp += 1
            elif boardPiece.color == RED:
                # if one of the pieces is not in the red camp then green is not the winner
                break

        return self.checkWin( redAtGreenCamp, greenAtRedCamp, N_PIECES_PER_PLAYER )

    # checking to see who has won the game
    def checkWin(self, currRed, curreGreen, winAmount):
        msgTitle = "Winner"
        if currRed == winAmount:
            easygui.msgbox( 'Red Wins!', msgTitle )
            return True
        elif curreGreen == winAmount:
            easygui.msgbox( 'Green Wins!', msgTitle )
            return True
        else:
            return False

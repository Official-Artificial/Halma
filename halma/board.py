import pygame
from.constants import BLACK, ROWS, WHITE, SQUARE_SIZE, COLS, RED, BROWN, GREEN, N_PIECES_PER_PLAYER
from.piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.green_left = 10
        self.red_pieces_place = 0
        self.green_pieces_place = 0
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
        for y in range(self.boardLW):
            for x in range(self.boardLW):
                if self.board[x][y][1] != player:
                    continue
                moves += self.availMoves(x, y, [], [])
        return moves

    def availMoves(self, x, y, moves, skip_tiles):
        for tempY in range(-1, 2):
            for tempX in range(-1, 2):
                newX = x + tempX
                newY = y + tempY
                if ((newX == x and newY == y) or newX < 0 or newY < 0 or newX >= self.boardLW or newY >= self.boardLW):
                    continue
                if self.board[newX][newY][1] == 0:
                    moves += [((x, y), (newX, newY))]
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

    # # placing the pieces on the board
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
                        self.board[row].append( Piece( row, col, GREEN ) )
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

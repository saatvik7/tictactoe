# This file defines a Board Class for the game of Tic Tac Toe

from typing import Tuple, Set
class Board:
    def __init__(self) -> None:
        """ Initialize a Board object """
        self.board = [[" "]*3 for _ in range(3)]
        self.winner = None
        self.draw = False


    def __repr__(self) -> str:
        """ repr allows us to print the Board """
        board_str = "-------\n"
        for row in self.board:
            board_str += f"|"
            for col in row:
                board_str += f"{col}|"
            board_str += "\n-------\n"
        return board_str


    def __check_win(self, row:int, col:int) -> None:
        """ Checks if either player has won on this board, given
            starting square and sets winner variable
        """
        piece = self.board[row][col]
        row_count = 0
        col_count = 0
        diag1_count = 0
        diag2_count = 0
        # check current row
        for j in range(3):
            if self.board[row][j] == piece:
                row_count += 1
        # check current col
        for i in range(3):
            if self.board[i][col] == piece:
                col_count += 1
        # check both diagonals
        for i, j in [(0,0), (1,1), (2, 2)]:
            if self.board[i][j] == piece:
                diag1_count += 1
        for i, j in [(0,2), (1,1), (2, 0)]:
            if self.board[i][j] == piece:
                diag2_count += 1
        # if any of them make a line of 3, we have a winner
        if row_count == 3 or col_count == 3 or diag1_count == 3 or diag2_count == 3:
            self.winner = piece


    def empty_slots(self) -> Set[Tuple[int, int]]:
        """ Returns list of empty coordinates in the board """
        results = set()
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == " ":
                    results.add((i, j))
        return results


    def insert(self, piece:str, row:int, col:int) -> bool:
        """ insert allows us to insert an X or O into the board.
            returns True if insert was successful, else False.
        """
        empty_slots = self.empty_slots()
        if (row, col) in empty_slots:
            self.board[row][col] = piece
            self.__check_win(row, col)
            if not self.winner and len(empty_slots) <= 1:
                self.draw = True
            return True
        return False


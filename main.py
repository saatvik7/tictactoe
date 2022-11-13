# This file runs the entire Tic Tac Toe Meta Game

from tictactoe import TicTacToe
from player import Player

if __name__ == "__main__":
    p1_type = None
    p2_type = None
    while p1_type not in ["human", "computer"]:
        p1_type = input("Player 1 will play with X. Please enter if they will play as a human or as a computer: ")
    while p2_type not in ["human", "computer"]:
        p2_type = input("Player 2 will play with O. Please enter if they will play as a human or as a computer: ")
    p1 = Player("X", p1_type)
    p2 = Player("O", p2_type)
    is_p1 = True
    meta_game = TicTacToe()
    while not meta_game.game_over and not meta_game.quit:
        if is_p1:
            meta_game.play_move(p1, 1)
        else:
            meta_game.play_move(p2, 2)
        is_p1 = not is_p1



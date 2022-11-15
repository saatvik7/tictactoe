# This file defines a TicTacToe Class, which plays a game of TicTacToe

from board import Board
from player import Player
from typing import Optional, Tuple
import random

class TicTacToe:
    def __init__(self) -> None:
        """ Initialize a TicTacToe object """
        self.boards = [[Board() for _ in range(3)] for _ in range(3)]
        self.meta_board = Board()
        self.game_over = False
        # This stores the set of valid boards that both players can move in
        self.valid_boards = set(list(range(9)))
        self.quit = False


    def __human_move(self, player_num:int) -> Optional[Tuple[int, Tuple[int, int], Board, Tuple[int, int]]]:
        """ This function gathers all the information required to make a move from a human player.
            Returns game_num, game_coords, cur_board, and board_coords
        """
        game_num = None
        valid_games = sorted(list(self.valid_boards))
        print(f"Player {player_num}'s Turn")
        while game_num not in self.valid_boards:
            try:
                game_num = int(input(f"Select a valid game number from {valid_games}: "))
            except EOFError as e:
                self.quit = True
                return
            except:
                print("Please enter a valid game number")
                continue
        game_coords = (game_num//3, game_num%3)
        curr_board = self.boards[game_coords[0]][game_coords[1]]
        board_coords = None
        empty_slots = curr_board.empty_slots()
        print(f"You selected board {game_num}, which looks like:")
        print(curr_board)
        while board_coords not in empty_slots:
            try:
                board_row = int(input(f"Select a valid row from {set([x[0] for x in empty_slots])}: "))
                board_col = int(input(f"Select a valid col from {set([x[1] for x in empty_slots])}: "))
                board_coords = (board_row, board_col)
            except EOFError as e:
                self.quit = True
                return
            except:
                print("Please enter a valid row/col")
                continue
        return (game_num, game_coords, curr_board, board_coords)


    def __check_meta_game(self, player_num:int) -> bool:
        """
        Checks the meta game for a win or a draw and prints appropriate output.
        """
        if self.meta_board.winner:
            print(f"Player {player_num} has won the Meta Game. Congratulations!")
            return True
        elif self.meta_board.draw:
            print(f"The Meta Game has ended in a draw. Well played both players.")
            return True
        return False


    def play_move(self, player:Player, player_num:int) -> None:
        """ This function plays next move in the game
            for a given player.
        """
        try:
            if player.player_type == "human":
                game_num, game_coords, curr_board, board_coords = self.__human_move(player_num)
            else:
                game_num = random.choice(list(self.valid_boards))
                game_coords = (game_num//3, game_num%3)
                curr_board = self.boards[game_coords[0]][game_coords[1]]
                board_coords = random.choice(list(curr_board.empty_slots()))
            # make a move on the chosen board at the chosen square
            curr_board.insert(player.piece, board_coords[0], board_coords[1])
            print(f"Player {player_num} moved to {board_coords} on board {game_num}. This is how it looks:")
            print(curr_board)
            if curr_board.winner:
                self.valid_boards.remove(game_num)
                self.meta_board.insert(player.piece, game_coords[0], game_coords[1])
                print(f"Player {player_num} wins the game instance at board {game_num}.")
                print(f"This is how the meta-game board looks: ")
                print(self.meta_board)
            elif curr_board.draw:
                print(f"The game instance at board {game_num} has a draw. A new instance of the game will be started at that board.")
                self.boards[game_coords[0]][game_coords[1]] = Board()
            if self.__check_meta_game(player_num):
                self.game_over = True
        except:
            return


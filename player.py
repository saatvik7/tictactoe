# This file defines a Player Class, for the game of Tic Tac Toe

class Player:
    def __init__(self, piece:str, player_type:str) -> None:
        """
        Initializes a Player for the game
        piece is either "X" or "O"
        player_type is either "human" or "computer"
        """
        self.piece = piece
        self.player_type = player_type

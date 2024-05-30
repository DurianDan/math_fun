from typing import List, Literal

PLAYER_MOVE = Literal["u", "d", "l", "r"]


class PlayerPointer:
    def __init__(self, horizontal_index, vertical_index) -> None:
        self.horizontal_index = horizontal_index
        self.vertical_index = vertical_index

    def is_out_of_board(self) -> bool:
        horizontal_out = self.horizontal_index > 9 or self.horizontal_index < 0
        vertical_out = self.vertical_index > 9 or self.vertical_index < 0
        return horizontal_out or vertical_out


class PlayerRounds:
    def __init__(
        self,
        player1: PlayerPointer,
        player2: PlayerPointer,
        player1_moves: List[PLAYER_MOVE],
        player2_moves: List[PLAYER_MOVE],
    ) -> None:
        self.player1: PlayerPointer = player1
        self.player2: PlayerPointer = player2
        self.player1_moves: List[PLAYER_MOVE] = player1_moves
        self.player2_moves: List[PLAYER_MOVE] = player2_moves

    def check_player1_on_old_location(self) -> bool:
        
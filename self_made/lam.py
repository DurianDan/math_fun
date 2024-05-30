# // const player1Moves = ['r', 'd', 'd', 'r', 'r', 'r', 'l', 'l', 'l', 'd', 'd', 'd', 'l', 'd', 'd', 'd', 'd', 'r'];
# // const player2Moves = ['u', 'l', 'l', 'u', 'l', 'l', 'u', 'l', 'l', 'd', 'd', 'l', 'l', 'u', 'u', 'r', 'u', 'l'];
# Player 1 starts on position 0x0 (top left corner). Player 2 starts on position 9x9
# Player can move 'u', 'd', 'l', and 'r'
# A pointer track players location, whenever a player moves, we move his pointer accordingly 
# -> it needs horizontal, vertical coordinates on the board
  # horz_index, vert_index ranges from 0 -> 9
# A collection stores previous moves of both players, list/set, check if current location of 
# the player is already in the collection or not (lookup) -> set O(1) time complexity on average
  # if the player is not eliminated, we add his location to set
# Conditions that a player is eliminated
  # Both players lands to the same space
  # The player move out of the board
  # The current location of the player is in the set
# Conditions that leads a draw game
  # Both players are eliminated on the same turn
  # Those 2 players still alive

import copy

class Pointer:
    def __init__(self, horizontal_index, vertical_index) -> None:
        self.h = horizontal_index
        self.v = vertical_index
    def move(self, direction):
        if direction == "u":
            self.v -= 1
        elif direction == "d":
            self.v += 1
        elif direction == "l":
            self.h -= 1
        elif direction == "r":
            self.h += 1
        else:
            raise Exception("Invalid move")
    def __eq__(self, __value: object) -> bool:
        return self.h == __value.h and self.v == __value.v
    def __hash__(self) -> int:
        # An unique pointer unit is (h,v)
        return hash(f"{self.h}_{self.v}")
    def is_out_of_board(self):
        return self.h < 0 or self.h > 9 or self.v < 0 or self.v > 9
    def is_in_the_set(self, moves):
        return self in moves
    def __str__(self) -> str:
        return f"{self.h}_{self.v}"

def run(player_1_moves, player_2_moves):
    moves = set()
    player_1_pointer = Pointer(0, 0)
    player_2_pointer = Pointer(9, 9)
    is_player_1_eliminated = False
    is_player_2_eliminated = False
    for i in range(len(player_1_moves)):
        player_1_pointer.move(player_1_moves[i])
        player_2_pointer.move(player_2_moves[i])
        player_1_pointer_cp = copy.deepcopy(player_1_pointer)
        player_2_pointer_cp = copy.deepcopy(player_2_pointer)
        print([str(item) for item in moves])
        print(f"Player 1 is at (h={player_1_pointer_cp.h},v={player_1_pointer_cp.v})")
        print(f"Player 2 is at (h={player_2_pointer_cp.h},v={player_2_pointer_cp.v})")
        print("\n")
        if player_1_pointer_cp.__eq__(player_2_pointer_cp):
            is_player_1_eliminated = True
            is_player_2_eliminated = True
            break
        else:
            is_player_1_eliminated = player_1_pointer_cp.is_out_of_board() or player_1_pointer_cp.is_in_the_set(moves)
            is_player_2_eliminated = player_2_pointer_cp.is_out_of_board() or player_2_pointer_cp.is_in_the_set(moves)
            if is_player_1_eliminated or is_player_2_eliminated:
                break
            else:
                moves.add(player_1_pointer_cp)
                moves.add(player_2_pointer_cp)
    if is_player_1_eliminated and is_player_2_eliminated:
        print("Draw")
    else:
        if (not is_player_1_eliminated) and (not is_player_2_eliminated):
            print("Draw")
        else:
            if is_player_1_eliminated:
                print("Player 2 wins")
            else:
                print("Player 1 wins")

if __name__ == "__main__":
    player1Moves = ["r","d","d","r","r","r","l","l","l","d","d","d","l","d","d","d","d","r"]
    player2Moves = ["u","l","l","u","l","l","u","l","l","d","d","l","l","u","u","r","u","l"]
    run(player1Moves, player2Moves)
    
    # Analysis
        # Time complexity: O(n)
        # Space complexity: O(n)
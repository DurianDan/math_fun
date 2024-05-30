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

from typing import Tuple, List, Literal
from copy import copy

player1Moves = ["r","d","d","r","r","r","l","l","l","d","d","d","l","d","d","d","d","r"]
player2Moves = ["u","l","l","u","l","l","u","l","l","d","d","l","l","u","u","r","u","l"]

PLAYER_POINTER = Tuple[int, int]
PLAYER_MOVE = Literal["u", "d", "l", "r"]

player1 = [0, 0]
player2 = [9, 9]
oldLocations: List[PLAYER_POINTER] = []


def checkPlayerOutOfBoard(player: PLAYER_POINTER) -> bool:
    vert, horz = player
    vertOut = vert > 9 or vert < 0
    horzOut = horz > 9 or horz < 0
    return vertOut or horzOut


def checkOnOldLocations(player: PLAYER_POINTER) -> bool:
    return player in oldLocations


def check2PlayersSameLocation(player1: PLAYER_POINTER, player2: PLAYER_POINTER) -> bool:
    return player1 == player2


def movePlayer(move: PLAYER_MOVE, player: PLAYER_POINTER) -> PLAYER_POINTER:
    if move == "d":
        player[0] += 1
    if move == "u":
        player[0] -= 1
    if move == "l":
        player[1] -= 1
    if move == "r":
        player[1] += 1
    return player


def checkEndResult(
    player1: PLAYER_POINTER, player2: PLAYER_POINTER, round: int
) :
    if round == len(player1Moves)-1:
        return "Draw"
    elif player1 is None:
        if player2 is None:
            return "Draw"
        else:
            return "Player2 Win"
    elif player2 is None:
        return "Player1 Win"
    return False


for round in range(len(player1Moves)):
    print(f"\nRound: {round}___________")
    print(f"{player1 = }")
    print(f"{player2 = }")
    print(f"{oldLocations = }")

    player1 = movePlayer(player1Moves[round], player1)
    player2 = movePlayer(player2Moves[round], player2)
    if checkPlayerOutOfBoard(player1) or checkOnOldLocations(player1):
        player1 = None
    if checkPlayerOutOfBoard(player2) or checkOnOldLocations(player2):
        player2 = None

    result = checkEndResult(player1, player2, round)

    if result: print(result); break
    if check2PlayersSameLocation(player2, player1):
        print("Draw")
        break
    oldLocations.extend([copy(player2), copy(player1)])

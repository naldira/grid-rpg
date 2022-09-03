import pytest

from game_tools.gridboard import *


def test_board_creation_success():
    board1 = Board((5, 5))
    assert board1.map_size == (5, 5)
    assert board1.player_pos == [1, 1]
    assert 2 < board1.dragon_pos[0] < 6 and 2 < board1.dragon_pos[1] < 6
    assert 2 < board1.door_pos[0] < 6 and 2 < board1.door_pos[1] < 6
    with pytest.raises(ValueError):
        board2 = Board([1, 2])


def test_allowed_moves_success():
    board1 = Board((6, 6))
    assert board1.allowed_moves([1, 1]) == (False, True, False, True)
    assert board1.allowed_moves([2, 2]) == (True, True, True, True)
    assert board1.allowed_moves([6, 6]) == (True, False, True, False)
    with pytest.raises(ValueError):
        board1.allowed_moves((1, 1))


def test_move_entities_success():
    board1 = Board((5, 5))
    board1.move(board1.player_pos, 'down')
    assert board1.player_pos == [1, 2]
    dragon_x = board1.dragon_pos[0]
    dragon_y = board1.dragon_pos[1]
    board1.move(board1.dragon_pos, 'left')
    assert board1.dragon_pos == [(dragon_x - 1), dragon_y]
    with pytest.raises(ValueError):
        board1.move(board1.dragon_pos, 'r')





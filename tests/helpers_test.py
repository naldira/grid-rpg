import pytest

from game_tools.helpers import *
from math import dist


def test_calculate_distance_between_two_points_success():
    with pytest.raises(TypeError):
        assert Helpers.calc_distance(1, 1)
        assert Helpers.calc_distance((1, 'a'),(1, 2))
    assert Helpers.calc_distance((1, 1), (5, 3)) == dist((1, 1), (5, 3))
    assert Helpers.calc_distance((2, 3), (2, 3)) == 0


def test_point_comparison_direction_success():
    with pytest.raises(TypeError):
        assert Helpers.point_comparison('a', 'b')
        assert Helpers.point_comparison((1, 1), ('a', 1))
    assert Helpers.point_comparison((1, 1), (1, 2)) == 'up'
    assert Helpers.point_comparison((2, 2), (2, 2)) == 'no move'


def test_get_difficulty_success(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'easy')
    assert Helpers.get_difficulty() == 'easy'


def test_start_or_test_success(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'test')
    assert Helpers.start_or_test() == 'test'


def test_get_dimensions_success(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'small')
    assert Helpers.get_dimensions() == (5, 5)


def test_get_directions_success(monkeypatch):
    with pytest.raises(ValueError):
        Helpers.get_direction((False, False, False, False))
    monkeypatch.setattr('builtins.input', lambda _: 'up')
    assert Helpers.get_direction((True, True, False, False)) == 'up'

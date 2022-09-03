import pytest

from game_tools.entities import *


def test_dragon_creation():
    default_dragon = Dragon()
    assert default_dragon.name == 'dragon'
    assert default_dragon.sight == 1
    assert default_dragon.hearing == 4
    custom_dragon = Dragon(name='asd')
    assert custom_dragon.name == 'asd'
    with pytest.raises(ValueError):
        sample_dragon = Dragon('ez')


def test_dragon_check_by_hearing():
    sample_dragon = Dragon('normal')
    assert sample_dragon.check_by_hearing(2, odds=10) is True
    assert sample_dragon.check_by_hearing(6) is False
    results = []
    for runs in range(50):
        results.append(sample_dragon.check_by_hearing(2))
    assert True in results


def test_dragon_check_by_sight():
    sample_dragon = Dragon()
    assert sample_dragon.check_by_sight(1) is True
    assert sample_dragon.check_by_sight(2) is False


def test_player_creation():
    default_player = Player()
    assert default_player.name == 'player'
    assert default_player.sight == 2
    custom_player = Player(name='cp')
    assert custom_player.name == 'cp'
    with pytest.raises(ValueError):
        player1 = Player(difficulty='ez')


def test_player_check_by_sight():
    player1 = Player()
    assert player1.check_by_sight(2) is True
    assert player1.check_by_sight(3) is False

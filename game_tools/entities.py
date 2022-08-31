from random import randint
import logging


"""
contains characters used in the game.
"""


class Character:
    """
    Character class for all non-item entities.
    """

    def __init__(self, name: str) -> None:
        self.name = name


class Dragon(Character):
    """
    dragon class with a default dragon name.
    """

    def __init__(self, difficulty: str = 'normal', name: str = 'dragon') -> None:
        Character.__init__(self, name)
        self.status = 'alive'
        self.sight = difficulty
        self.hearing = difficulty

    @property
    def sight(self) -> int:
        """
        getter for sight attribute which is the range in which the dragon
        can hear the player to move toward.
        """
        return self._sight

    @sight.setter
    def sight(self, difficulty: str) -> None:
        """
        setter for sight attribute, info logs and raises a value error if
        difficulty passed to dragon is not in a pre-defined list.
        """
        difficulty_list = ['easy', 'normal', 'hard']
        if difficulty in difficulty_list:
            if difficulty == 'easy':
                self._sight = 0
            if difficulty == 'normal':
                self._sight = 1
            if difficulty == 'hard':
                self._sight = 2
        else:
            logging.info(f'{difficulty} is an invalid difficulty for dragon')
            raise ValueError(f"{difficulty} is not a valid difficulty")

    @property
    def hearing(self) -> int:
        """
        getter for hearing attribute which is the range in which
        the dragon can see the player to move toward.
        """
        return self._hearing

    @hearing.setter
    def hearing(self, difficulty: str) -> None:
        """
        setter for sight attribute, info logs and raises a value error if
        difficulty passed to dragon is not in a pre-defined list.
        """
        difficulty_list = ['easy', 'normal', 'hard']
        if difficulty in difficulty_list:
            if difficulty == 'easy':
                self._hearing = 2
            if difficulty == 'normal':
                self._hearing = 4
            if difficulty == 'hard':
                self._hearing = 6
        else:
            logging.info(f'{difficulty} is an invalid difficulty for dragon')
            raise ValueError(f"{difficulty} is not a valid difficulty")

    def dragon_sight(self, distance: float, odds: int = 10) -> bool:
        """
        allows the dragon to move toward player based on the
        given distance and success chance (default is 100%).

        Parameters
        ----------
        distance: float :
            distance between dragon and player.
        odds: int :
             (Default value = 10)
            the chance for activation where each point is 10%,
            default 100% for sight.
        Returns
        -------
        Bool:
            whether the dragon will toward player or not.
        """
        move = False
        if randint(1, 10) < odds:
            if self.sight >= distance:
                move = True
        return move

    def dragon_hearing(self, distance: float, odds: int = 3) -> bool:
        """
        allows the dragon to move toward player based on the
        given distance and success chance (default is 30%).

        Parameters
        ----------
        distance: float :
            distance between dragon and player.
        odds: int :
             (Default value = 3)
            the chance for activation where each point is 10%,
            default 30% for hearing.
        Returns
        -------
        Bool:
            whether the dragon will toward player or not.
        """
        move = False
        if randint(0, 10) < odds:
            if self.hearing >= distance > self.sight:
                move = True
        return move


class Player(Character):
    """
    player class with a player default name
    """

    def __init__(self, difficulty: str = 'normal', name: str = 'player') -> None:
        Character.__init__(self, name)
        self.status = 'alive'
        self.sight = difficulty

    @property
    def sight(self) -> int:
        """
        getter for sight attribute which is the range in which
        the player can see entities on the map.
        """
        return self._sight

    @sight.setter
    def sight(self, difficulty: str) -> None:
        """
        setter for sight attribute, info logs and raises a value error if
        difficulty passed to dragon is not in a pre-defined list.
        """
        difficulty_list = ['easy', 'normal', 'hard']
        if difficulty in difficulty_list:
            if difficulty == 'easy':
                self._sight = 3
            if difficulty == 'normal':
                self._sight = 2
            if difficulty == 'hard':
                self._sight = 1
        else:
            logging.info(f'{difficulty} is an invalid difficulty for player')
            raise ValueError(f"{difficulty} is not a valid difficulty")

    def player_sight(self, distance: float) -> bool:
        """
        allows player to see the content of cells around it.

        Parameters
        ----------
        distance: float :
            distance between player and target cell.

        Returns
        -------
        Bool:
            whether player can see the content of given cell.
        """
        if distance <= self.sight:
            can_see = True
        else:
            can_see = False
        return can_see


# tests
if __name__ == '__main__':
    dragon = Dragon('hard')
    for key, value in dragon.__dict__.items():
        print(f"{key} is {value}")
    player = Player()
    for key, value in player.__dict__.items():
        print(f"{key} is {value}")
    print(dragon.dragon_hearing(3))
    print(player.player_sight(2))

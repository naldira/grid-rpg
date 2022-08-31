from math import sqrt
from os import system, name
from typing import (Tuple,
                    NewType,
                    Annotated)

"""
contains classes with methods that are used in calculations in
other parts of the program.
"""

coords_tuple = NewType('coords_tuple', tuple[int, int])
coords_list = NewType('coords_list', list[int, int])


class Helpers:
    """
    only contains static methods needed for the program to run.
    seperated to declutter other classes.
    """
    direction_list = ['up', 'down', 'left', 'right', 'quit']

    @staticmethod
    def calc_distance(first_coords: coords_tuple,
                      second_coords: coords_tuple) -> float:
        """
        calculates the distance between 2 points.

        Parameters
        ----------
        first_coords: tuple[int, int] :
            X, Y coordinates of the first point.
        second_coords: tuple[int, int] :
            X, Y coordinates of the second point.
        Returns
        -------
        Float:
            the distance between the 2 given points.
        """
        x_distance = first_coords[0] - second_coords[0]
        y_distance = first_coords[1] - second_coords[1]
        distance = sqrt(x_distance ** 2 + y_distance ** 2)
        return distance

    @staticmethod
    def clear_board() -> None:
        """
        clears the terminal.
        """
        system('cls' if name == 'nt' else 'clear')

    @staticmethod
    def point_comparison(point1: coords_list,
                         point2: coords_list) -> str:
        """
        shows the direction in which entity at second point has to take
        to get closer to entity at first point.

        Parameters
        ----------
        point1: tuple[int, int] :
            X, Y coordinates of the first point. (the one that has to move).
        point2: tuple[int, int] :
            X, Y coordinates of the second point. (target cell).

        Returns
        -------
        str:
            the UP/DOWN/LEFT/RIGHT direction to get closer, 'no move'
            if they're at the same location.
        """
        x_diff = point1[0] - point2[0]
        y_diff = point1[1] - point2[1]
        direction = None
        if point1 == point2:
            direction = 'no move'
        # the direction entity at point2 should take to get closer to point1
        if abs(x_diff) >= abs(y_diff) and x_diff > 0:
            direction = 'right'
        elif abs(x_diff) >= abs(y_diff) and x_diff < 0:
            direction = 'left'
        elif abs(x_diff) <= abs(y_diff) and y_diff > 0:
            direction = 'down'
        elif abs(x_diff) <= abs(y_diff) and y_diff < 0:
            direction = 'up'
        return direction.lower()

    @staticmethod
    def get_difficulty() -> str:
        """
        gets difficulty based on user input.
        Returns
        -------
        str:
            game's difficulty
        """
        print('\neasy: higher sight for player and '
              'lower sight and hearing for dragon')
        print('\nnormal: lower sight for player and'
              ' normal sight and hearing for dragon')
        print('\nhard: minimum sight for player and'
              ' higher sight and hearing for dragon\n')
        while True:
            difficulty_list = ['easy', 'normal', 'hard']
            difficulty = input('please enter difficulty '
                               '(EASY, NORMAL, HARD): \n')
            if difficulty.lower() == 'quit':
                quit()
            elif difficulty.lower() in difficulty_list:
                break
        return difficulty.lower()

    @staticmethod
    def start_or_test() -> str:
        """
        gets game mode (start = normal, test = debug)
        -------
        str:
            game mode
        """
        while True:
            options = ['start', 'test']
            choice = input('enter START to start, or TEST to'
                           ' enter debug mode, or QUIT to exit: \n')
            if choice.lower() == 'quit':
                quit()
            elif choice.lower() in options:
                break
        return choice.lower()

    @staticmethod
    def get_dimensions() -> coords_tuple:
        """
        gets game dimensions from player input. 3 predefined sizes
        of small, medium and large squares, also supports custom
        dimensions(even rectangle)
        raises value error if cast to int fails.
        -------
        tuple[int, int]:
            a tuple containing width and height of the grid
        """
        print('\nsmall: 6x6')
        print('\nmedium: 10x10')
        print('\nlarge: 15x15')
        print('\ncustom: dimensions input by you\n')
        while True:
            size = input('please enter map size '
                         '(SMALL, MEDIUM, LARGE, CUSTOM):\n')
            if size.lower() == 'quit':
                quit()
            elif size.lower() == 'small':
                size = (5, 5)
                break
            elif size.lower() == 'medium':
                size = (10, 10)
                break
            elif size.lower() == 'large':
                size = (15, 15)
                break
            elif size == 'custom':
                while True:
                    width = input('map width? (5 - 50):\n')
                    try:
                        width = int(width)
                        if width == 'quit':
                            quit()
                        elif 5 <= width <= 50:
                            break
                    except ValueError:
                        print('Please only use numbers')

                while True:
                    height = input('map height? (5 - 50):\n')
                    try:
                        height = int(height)
                        if width == 'quit':
                            quit()
                        elif 5 <= height <= 50:
                            break
                    except ValueError:
                        print('Please only use numbers')
                size = (width, height)
                break
        return size

    @classmethod
    def get_direction(cls, allowed_moves: Annotated[Tuple[bool], 4]) -> str:
        """
        given a tuple of 4 boolean values representing UP/DOWN/LEFT/right
        directions, adds possible movements to a list and then joins them
        in a string. (True, True, False, True) -> [up, down, right] >
        'Up or DOWN or RIGHT' raises valueError if the given tuple doesn't
        contain any True values (meaning here's no allowed direction).

        Parameters
        ----------
        allowed_moves: tuple[bool, ...] :
            a tuple of 4 boolean values representing UP/DOWN/LEFT/right
         directions.
        Returns
        -------
        str:
            a string of possible movements.
        """
        if True not in allowed_moves:
            raise ValueError(f'{allowed_moves} must contain'
                             f' at least one True value')
        allowed_directions = list()
        for index in range(len(allowed_moves)):
            if allowed_moves[index]:
                allowed_directions.append(cls.direction_list[index].upper())
        while True:
            direction = input('enter ' + ' or '.join(allowed_directions) +
                              ' to move:\n')
            if direction.lower() == 'quit':
                quit()
            if direction.lower() in cls.direction_list:
                break
        return direction.lower()

    @staticmethod
    def intro_message() -> str:
        """
        greeting message at game's start.
        Returns
        -------
        str:
            greeting message
        """
        version = '0.5.1'
        intro = f'spooky DnD version={version}' \
                f' please select game mode, difficulty and map size.\n'
        return intro

    @staticmethod
    def starting_rp_message() -> str:
        """
        starting role-playing message.
        Returns
        -------
        str:
            background story.
        """
        starting_rp = 'you were lost in  the caverns under your village' \
                      ', It\'s completely dark in here and you cannot ' \
                      'see a thing, you can only move up, down, left and' \
                      ' right to find the exit, beware of the dragon your' \
                      ' grandma used to tell stories about that lives below' \
                      ' your village...'
        return starting_rp


calculate_distance = Helpers.calc_distance
point_comparison = Helpers.point_comparison


if __name__ == '__main__':
    # x = Helpers.get_dimensions()
    # print(x)
    Helpers.get_direction((False, False, False, True))

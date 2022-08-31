from random import randint
import logging
from typing import (Callable,
                    List,
                    Annotated)

from game_tools.helpers import (coords_tuple,
                                coords_list)


"""
contains game's Board and supporting classes needed to
operate on it.
"""


class Board:
    """
    controls the game board and the entities placed within it.
    """
    __directions = ['up', 'down', 'left', 'right', 'no move']
    __char_list = ['player', 'dragon']

    def __init__(self, size: coords_tuple) -> None:
        self.map_size = size
        player_dragon_door = self.init_pos(size)
        self.player_pos = player_dragon_door[0]
        self.dragon_pos = player_dragon_door[1]
        self.door_pos = player_dragon_door[2]

    @property
    def map_size(self):
        """
        getter for size attribute, which is the dimensions
        of the game board, e.g. a 4 x 6 rectangle.
        """
        return self._map_size

    @map_size.setter
    def map_size(self, size: coords_tuple) -> None:
        """
        setter for size attribute, raises a valueError
        exception if the input is not a tuple
        containing two integers.
        """
        if isinstance(size, tuple) and len(size) == 2 \
                and [type(size[0]), type(size[1])] == [int, int]:
            self._map_size = size
        else:
            raise ValueError('map size should be a tuple containing 2 int\'s')

    @staticmethod
    def init_pos(dimension: coords_tuple) -> List[Annotated[coords_list, 3]]:
        """
        creates a random a list containing 3 [X,Y] lists which are the
        starting positions for player,dragon, and door in that order.
        e.g. in [[x1, y1], [x2, y2], [x3, y3]] player's starting position
        is for player and so on. player always start at [1, 1] dragon and
        door can never start at the same location and there's some distance
        with player.

        Parameters
        ----------
        dimension: tuple[int, int] :
                a tuple containing dimensions of the game board.

        Returns
        -------
        list[list, ...]:
            list containing 3 [X,Y] lists which are the
            starting positions for player,dragon, and door in that order.

        """
        player_pos = [1, 1]
        dragon_pos = [randint(3, dimension[0]),
                      randint(3, dimension[1])]
        while True:
            door_pos = [randint(3, dimension[0]),
                        randint(3, dimension[1])]
            if door_pos != dragon_pos:
                break
        pla_dra_door = [player_pos, dragon_pos, door_pos]
        return pla_dra_door

    def allowed_moves(self, position: list[int, int])\
            -> tuple[bool, bool, bool, bool]:
        """
        checks for directions where movement is not blocked by walls.

        Parameters
        ----------
        position: list[int, int] :
            X, Y coordinates of the entity (usually the player)

        Returns
        -------
        tuple[bool, bool, bool, bool]:
            the booleans in the tuple correspond to possibility of movement
            in UP/DOWN/LEFT/RIGHT direction.
        """
        if isinstance(position, list) and len(position) == 2:
            if position[1] == 1:
                can_go_up = False
            else:
                can_go_up = True
            if position[1] == self.map_size[1]:
                can_go_down = False
            else:
                can_go_down = True
            if position[0] == 1:
                can_go_left = False
            else:
                can_go_left = True
            if position[0] == self.map_size[0]:
                can_go_right = False
            else:
                can_go_right = True
            return can_go_up, can_go_down, can_go_left, can_go_right
        else:
            logging.info('invalid position given to allowed_moves')
            raise ValueError(f'{position} is not a (x, y) coordinates tuple')

    def move(self, coords: coords_list, direction: str) -> str or None:
        """
        moves the entity at the given location to the given direction

        Parameters
        ----------
        coords: list[int, int] :
            X, Y coordinates of the given entity
        direction: str :
            given direction, raises a valueError if it's not
            UP/DOWN/LEFT/RIGHT.
        Returns
        -------
        None or str:
            if the UP/DOWN/LEFT/RIGHT input is not within allowed moves
            (touches the game walls) returns reaching the wall message,
            else None.
        """
        carryover = None
        wall_text = 'your hand touches the cave\'s wall,' \
                    'try a different direction'
        if direction.lower() in Board.__directions and\
                coords in [self.player_pos, self.dragon_pos]:
            if direction.lower() == 'up':
                if self.allowed_moves(coords)[0]:
                    coords[1] -= 1
                else:
                    carryover = wall_text
            elif direction.lower() == 'down':
                if self.allowed_moves(coords)[1]:
                    coords[1] += 1
                else:
                    carryover = wall_text
            elif direction.lower() == 'left':
                if self.allowed_moves(coords)[2]:
                    coords[0] -= 1
                else:
                    carryover = wall_text
            elif direction.lower() == 'right':
                if self.allowed_moves(coords)[3]:
                    coords[0] += 1
                else:
                    carryover = wall_text
            else:
                pass
        elif direction.lower() not in Board.__directions:
            raise ValueError('directions can only be up/down/left/right')

        else:
            logging.info('invalid movement coords given')
            raise ValueError(f'invalid coords, {coords} corresponds'
                             f' to neither dragon nor player')
        return carryover

    def check_victory_loss(self, func: Callable) -> None:
        """
        checks for victory or loss condition.

        Parameters
        ----------
        func :
            the function to be run if 'rematch' is chosen.
        """
        if self.player_pos == self.door_pos:
            print('YOU WON: Finding the exit to the '
                  'cave,you get to live another day')
            while True:
                rematch = input('play again? yes/no:\n').lower()
                if rematch == 'yes':
                    func()
                elif rematch in ['no', 'quit']:
                    quit()
        elif self.player_pos == self.dragon_pos:
            print('GAME OVER: The dragon gnaws on your'
                  ' flesh and bones, you\'re dead')
            while True:
                rematch = input('play again? yes/no:\n').lower()
                if rematch == 'yes':
                    func()
                elif rematch in ['no', 'quit']:
                    quit()
                else:
                    continue

    # def cells_init(self) -> dict:
    #     for _x in range(self.map_size[0]):
    #         for _y in range(self.map_size[1]):
    #             self.cell_data[(_x + 1, _y + 1)] = None
    #
    # def manipulate_cell(self, cell: tuple[int, int], value: str):
    #     if self.cell_data == dict():
    #         self.cells_init()
    #     self.cell_data[cell] = value


class BoardPrints:
    """
    contains class/static methods needed for Board class.
    seperated to declutter the Board class.
    """
    @staticmethod
    def generate_board(obj: Board) -> list[List[str], ...]:
        """
        creates the game board in form of a list of rows containing
        (Y axis) containing cells (X axis).
        Parameters
        ----------
        obj :
            an instance of Board class.
        Returns
        -------
        list[list, ...]:
            list of lists (rows) which make up the Y-axis each containing
            a list of cells (X axis).
        """
        x_length = (obj.map_size[0] * 4) + 1
        y_length = (obj.map_size[1] * 2) + 1
        grid = [['-' for _ in range(x_length)] for _row in range(y_length)]
        for row in range(y_length):
            if row % 2 == 0:
                for cell in range(x_length):
                    if cell % 4 == 0:
                        grid[row][cell] = ' '
            else:
                for cell in range(x_length):
                    if cell % 4 == 0:
                        grid[row][cell] = '|'
                    else:
                        grid[row][cell] = ' '
        return grid

    @staticmethod
    def print_board(grid: list[List[str], ...]) -> None:
        """
        prints the game board.

        Parameters
        ----------
        list of lists (rows) which make up the Y-axis each
            containing a list of cells (X axis).
            of cells (X axis).
        """
        for row in grid:
            print(''.join(row))

    @staticmethod
    def place_player(grid: list[List[str], ...],
                     player_pos: coords_list) -> None:
        """
        inserts player as an 'X' onto the game board list.

        Parameters
        ----------
        grid: list[list, ...] :
            list of lists (rows) which make up the Y-axis each
            containing a list of cells (X axis).
        player_pos: list[int, int] :
            X, Y coordinates of the player.
        """
        player_x = (player_pos[0]) * 4 - 2
        player_y = (player_pos[1]) * 2 - 1
        grid[player_y][player_x] = 'x'

    @classmethod
    def remove_player(cls, grid: list[List[str], ...], player_pos: coords_list,
                      dragon_pos: coords_list) -> None:
        """
        replaces player and dragon in game board list with blank.
        Parameters
        ----------
        grid: list[list, ...] :
            list of lists (rows) which make up the Y-axis each
            containing a list of cells (X axis).
        player_pos: list[int, int] :
            X, Y coordinates of the player.
        dragon_pos: list[int, int] :
            X, Y coordinates of the dragon.
        """
        player_x = (player_pos[0]) * 4 - 2
        player_y = (player_pos[1]) * 2 - 1
        grid[player_y][player_x] = ' '
        dragon_x = (dragon_pos[0] - 1) * 4 + 2
        dragon_y = (dragon_pos[1] - 1) * 2 + 1
        grid[dragon_y][dragon_x] = ' '

    @classmethod
    def place_dragon(cls, grid: list[List[str], ...],
                     dragon_pos: coords_list) -> None:
        """
        inserts dragon as an 'D' onto the game board list.

        Parameters
        ----------
        grid: list[list, ...] :
            list of lists (rows) which make up the Y-axis
            each containing a list of cells (X axis).
        dragon_pos: list[int, int] :
            X, Y coordinates of the dragon.
        """
        dragon_x = (dragon_pos[0] - 1) * 4 + 2
        dragon_y = (dragon_pos[1] - 1) * 2 + 1
        grid[dragon_y][dragon_x] = 'D'

    @classmethod
    def place_door(cls, grid: list[List[str], ...],
                   door_pos: coords_list) -> None:
        """
        inserts door as an "O" onto the game board list.

        Parameters
        ----------
        grid: list[list, ...] :
            list of lists (rows) which make up the Y-axis
            each containing a list of cells (X axis).
        door_pos: list[int, int] :
            X, Y coordinates of the door.
        """
        door_x = (door_pos[0] - 1) * 4 + 2
        door_y = (door_pos[1] - 1) * 2 + 1
        grid[door_y][door_x] = 'O'


# tests
if __name__ == '__main__':
    first = Board((5, 5))
    print(f'player at {first.player_pos}, dragon at '
          f'{first.dragon_pos} and door at {first.door_pos}')
    first.move(first.player_pos, 'down')
    print(f'player at {first.player_pos}, dragon at '
          f'{first.dragon_pos} and door at {first.door_pos}')
    first.move(first.dragon_pos, 'right')
    print(f'player at {first.player_pos}, dragon at '
          f'{first.dragon_pos} and door at {first.door_pos}')
    board = BoardPrints.generate_board(first)
    BoardPrints.place_player(board, first.player_pos)
    BoardPrints.place_dragon(board, first.dragon_pos)
    BoardPrints.place_door(board, first.door_pos)
    BoardPrints.print_board(board)

from game_tools import entities, gridboard
from game_tools.helpers import Helpers as Helpers


def main() -> None:
    """
    main function to run the program
    """
    Helpers.clear_board()
    print(Helpers.intro_message())
    mode = Helpers.start_or_test()
    difficulty = Helpers.get_difficulty()
    size = Helpers.get_dimensions()
    player = entities.Player(difficulty)
    dragon = entities.Dragon(difficulty)
    board = gridboard.Board(size)
    carry_over = None
    generated_board = gridboard.BoardPrints.generate_board(board)
    Helpers.clear_board()
    print(Helpers.starting_rp_message())
    while True:
        player_pos = board.player_pos
        dragon_pos = board.dragon_pos
        door_pos = board.door_pos
        dragon_player_distance = Helpers.calc_distance(dragon_pos, player_pos)
        player_door_distance = Helpers.calc_distance(player_pos, door_pos)
        gridboard.BoardPrints.place_player(generated_board, player_pos)
        if mode == 'test' or player.player_sight(dragon_player_distance):
            gridboard.BoardPrints.place_dragon(generated_board, dragon_pos)
        if mode == 'test' or player.player_sight(player_door_distance):
            gridboard.BoardPrints.place_door(generated_board, door_pos)
        gridboard.BoardPrints.print_board(generated_board)
        gridboard.BoardPrints.remove_player(generated_board, player_pos, dragon_pos) # noqa
        if carry_over is not None:
            print(carry_over)
        print(f"player= x dragon = D door = O\nyou\'re at {player_pos}")
        if mode == 'test':
            print(f"dragon at {dragon_pos}, door at {door_pos}\n"
                  f"distance to dragon: {dragon_player_distance:0.2f}"
                  f" and to door {player_door_distance:0.2f}\n")
        allowed_moves = board.allowed_moves(player_pos)
        direction = Helpers.get_direction(allowed_moves)
        carry_over = board.move(player_pos, direction)
        board.check_victory_loss(main)
        if direction in Helpers.direction_list:
            if dragon.dragon_sight(dragon_player_distance):
                dragon_direction = Helpers.point_comparison(player_pos, dragon_pos)  # noqa
                board.move(dragon_pos, dragon_direction)
            if dragon.dragon_hearing(dragon_player_distance):
                dragon_direction = Helpers.point_comparison(player_pos, dragon_pos)  # noqa
                board.move(dragon_pos, dragon_direction)
            if mode == 'test' or player.player_sight(dragon_player_distance):
                gridboard.BoardPrints.place_dragon(generated_board, dragon_pos)
            Helpers.clear_board()
            gridboard.BoardPrints.print_board(generated_board)
            board.check_victory_loss(main)
        Helpers.clear_board()


main()

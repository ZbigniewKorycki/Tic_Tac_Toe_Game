wall_up_down = " --- --- --- "
wall_back = "|"

locations = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Welcome to the Tic Tac Toe Game!")

PLAYER_1_NAME = input("What is the name of first player?: ")
PLAYER_1_MARK = "*"

PLAYER_2_NAME = input("What is the name of second player?: ")
PLAYER_2_MARK = "○"

player_1_positions = []
player_2_positions = []

winning_locations = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["1", "4", "7"],
    ["2", "5", "8"],
    ["3", "6", "9"],
    ["1", "5", "9"],
    ["3", "5", "7"]
]


def create_board():
    print(wall_up_down)
    for index, place in enumerate(locations, 1):
        print(wall_back, end=" ")
        print(place, end=" ")
        if index % 3 == 0:
            print(wall_back, end="\n")
            print(wall_up_down)


def winning(player_positions):
    for combination in winning_locations:
        result_player = all(element in player_positions for element in combination)
        if result_player:
            return True
    else:
        return False


def end_of_free_spaces():
    num_marks_player1 = locations.count(PLAYER_1_MARK)
    num_marks_player2 = locations.count(PLAYER_2_MARK)
    if num_marks_player1 + num_marks_player2 == len(locations):
        return True
    else:
        return False


def player_turn(player_name, player_mark, player_positions):
    incorrect_move = True
    while incorrect_move:
        create_board()
        player_move = input(f"{player_name}: Under which position do you want to put your mark ( {player_mark} ): ")
        if player_move in locations:
            position = locations.index(player_move)
            player_positions.append(locations[position])
            locations[position] = player_mark
            incorrect_move = False
        else:
            print(f"This position is not available. Choose different one.")
    return player_positions, player_name


game_on = True
while game_on:
    move_player1 = player_turn(PLAYER_1_NAME, PLAYER_1_MARK, player_1_positions)
    if winning(move_player1[0]):
        print(f"{move_player1[1]} win")
        break
    elif end_of_free_spaces():
        print("End of free space. Nobody win.")
        break
    move_player2 = player_turn(PLAYER_2_NAME, PLAYER_2_MARK, player_2_positions)
    if winning(move_player2[0]):
        print(f"{move_player2[1]} win")
        break
    elif end_of_free_spaces():
        print("End of free space. Nobody win.")
        break
    print("--------------------------------------END OF ROUND--------------------------------------")

print("Final board:")
create_board()



wall_up_down = " --- --- --- "
wall_back = "|"

locations = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

PLAYER_1_NAME = "Adam"
PLAYER_1_MARK = "*"

PLAYER_2_NAME = "Marek"
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


game_on = True
while game_on:
    incorrect_move_player_1 = True
    while incorrect_move_player_1:
        create_board()
        move_player_1 = input(f"{PLAYER_1_NAME}: Under which position you want to put your mark ( {PLAYER_1_MARK} ): ")
        if move_player_1 in locations:
            position = locations.index(move_player_1)
            player_1_positions.append(locations[position])
            locations[position] = PLAYER_1_MARK
            incorrect_move_player_1 = False

        else:
            print(f"This position is not available. Choose different one.")
    if winning(player_1_positions):
        print(f"{PLAYER_1_NAME} win")
        break
    elif end_of_free_spaces():
        print("End of free space. Noboby win.")
        break
    incorrect_move_player_2 = True
    while incorrect_move_player_2:
        create_board()
        move_player_2 = input(f"{PLAYER_2_NAME}: Under which position you want to put your mark ( {PLAYER_2_MARK} ): ")
        if move_player_2 in locations:
            position = locations.index(move_player_2)
            player_2_positions.append(locations[position])
            locations[position] = PLAYER_2_MARK
            incorrect_move_player_2 = False
        else:
            print("This position is not available. Choose different one.")
    if winning(player_2_positions):
        print(f"{PLAYER_2_NAME}win")
        break
    elif end_of_free_spaces():
        print("End of free space. Noboby win.")
        break
    print("--------------------------------------END OF ROUND--------------------------------------")

print("Final board:")
create_board()


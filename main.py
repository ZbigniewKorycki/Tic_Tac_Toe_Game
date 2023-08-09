wall_up_down = " --- --- --- "
wall_back = "|"

locations = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

PLAYER_1_MARK = "*"
PLAYER_2_MARK = "○"




def create_board():
    print(wall_up_down)
    for index, place in enumerate(locations, 1):
        print(wall_back, end=" ")
        print(place, end=" ")
        if index % 3 == 0:
            print(wall_back, end="\n")
            print(wall_up_down)


game_on = True
while game_on:
    create_board()
    incorrect_move_player_1 = True
    while incorrect_move_player_1:
        move_player_1 = input(f"Player 1: Under which position you want to put your mark ( {PLAYER_1_MARK} ): ")
        if move_player_1 in locations:
            position = locations.index(move_player_1)
            locations[position] = PLAYER_1_MARK
            create_board()
            incorrect_move_player_1 = False
        else:
            print(f"This position is not available. Choose different one.")
            create_board()
    incorrect_move_player_2 = True
    while incorrect_move_player_2:
        move_player_2 = input(f"Player 2: Under which position you want to put your mark ( {PLAYER_2_MARK} ): ")
        if move_player_2 in locations:
            position = locations.index(move_player_2)
            locations[position] = PLAYER_2_MARK
            create_board()
            incorrect_move_player_2 = False
        else:
            print("This position is not available. Choose different one.")
            create_board()



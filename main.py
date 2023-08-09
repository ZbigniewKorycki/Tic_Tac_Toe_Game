# #  --- --- ---
# # | X | X | X |
#    --- --- ---
# # | X | X | X |
#    --- --- ---
# # | X | X | X |
# #  --- --- ---
# #

wall_up_down = " --- --- --- "
wall_back = "|"

locations = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def create_board():
    print(wall_up_down)
    for index, place in enumerate(locations, 1):
        print(wall_back, end=" ")
        print(place, end=" ")
        if index % 3 == 0:
            print(wall_back, end="\n")
            print(wall_up_down)


create_board()






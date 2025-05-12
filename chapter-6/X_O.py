board = {
    "top_left":"empty",
    "top_right":"empty",
    "top_midle":"empty",
    "midle_midle":"empty",
    "midle_right":"empty",
    "midle_left":"empty",
    "bottom_left":"empty",
    "bottom_right":"empty",
    "top_midle":"empty"
}
user1_input = input()
if user1_input == "x 1":
    board[top_left] = "x"
elif user1_input == "x 2":
    board[top_midle]
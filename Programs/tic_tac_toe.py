board = {
    "top_left": "empty",
    "top_center": "empty",
    "top_right": "empty",
    "middle_left": "empty",
    "middle_center": "empty",
    "middle_right": "empty",
    "bottom_left": "empty",
    "bottom_center": "empty",
    "bottom_right": "empty"
}

def display_board(board):
    print(f"{board['top_left']} || {board['top_center']} || {board['top_right']}")
    print(f"{board['middle_left']} || {board['middle_center']} || {board['middle_right']}")
    print(f"{board['bottom_left']} || {board['bottom_center']} || {board['bottom_right']}")

while True:
    display_board(board)
    user_input = input("Enter a number (1-9): ")

    if user_input == "1" and board["top_left"] == "empty":
        board["top_left"] = "x"
    elif user_input == "2" and board["top_center"] == "empty":
        board["top_center"] = "x"
    elif user_input == "3" and board["top_right"] == "empty":
        board["top_right"] = "x"
    elif user_input == "4" and board["middle_left"] == "empty":
        board["middle_left"] = "x"
    elif user_input == "5" and board["middle_center"] == "empty":
        board["middle_center"] = "x"
    elif user_input == "6" and board["middle_right"] == "empty":
        board["middle_right"] = "x"
    elif user_input == "7" and board["bottom_left"] == "empty":
        board["bottom_left"] = "x"
    elif user_input == "8" and board["bottom_center"] == "empty":
        board["bottom_center"] = "x"
    elif user_input == "9" and board["bottom_right"] == "empty":
        board["bottom_right"] = "x"

    if "empty" not in board.values():
        display_board(board)
        break

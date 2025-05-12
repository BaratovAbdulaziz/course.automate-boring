board = {
    "top_left": "empty",
    "top_right": "empty",
    "top_midle": "empty",
    "midle_midle": "empty",
    "midle_right": "empty",
    "midle_left": "empty",
    "bottom_left": "empty",
    "bottom_right": "empty",
    "bottom_midle": "empty"
}

def result(board):
    print(f"{board['top_left']} || {board['top_midle']} || {board['top_right']}")
    print(f"{board['midle_left']} || {board['midle_midle']} || {board['midle_right']}")
    print(f"{board['bottom_left']} || {board['bottom_midle']} || {board['bottom_right']}")

while True:
    result(board)
    user1_input = input("Enter a number (1-9): ")

    if user1_input == "1" and board["top_left"] == "empty":
        board["top_left"] = "x"
    elif user1_input == "2" and board["top_midle"] == "empty":
        board["top_midle"] = "x"
    elif user1_input == "3" and board["top_right"] == "empty":
        board["top_right"] = "x"
    elif user1_input == "4" and board["midle_left"] == "empty":
        board["midle_left"] = "x"
    elif user1_input == "5" and board["midle_midle"] == "empty":
        board["midle_midle"] = "x"
    elif user1_input == "6" and board["midle_right"] == "empty":
        board["midle_right"] = "x"
    elif user1_input == "7" and board["bottom_left"] == "empty":
        board["bottom_left"] = "x"
    elif user1_input == "8" and board["bottom_midle"] == "empty":
        board["bottom_midle"] = "x"
    elif user1_input == "9" and board["bottom_right"] == "empty":
        board["bottom_right"] = "x"

    if "empty" not in board.values():
        result(board)
        break

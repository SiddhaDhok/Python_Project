import random

# Game board setup
BOARD_SIZE = 5
board = []
for _ in range(BOARD_SIZE):
    board.append(["O"] * BOARD_SIZE)

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Place a single ship randomly
def place_ship(board):
    ship_row = random.randint(0, BOARD_SIZE - 1)
    ship_col = random.randint(0, BOARD_SIZE - 1)
    return ship_row, ship_col

# Game loop
def play_battleship():
    print("Let's play Battleship!")
    print_board(board)

    ship_row, ship_col = place_ship(board)
    # For debugging, uncomment the next line to see ship location
    # print(f"Ship is at ({ship_row}, {ship_col})")

    turns = 4
    for turn in range(turns):
        print(f"\nTurn {turn + 1} of {turns}")
        try:
            guess_row = int(input("Guess Row (0-4): "))
            guess_col = int(input("Guess Col (0-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if not (0 <= guess_row < BOARD_SIZE and 0 <= guess_col < BOARD_SIZE):
            print("Oops, that's not even in the ocean!")
        elif board[guess_row][guess_col] == "X":
            print("You already guessed that spot.")
        elif guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            board[guess_row][guess_col] = "H"  # Mark as hit
            print_board(board)
            break
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"  # Mark as missed
            print_board(board)

        if turn == turns - 1:
            print("\nGame Over! You ran out of turns.")
            print(f"The battleship was at ({ship_row}, {ship_col}).")

# Start the game
if __name__ == "__main__":
    play_battleship()
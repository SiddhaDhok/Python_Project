# Placing user's ships
def get_user_ship_positions(board, count=8):
    placed = 0
    print(f"Enter positions for {count} ships (row col):")
    while placed < count:
        try:
            inp = input(f"Ship {placed+1}: ").strip().split()
            if len(inp) != 2:
                print("Enter exactly two integers.")
                continue

            r, c = map(int, inp)
            if board.place_ship((r, c)):
                placed += 1
                board.display(show_ships=True)
            else:
                print("Invalid or duplicate position.")

        except ValueError:
            print("Invalid input. Enter integers only.")

# Attack 
def attack(board, pos):
    r, c = pos
    if not (0 <= r < board.size and 0 <= c < board.size):
        return "Invalid"

    if pos in board.hit_positions or pos in board.miss_positions:
        return "Already Attacked"

    if pos in board.ship_positions:
        board.hit_positions.add(pos)
        board.ship_positions.remove(pos)
        return "Hit"

    board.miss_positions.add(pos)
    return "Miss"
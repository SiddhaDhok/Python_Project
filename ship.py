# ============================================================
# USER SHIP PLACEMENT
# ============================================================
def get_user_ship_positions(board, count=8):
    placed = 0
    print(f"Enter positions for {count} ships (row col):")
    # Keep asking until all ships are placed
    while placed < count:
        try:
            # Get input and split it into row and column
            inp = input(f"Ship {placed+1}: ").strip().split()
            if len(inp) != 2:
                print("Enter exactly two integers.")
                continue

            # Convert to integers
            r, c = map(int, inp)
            # Try to place the ship on the board
            if board.place_ship((r, c)):
                placed += 1
                # Show the updated board so they can see where ships are
                board.display(show_ships=True)
            else:
                print("Invalid or duplicate position.")

        except ValueError:
            # Handles if they didn't enter numbers
            print("Invalid input. Enter integers only.")


# ============================================================
# ATTACK FUNCTION
# ============================================================
def attack(board, pos):
    r, c = pos
    # Check if the position is even on the board
    if not (0 <= r < board.size and 0 <= c < board.size):
        return "Invalid"

    # Can't attack the same spot twice
    if pos in board.hit_positions or pos in board.miss_positions:
        return "Already Attacked"

    # Check if there's a ship at this position
    if pos in board.ship_positions:
        # Record the hit and remove the ship segment
        board.hit_positions.add(pos)
        board.ship_positions.remove(pos)
        return "Hit"

    # No ship there - it's a miss
    board.miss_positions.add(pos)
    return "Miss"
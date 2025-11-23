import random

# ============================================================
# BOARD CLASS
# ============================================================
class Board:
    def __init__(self, size=10):
        self.size = size
        self.ship_positions = set()
        self.hit_positions = set()
        self.miss_positions = set()

    def display(self, show_ships=False):
        print("  " + " ".join(str(i) for i in range(self.size)))
        for r in range(self.size):
            row_display = []
            for c in range(self.size):
                pos = (r, c)

                if pos in self.hit_positions:
                    row_display.append("O")  # hit
                elif pos in self.miss_positions:
                    row_display.append("X")  # miss
                elif pos in self.ship_positions and show_ships:
                    row_display.append("S")
                else:
                    row_display.append(" ")
            print(str(r) + " " + " ".join(row_display))

    def place_ship(self, pos):
        r, c = pos
        if 0 <= r < self.size and 0 <= c < self.size:
            if pos not in self.ship_positions:
                self.ship_positions.add(pos)
                return True
        return False

    def place_ships_randomly(self, count=8):
        while len(self.ship_positions) < count:
            pos = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            self.place_ship(pos)


# ============================================================
# USER SHIP PLACEMENT
# ============================================================
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


# ============================================================
# ATTACK FUNCTION
# ============================================================
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


# ============================================================
# MAIN GAME
# ============================================================
def main():
    user_board = Board()
    comp_board = Board()

    comp_board.place_ships_randomly()

    print("\n=== PLACE YOUR SHIPS ===")
    get_user_ship_positions(user_board)

    print("\nYour Board:")
    user_board.display(show_ships=True)

    print("\nComputer Board:")
    comp_board.display(show_ships=False)

    print("\n=== GAME START ===")

    user_turns = 20
    comp_turns = 20

    while True:

        # ============================================================
        # USER TURN
        # ============================================================
        print(f"\nYour Turn (Remaining turns: {user_turns})")

        while True:
            try:
                r, c = map(int, input("Enter attack (row col): ").split())
            except:
                print("Invalid input. Try again.")
                continue

            result = attack(comp_board, (r, c))

            if result == "Invalid":
                print("Invalid position. Try again.")
                continue

            if result == "Already Attacked":
                print("You already tried that spot. Try again.")
                continue

            print(result)
            print("\nComputer Board:")
            comp_board.display(show_ships=False)

            if result == "Hit":
                print("You earned a bonus turn!")
                continue  # free extra turn

            if result == "Miss":
                user_turns -= 1
                break  # normal turn consumed

        # WIN CHECK
        if len(comp_board.ship_positions) == 0:
            print("\n🎉 YOU WIN! You destroyed the enemy fleet!")
            break
        if user_turns == 0:
            print("\n❌ You ran out of turns!")
            break

        # ============================================================
        # AI TURN
        # ============================================================
        print(f"\nAI's Turn (Remaining turns: {comp_turns})")

        while True:
            ai_r = random.randint(0, 9)
            ai_c = random.randint(0, 9)

            result = attack(user_board, (ai_r, ai_c))

            if result == "Already Attacked":
                continue  # retry same turn

            print(f"AI fired at [{ai_r}, {ai_c}] → {result}")

            if result == "Hit":
                print("AI gets a bonus turn!")
                continue

            if result == "Miss":
                comp_turns -= 1
                break

        # LOSE CHECK
        if len(user_board.ship_positions) == 0:
            print("\n💀 YOU LOSE! Your fleet has been destroyed!")
            break
        if comp_turns == 0:
            print("\n🎉 YOU WIN! The AI ran out of turns!")
            break


# START THE GAME
main()

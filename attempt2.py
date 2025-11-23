import random

# ---------------------------------------
# BOARD CLASS
# ---------------------------------------
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
                    row_display.append("S")  # show ships only on your board
                else:
                    row_display.append(" ")  # unknown
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


# ---------------------------------------
# USER SHIP PLACEMENT
# ---------------------------------------
def get_user_ship_positions(board, count=8):
    placed = 0
    print(f"Enter the positions for {count} ships (row col):")
    while placed < count:
        try:
            inp = input(f"Ship {placed+1}: ").strip().split()
            if len(inp) != 2:
                print("Enter two integers separated by space.")
                continue
            r, c = map(int, inp)

            if board.place_ship((r, c)):
                placed += 1
                board.display(show_ships=True)
            else:
                print("Invalid or duplicate position.")
        except:
            print("Invalid input.")


# ---------------------------------------
# ATTACK FUNCTION
# ---------------------------------------
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
    else:
        board.miss_positions.add(pos)
        return "Miss"


# ---------------------------------------
# MAIN GAME LOOP
# ---------------------------------------
def main():
    user_board = Board()
    computer_board = Board()

    # Random AI ship placement
    computer_board.place_ships_randomly()

    print("\n=== Place Your Ships ===")
    get_user_ship_positions(user_board)

    print("\nYour Board:")
    user_board.display(show_ships=True)

    print("\nComputer Board:")
    computer_board.display(show_ships=False)

    # GAME BEGINS
    print("\n=== BATTLE START ===")

    while True:
        # ---------------------------------------
        # USER TURN
        # ---------------------------------------
        print("\nYour Turn:")

        while True:
            try:
                r, c = map(int, input("Enter attack (row col): ").split())
            except:
                print("Invalid input.")
                continue

            result = attack(computer_board, (r, c))
            print(result)

            print("\nComputer Board:")
            computer_board.display(show_ships=False)

            if result == "Already Attacked":
                print("Pick a new position.")
                continue  # retry same turn

            if result == "Hit":
                # extra turn
                continue

            break  # miss ends the turn

        # WIN CHECK
        if len(computer_board.ship_positions) == 0:
            print("\n🎉 YOU WIN! You destroyed all enemy ships!")
            break

        # ---------------------------------------
        # AI TURN
        # ---------------------------------------
        print("\nAI's Turn:")
        while True:
            ai_r = random.randint(0, 9)
            ai_c = random.randint(0, 9)
            result = attack(user_board, (ai_r, ai_c))

            print(f"AI fired at [{ai_r}, {ai_c}]")
            print(result)

            if result == "Already Attacked":
                continue  # retry

            if result == "Hit":
                continue  # extra move

            break  # miss ends turn

        # LOSE CHECK
        if len(user_board.ship_positions) == 0:
            print("\n💀 YOU LOSE! Your fleet has been destroyed!")
            break


# ---------------------------------------
# START GAME
# ---------------------------------------
main()

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
import random

# ============================================================
# BOARD CLASS
# ============================================================
class Board:
    def __init__(self, size=10):
        self.size = size
        # Keep track of where ships are placed
        self.ship_positions = set()
        # Track successful hits
        self.hit_positions = set()
        # Track missed shots
        self.miss_positions = set()

    def display(self, show_ships=False):
        # Print column numbers at the top
        print("  " + " ".join(str(i) for i in range(self.size)))
        for r in range(self.size):
            row_display = []
            for c in range(self.size):
                pos = (r, c)

                # Show hits as 'O'
                if pos in self.hit_positions:
                    row_display.append("O")  # hit
                # Show misses as 'X'
                elif pos in self.miss_positions:
                    row_display.append("X")  # miss
                # Only show ships if we're supposed to (like on player's own board)
                elif pos in self.ship_positions and show_ships:
                    row_display.append("S")
                else:
                    # Empty water
                    row_display.append(" ")
            # Print row number and the row itself
            print(str(r) + " " + " ".join(row_display))

    def place_ship(self, pos):
        # Make sure position is valid and not already taken
        r, c = pos
        if 0 <= r < self.size and 0 <= c < self.size:
            if pos not in self.ship_positions:
                self.ship_positions.add(pos)
                return True
        return False

    def place_ships_randomly(self, count=8):
        # Keep placing until we have enough ships
        while len(self.ship_positions) < count:
            # Pick a random spot
            pos = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            self.place_ship(pos)
    
    # ============================================================
    # SERIALIZE BOARD TO DICTIONARY (for saving)
    # ============================================================
    def to_dict(self):
        """Convert board to a dictionary for JSON serialization."""
        # Sets can't be saved to JSON, so convert them to lists
        return {
            "size": self.size,
            "ship_positions": list(self.ship_positions),
            "hit_positions": list(self.hit_positions),
            "miss_positions": list(self.miss_positions)
        }
    
    # ============================================================
    # LOAD BOARD FROM DICTIONARY (for loading)
    # ============================================================
    @staticmethod
    def from_dict(data):
        """Create a board from a dictionary."""
        # Create a new board with the saved size
        board = Board(size=data["size"])
        # Convert lists back to sets (and make sure tuples are tuples)
        board.ship_positions = set(tuple(pos) for pos in data["ship_positions"])
        board.hit_positions = set(tuple(pos) for pos in data["hit_positions"])
        board.miss_positions = set(tuple(pos) for pos in data["miss_positions"])
        return board
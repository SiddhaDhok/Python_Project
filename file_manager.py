import os
import json

# File names for storing game data
RESULTS_FILE = "battleship_save.txt"
SAVE_FILE = "saved_game.json"

# ============================================================
# SAVE GAME RESULT
# ============================================================
def save_result(result_text):
    # Append result to the file (creates file if it doesn't exist)
    with open(RESULTS_FILE, "a") as f:
        f.write(result_text + "\n")


# ============================================================
# LOAD ALL RESULTS
# ============================================================
def load_results():
    # If no results file exists yet, return a default message
    if not os.path.exists(RESULTS_FILE):
        return ["No saved results yet."]
    
    # Read all the lines from the file
    with open(RESULTS_FILE, "r") as f:
        lines = f.readlines()
        # Strip whitespace from each line
        return [line.strip() for line in lines]


# ============================================================
# CLEAR ALL RESULTS
# ============================================================
def clear_results():
    # If the file exists, empty it out
    if os.path.exists(RESULTS_FILE):
        open(RESULTS_FILE, "w").close()
        return True
    return False


# ============================================================
# SAVE GAME STATE
# ============================================================
def save_game_state(game_state):
    """
    Save the current game state to a file.
    game_state should be a dictionary containing:
    - user_board_data
    - comp_board_data
    - user_turns
    - comp_turns
    - round_num
    """
    try:
        # Write the game state as JSON with nice formatting
        with open(SAVE_FILE, "w") as f:
            json.dump(game_state, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving game: {e}")
        return False


# ============================================================
# LOAD GAME STATE
# ============================================================
def load_game_state():
    """
    Load a saved game state from file.
    Returns the game state dictionary or None if no save exists.
    """
    # Can't load if there's no save file
    if not os.path.exists(SAVE_FILE):
        return None
    
    try:
        # Read and parse the JSON
        with open(SAVE_FILE, "r") as f:
            game_state = json.load(f)
        return game_state
    except Exception as e:
        print(f"Error loading game: {e}")
        return None


# ============================================================
# CHECK IF SAVED GAME EXISTS
# ============================================================
def has_saved_game():
    """Check if a saved game file exists."""
    # Simple check to see if the file is there
    return os.path.exists(SAVE_FILE)


# ============================================================
# DELETE SAVED GAME
# ============================================================
def delete_saved_game():
    """Delete the saved game file."""
    # Remove the save file if it exists
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)
        return True
    return False
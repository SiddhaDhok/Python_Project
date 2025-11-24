import random
import ship
import board
import file_manager
from datetime import datetime


# ============================================================
# MAIN GAME
# ============================================================
def game(loaded_state=None):
    """
    Main game function. Can optionally load from a saved state.
    """
    
    if loaded_state:
        # Resume from saved game
        print("\n=== RESUMING SAVED GAME ===")
        # Rebuild the boards from the saved data
        user_board = board.Board.from_dict(loaded_state["user_board"])
        comp_board = board.Board.from_dict(loaded_state["comp_board"])
        # Restore turn counts and round number
        user_turns = loaded_state["user_turns"]
        comp_turns = loaded_state["comp_turns"]
        round_num = loaded_state["round_num"]
        print(f"Resuming froSm Round {round_num}...")
    else:
        # Start new game
        user_board = board.Board()
        comp_board = board.Board()

        # Computer randomly places its ships
        comp_board.place_ships_randomly()

        # Let the player place their ships manually
        print("\n=== PLACE YOUR SHIPS ===")
        ship.get_user_ship_positions(user_board)

        # Both players start with 20 turns
        user_turns = 20
        comp_turns = 20
        round_num = 1

    # Show both boards at the start (or resume)
    print("\nYour Board:")
    user_board.display(show_ships=True)

    print("\nComputer Board:")
    comp_board.display(show_ships=False)

    print("\n=== GAME START ===")
    
    game_result = None  # Will store the game outcome
    
    # Main game loop - keep going until someone wins or turns run out
    while True:

        # Check if both players ran out of turns
        # STOP before printing the next round if both players have 0 turns left
        if user_turns == 0 and comp_turns == 0:
            print("\n=== TURNS ARE OVER! FINAL RESULT ===")
            # Count remaining ships to determine winner
            user_ships_left = len(user_board.ship_positions)
            comp_ships_left = len(comp_board.ship_positions)
            
            # Whoever has fewer ships left loses
            if comp_ships_left < user_ships_left:
                print("\n🎉 You win! You have more surviving ships!")
                game_result = f"Player WON - Ships: Player hit {8-comp_ships_left} ships and AI hit {8-user_ships_left} - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            elif comp_ships_left > user_ships_left:
                print("\n❌ You lose! Your opponent has more ships!")
                game_result = f"Player LOST - Ships: Player hit {8-comp_ships_left} and AI hit {8-user_ships_left} - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            else:
                print("\nIt's a draw! Both players have the same number of ships left.")
                game_result = f"DRAW - Ships: Player hit {8-comp_ships_left} and AI hit {8-user_ships_left} - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            
            # Game is over, clean up the save file
            # Delete saved game when finished
            file_manager.delete_saved_game()
            break

        print(f"\n<--- ROUND {round_num} --->")

        # ============================================================
        # USER TURN (only if they still have turns)
        # ============================================================
        if user_turns > 0:
            print(f"\nYour Turn (Remaining turns: {user_turns})")
            print("(Type 'save' to save and quit)")

            # Keep asking for input until they make a valid move
            while True:
                try:
                    user_input = input("Enter attack (row col): ").strip().lower()
                    
                    # Check if user wants to save
                    if user_input == "save":
                        save_current_game(user_board, comp_board, user_turns, comp_turns, round_num)
                        print("\n✓ Game saved! You can resume later.")
                        return None  # Exit without a result
                    
                    # Parse the row and column
                    r, c = map(int, user_input.split())
                except:
                    print("Invalid input. Try again.")
                    continue

                # Try to attack that position
                result = ship.attack(comp_board, (r, c))

                # Handle invalid positions
                if result == "Invalid":
                    print("Invalid position. Try again.")
                    continue

                # Can't attack the same spot twice
                if result == "Already Attacked":
                    print("You already tried that spot. Try again.")
                    continue

                # Show the updated board
                print("\nComputer Board:")
                comp_board.display(show_ships=False)
                print(result)

                # If you hit, check for victory or give bonus turn
                if result == "Hit":
                    if len(comp_board.ship_positions) == 0:
                        print("\n🎉 YOU WIN! You destroyed the enemy fleet!")
                        game_result = f"Player WON (Destroyed all ships) - Round {round_num} - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                        file_manager.delete_saved_game()
                        break
                    else:
                        # Hit = bonus turn!
                        print("You earned a bonus turn!")
                        continue

                # Miss means turn is over
                if result == "Miss":
                    user_turns -= 1
                    break

            # Double-check for victory (in case we broke out of the loop)
            if len(comp_board.ship_positions) == 0:
                print("\n🎉 YOU WIN! You destroyed the enemy fleet!")
                game_result = f"Player WON (Destroyed all ships) - Round {round_num} - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                file_manager.delete_saved_game()
                break

        # ============================================================
        # AI TURN (only if AI still has turns)
        # ============================================================
        if comp_turns > 0:
            print(f"\nAI's Turn (Remaining turns: {comp_turns})")

            # AI keeps going until it makes a valid move
            while True:
                # Pick a random spot to attack
                ai_r = random.randint(0, 9)
                ai_c = random.randint(0, 9)

                result = ship.attack(user_board, (ai_r, ai_c))

                # If AI picked a spot it already tried, pick again
                if result == "Already Attacked":
                    continue

                print(f"AI fired at [{ai_r}, {ai_c}] → {result}")

                # Check if AI won or gets bonus turn
                if result == "Hit":
                    if len(user_board.ship_positions) == 0:
                        print("\n💀 YOU LOSE! Your fleet has been destroyed!")
                        game_result = f"Player LOST (All ships destroyed) - Round {round_num} - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                        file_manager.delete_saved_game()
                        break
                    else:
                        # AI gets another shot!
                        print("AI gets a bonus turn!")
                        continue

                # Miss = AI turn ends
                if result == "Miss":
                    comp_turns -= 1
                    break

            # Check again if AI destroyed all ships
            if len(user_board.ship_positions) == 0:
                print("\n💀 YOU LOSE! Your fleet has been destroyed!")
                game_result = f"Player LOST (All ships destroyed) - Round {round_num} - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                file_manager.delete_saved_game()
                break

        # ============================================================
        # ADVANCE TO NEXT ROUND ONLY IF SOMEONE STILL HAS TURNS
        # ============================================================
        if user_turns > 0 or comp_turns > 0:
            round_num += 1
    
    return game_result  # Return the result so main.py can save it


# ============================================================
# SAVE CURRENT GAME STATE
# ============================================================
def save_current_game(user_board, comp_board, user_turns, comp_turns, round_num):
    """Save the current game state to a file."""
    # Pack everything into a dictionary
    game_state = {
        "user_board": user_board.to_dict(),
        "comp_board": comp_board.to_dict(),
        "user_turns": user_turns,
        "comp_turns": comp_turns,
        "round_num": round_num
    }
    return file_manager.save_game_state(game_state)


if __name__ == "__main__":
    game()
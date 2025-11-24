import game_manager
import file_manager

# ============================================================
# MAIN MENU
# ============================================================
def menu():
    while True:
        print("\n========== BATTLESHIP MENU ==========")
        print("1. Start New Game")
        
        # Show resume option if saved game exists
        # Menu options change depending on whether there's a saved game
        if file_manager.has_saved_game():
            print("2. Resume Saved Game")
            print("3. View Past Results")
            print("4. Clear Saved Results")
            print("5. Delete Saved Game")
            print("6. Exit")
        else:
            print("2. View Past Results")
            print("3. Clear Saved Results")
            print("4. Exit")
        
        print("====================================")

        choice = input("Enter your choice: ").strip()

        # Adjust menu based on whether saved game exists
        has_save = file_manager.has_saved_game()

        # ================= START NEW GAME =================
        if choice == "1":
            # Warn if there's already a saved game
            if has_save:
                confirm = input("⚠️  A saved game exists. Starting a new game will overwrite it. Continue? (y/n): ").lower()
                if confirm != "y":
                    print("Cancelled.")
                    continue
            
            print("\nStarting new game...\n")
            # Run the game and get the result
            game_result = game_manager.game()
            
            # Save the game result automatically (if game finished)
            if game_result:
                file_manager.save_result(game_result)
                print("\n✓ Game result saved.")

        # ================= RESUME SAVED GAME =================
        elif choice == "2" and has_save:
            print("\nLoading saved game...\n")
            # Load the saved state from file
            saved_state = file_manager.load_game_state()
            
            if saved_state:
                # Resume the game with the loaded state
                game_result = game_manager.game(loaded_state=saved_state)
                
                # Save result if game finished
                if game_result:
                    file_manager.save_result(game_result)
                    print("\n✓ Game result saved.")
            else:
                print("❌ Failed to load saved game.")

        # ================= VIEW RESULTS =================
        # Menu number changes based on save file existence
        elif (choice == "2" and not has_save) or (choice == "3" and has_save):
            print("\n=== PAST RESULTS ===")
            # Load and display all past game results
            results = file_manager.load_results()
            for i, r in enumerate(results, 1):
                print(f"{i}. {r}")

        # ================= CLEAR RESULTS =================
        elif (choice == "3" and not has_save) or (choice == "4" and has_save):
            # Make sure they really want to delete everything
            confirm = input("Are you sure you want to clear all results? (y/n): ").lower()
            if confirm == "y":
                cleared = file_manager.clear_results()
                if cleared:
                    print("✓ All results cleared.")
                else:
                    print("No results file found.")
            else:
                print("Cancelled.")

        # ================= DELETE SAVED GAME =================
        elif choice == "5" and has_save:
            # Confirm before deleting
            confirm = input("Are you sure you want to delete the saved game? (y/n): ").lower()
            if confirm == "y":
                if file_manager.delete_saved_game():
                    print("✓ Saved game deleted.")
                else:
                    print("No saved game found.")
            else:
                print("Cancelled.")

        # ================= EXIT GAME =================
        # Exit option is at different positions depending on save file
        elif (choice == "4" and not has_save) or (choice == "6" and has_save):
            # Remind them if they have a saved game
            if has_save:
                print("\n⚠️  You have a saved game. You can resume it next time.")
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# ============================================================
# RUN PROGRAM
# ============================================================
if __name__ == "__main__":
    menu()
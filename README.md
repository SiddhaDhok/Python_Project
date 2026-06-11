PYTHON-PROJECT
# **Battleship Game**

A command-line implementation of the classic Battleship game where you face off against an AI opponent in turn-based naval combat.

## **Overview**

This is a strategic Battleship game played on a 10x10 grid. Players take turns attacking coordinates to find and destroy their opponent's fleet. The game features a unique turn pool system where each player starts with 20 turns, and successful hits earn bonus attacks. Save your progress at any time and resume later\!

## **Features**

* **20-turn battle system** \- Strategic resource management adds depth to gameplay  
* **Bonus attack mechanic** \- Hit a ship to earn an extra attack without consuming a turn  
* **Save and resume** \- Type 'save' during your turn to pause and continue later  
* **Comprehensive game history** \- All results saved with timestamps and detailed statistics  
* **Smart random AI** \- Challenging computer opponent  
* **Multiple victory paths**:  
  * Destroy all 8 enemy ships for an instant victory  
  * Outlast your opponent and have more surviving ships when turns expire  
  * Force a tactical draw if both fleets are equally damaged

  ## **Game Rules**

  ### **Setup**

1. Each player places 8 ships on a 10x10 grid (coordinates 0-9)  
2. Ships occupy single grid squares and cannot overlap  
3. Both players start with 20 turns

   ### **Gameplay**

1. **Taking Turns**: Players alternate attacking by entering row and column coordinates  
2. **Bonus Turns**: Successfully hitting a ship grants an immediate bonus attack (doesn't consume your turn count)  
3. **Misses**: Missing an attack ends your turn and consumes one turn from your pool  
4. **Winning**:  
   * **Instant Victory**: Destroy all 8 enemy ships at any point  
   * **Turn Limit Victory**: Have more surviving ships when both players run out of turns  
   * **Draw**: Equal ships remaining when turns are exhausted

   ### **Strategy Tips**

* Your 20 turns give you approximately 2 attacks per ship if you never miss  
* Each bonus turn from a hit is extremely valuable \- it's essentially a free attack  
* Consider spreading ships to avoid clusters that could be discovered together  
* Early game reconnaissance can pay dividends later

  ## **Installation**

**No dependencies required\!** This game uses only Python's standard library.

* Ensure you have Python 3.6 or higher installed  
* python \--version (to check the version)  
* Download all game files to the same directory:  
* \- main.py  
* \- game\_manager.py  
* \- board.py  
* \- ship.py  
* \- file\_manager.py


  ## **How to Play**

  ### **Starting the Game**

* python main.py


  ### **Main Menu**

The menu adapts based on whether you have a saved game:

**Without Saved Game:**

1. Start New Game  
2. View Past Results  
3. Clear Saved Results  
4. Exit

**With Saved Game:**

1. Start New Game  
2. Resume Saved Game  
3. View Past Results  
4. Clear Saved Results  
5. Delete Saved Game  
6. Exit

   ### **Ship Placement Phase**

When starting a new game, you'll place your 8 ships:

* Enter positions for 8 ships (row col):  
* Ship 1: 0 0  
* Ship 2: 2 3  
* Ship 3: 5 7  
* ...


**Placement Rules:**

* Enter coordinates as two space-separated numbers (0-9)  
* Format: `row column` (e.g., `3 5` places a ship at row 3, column 5\)  
* Ships cannot overlap with existing ships  
* Invalid positions will prompt you to try again  
* The board updates after each successful placement

  ### **Combat Phase**

**Your Turn:**

* Your Turn (Remaining turns: 20\)  
* (Type 'save' to save and quit)  
* Enter attack (row col): 4 6  
    
* Enter coordinates to attack: `row column`  
* Type `save` instead to save your progress and exit  
* Hit a ship to earn a bonus turn immediately  
* Miss to end your turn and decrease your turn count

**AI Turn:** The computer automatically attacks during its turn. Watch for its targeting and adjust your strategy\!

### **Reading the Board**

* 0 1 2 3 4 5 6 7 8 9  
* 0 S     X              
* 1       O   S          
* 2 S         S          
* 3     O                
* 4                 S    
* ……………………


**Symbol Legend:**

* `S` \- Your ship (only visible on your own board)  
* `O` \- Hit\! A ship has been destroyed here  
* `X` \- Miss \- nothing but empty water  
* (space) \- Unknown territory / Empty water

**You'll see two boards:**

* **Your Board**: Shows your ships (S), enemy hits (O), and enemy misses (X)  
* **Computer Board**: Shows only your hits (O) and misses (X) \- enemy ships are hidden

  ## **Project Structure**

* Battleship:  
* ├── main.py                          \# Entry point \- menu system and game flow  
* ├── game\_manager.py         \# Core game logic, turn management, win conditions  
* ├── board.py                         \# Board class \- grid management and display  
* ├── ship.py                            \# Ship placement and attack mechanics  
* ├── file\_manager.py              \# Persistence layer \- save/load/history  
* ├── battleship\_save.txt         \# Auto-generated game results history  
* └── saved\_game.json           \# Auto-generated current game save file


  ## **Code Architecture**

  ### **Main Components**

**main.py** \- Application Entry Point

* Dynamic menu system that adapts to game state  
* Orchestrates game flow and user choices  
* Handles game result persistence

**game\_manager.py** \- Game Engine

* Controls the main game loop and turn sequence  
* Manages both player and AI turns with bonus attack logic  
* Implements win condition checking  
* Handles save/resume functionality  
* Tracks round numbers and turn counts

**board.py** \- Board Management

* `Board` class representing the 10x10 game grid  
* Maintains three key sets: ship positions, hits, and misses  
* Provides display methods with optional ship visibility  
* Includes ship placement with validation  
* Serialization methods (`to_dict`/`from_dict`) for save system

**ship.py** \- Combat Mechanics

* User ship placement with input validation  
* Attack resolution system  
* Hit/miss detection logic  
* Returns attack results: "Hit", "Miss", "Invalid", or "Already Attacked"

**file\_manager.py** \- Data Persistence

* JSON-based save/load system for game state  
* Text-based results logging with timestamps  
* File existence checking and management utilities  
* CRUD operations for both save files and result history

  ### **Key Design Patterns**

**State Serialization**: Boards convert to dictionaries for JSON storage, with sets converted to lists for serialization compatibility.

**Result-Oriented Design**: Attack functions return descriptive strings rather than boolean values, making game logic more readable.

**Separation of Concerns**: Each module has a single, well-defined responsibility, making the codebase maintainable and testable.

## **Save System Details**

### **What Gets Saved**

The save system captures your complete game state:

* Both player and computer board states (ships, hits, misses)  
* Current turn counts for both players  
* Current round number  
* All position data for full game reconstruction

  ### **Save File Location**

* **Active Game**: `saved_game.json` (JSON format)  
* **Game History**: `battleship_save.txt` (text format, one result per line)

  ### **When to Save**

* Type `save` during your turn to pause the game  
* Games are automatically saved before you exit  
* Completed games automatically delete the save file  
* Results are logged after every completed game

  ### **Save File Format**

* {  
*   "user\_board": {  
*     "size": 10,  
*     "ship\_positions": \[\[0,0\], \[1,1\], ...\],  
*     "hit\_positions": \[\[2,3\], ...\],  
*     "miss\_positions": \[\[5,5\], ...\]  
*   },  
*   "comp\_board": { ... },  
*   "user\_turns": 15,  
*   "comp\_turns": 12,  
*   "round\_num": 8  
* }


  ## **Game Statistics**

Results are logged with comprehensive information:

**Victory by Destruction:**

* Player WON (Destroyed all ships) \- Round 9 \- 2025-11-24 23:25


**Victory by Ship Count:**

* Player WON \- Ships: Player hit 6 ships and AI hit 3 \- 2025-11-24 23:22


**Defeat:**

* Player LOST (All ships destroyed) \- Round 12 \- 2025-11-24 23:34


**Draw:**

* DRAW \- Ships: Player hit 4 and AI hit 4 \- 2025-11-24 23:32


View your complete battle history anytime from the main menu\!

## **Winning Strategies**

### **Offensive Tactics**

* **Maximize Bonus Turns**: Each hit gives you a free attack. String together hits to stretch your 20 turns further.  
* **Pattern Your Attacks**: Consider checkerboard or line patterns to maximize coverage.  
* **Endgame Awareness**: Track how many enemy ships remain vs. your turns left.

  ### **Defensive Tactics**

* **Spread Formation**: Don't cluster ships in one area.  
* **Corner Strategy**: Corners are statistically attacked less often early game.  
* **Edge Placement**: Consider mixing edge and center placements.

  ### **Resource Management**

* **Turn Conservation**: Every miss matters. Make educated guesses when possible.  
* **Calculate Odds**: With 8 ships on 100 squares, you have an 8% base hit chance.  
* **Know When to Risk**: Sometimes aggressive plays are worth it if you're behind.

  ## **Troubleshooting**

**Game won't start:**

* Ensure all 5 Python files are in the same directory  
* Check you're running Python 3.6 or higher

**Save file issues:**

* The game creates files automatically \- no setup needed  
* If save files become corrupted, delete them and start fresh  
* Save files are plain text (JSON) and can be manually inspected

**Input problems:**

* Coordinates must be integers from 0-9  
* Use space to separate row and column: `3 5` not `3,5`  
* Type `save` (not "save" with quotes) to save during your turn



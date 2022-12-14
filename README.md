# cse210-02
Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

Hilo is played according to the following rules:

- The player starts the game with 300 points.
- Individual cards are represented as a number from 1 to 13.
- The current card is displayed.
- The player guesses if the next one will be higher or lower.
- The the next card is displayed.
- The player earns 100 points if they guessed correctly.
- The player loses 75 points if they guessed incorrectly.
- If a player reaches 0 points the game is over.
- If a player has more than 0 points they decide if they want to keep playing.
- If a player decides not to play again the game is over.

***Authors: Aaron Wilson (aarjwilson@gmail.com)***<br>
***Software Needed: Python***

The Hilo_game_design.plantuml may require you to use **"plantuml"** and **"graphviz"** to view it properly.

#### Project Structure
- The main.py file runs the game.
- The card.py and director.py contain the classes and functions for the game to work.

See the Hilo_game_design.plantuml for a visual of the classes, functions, and values within the game structure.

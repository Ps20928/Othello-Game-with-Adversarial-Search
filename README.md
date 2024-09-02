# Reversi (Othello) Game Implementation

This project is a Python-based implementation of the classic board game Reversi (also known as Othello). The goal of this project is to simulate the game using Python, where players can compete against each other or against an AI.

## Problem Definition

The objective is to have the majority of discs of your color (either black or white) on the board at the end of the game. The game is played on an 8x8 grid board, and players take turns placing discs on the board to capture their opponent's discs.

## Game Rules

- *Board Setup*: The board starts with two black and two white discs placed diagonally in the center.
- *Player Turns*: Players alternate turns, with black always going first.
- *Legal Moves*: A move is legal if it flanks one or more of the opponent's discs in a straight line (horizontal, vertical, or diagonal).
- *Flipping Discs*: When a legal move is made, all opponent's discs that are flanked by the player's discs are flipped to the player's color.
- *Turn Skipping*: If a player has no legal moves, their turn is skipped.
- *Game End*: The game ends when the board is full or neither player can make a legal move.
- *Winning*: The player with the most discs of their color on the board at the end wins.

## Input Description

- *Player Moves*: Players specify the row and column where they want to place their disc.
- *Game Board State*: The board is an 8x8 grid with the following values:
  - 0: Empty cell
  - 1: Black disc (Player 1)
  - 2: White disc (Player 2)
- *AI Decision Making*: The AI uses the Minimax algorithm with Alpha-Beta pruning to determine the best move.

## Implementation Details

### Classes and Functions

- *ReversiBoard Class*:
  - __init__: Initializes the board with the starting positions.
  - get_board: Returns the current board state.
  - is_empty: Checks if a cell is empty.
  - place_disc: Places a disc and flips the opponent's discs if flanking occurs.
  - flip_discs: Flips discs in all eight directions if flanked.

- *is_valid_move Function*: Checks if a move is valid by analyzing potential flanking.
- *evaluate_game_state Function*: Evaluates the game state by counting the number of discs for each player.
- *is_game_over Function*: Determines if the game is over.
- *Minimax Algorithm*: Used by the AI to find the best move, optimized with Alpha-Beta pruning.

### Parameters

- *depth*: The depth of the search tree for the Minimax algorithm.
- *player*: The current player making the move.
- *maximizing_player*: Boolean indicating if the current move is for maximizing or minimizing the score.
- *alpha and beta*: Parameters for Alpha-Beta pruning to optimize the search.

### find_best_move Function

- Uses the Minimax algorithm to find the best move for the AI.

### Print Board Function

- Displays the current state of the game board.

### Main Function

- Controls the game flow, alternating between players and determining the winner.

## Output/Results

The program outputs the state of the game board after each move, showing how discs are flipped and the board evolves.

## References

- [Reversi/Othello Rules](https://en.wikipedia.org/wiki/Reversi)
- [Minimax Algorithm](https://en.wikipedia.org/wiki/Minimax)
- [Alpha-Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)


import numpy as np

class ReversiBoard:
  
  #The Reversi game board as a 2D array.
  
  def __init__(self):
    # Initialize the board with all empty cells (0)
    self.board = np.zeros((8, 8), dtype=int)

    # Set the starting positions (center four squares)
    self.board[3, 3] = 2
    self.board[4, 4] = 2
    self.board[3, 4] = 1
    self.board[4, 3] = 1

  def get_board(self):
    return self.board

  def is_empty(self, row, col):
    return self.board[row, col] == 0

  def place_disc(self, row, col, player):
    if not self.is_empty(row, col):
      return False  # Invalid move (cell not empty)

    self.board[row, col] = player
    self.flip_discs(row, col, player)#flips opponent's discs if flanking occurs.
    return True

  def flip_discs(self, row, col, player):
  
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
      x, y = row + dx, col + dy
      # Check if there's a chain of opponent's discs followed by our disc
      while 0 <= x < 8 and 0 <= y < 8 and self.board[x, y] == (3 - player):
        x += dx
        y += dy
      if 0 <= x < 8 and 0 <= y < 8 and self.board[x, y] == player:
        # Flip all discs in the chain
        for i in range(1, x - row + 1):
          self.board[row + i * dx, col + i * dy] = player

def is_valid_move(board, row, col, player):
  if not board[row, col] == 0:
    return False

  # Check for flanking in any of the eight directions
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1)]
  for dx, dy in directions:
    x, y = row + dx, col + dy
    opponent = 3 - player  # Opponent's player number
    # Check if there's a chain of opponent's discs followed by our disc
    while 0 <= x < 8 and 0 <= y < 8 and board[x, y] == opponent:
      x += dx
      y += dy
    if 0 <= x < 8 and 0 <= y < 8 and board[x, y] == player:
      return True

  # No flanking found in any direction
  return False

def evaluate_game_state(board):
 # Evaluates the game state for Reversi based on the number of discs each player has on the board.
  player1_score = 0
  player2_score = 0
  for row in range(8):
    for col in range(8):
      if board[row, col] == 1:
        player1_score += 1
      elif board[row, col] == 2:
        player2_score += 1
  return player1_score, player2_score

def is_game_over(board):
  #Checks if the game is over in Reversi (no empty cells or no valid moves).
 
  # Check for empty cells
  for row in range(8):
    for col in range(8):
      if board[row, col] == 0:
        return False

  # Check for valid moves for both players
  for player in (1, 2):
    for row in range(8):
      for col in range(8):
        if is_valid_move(board, row, col, player):
          return False

  return True

def minimax(board, depth, player, maximizing_player, alpha=-float('inf'), beta=float('inf')):

  #Implements the Minimax algorithm with Alpha-Beta Pruning for Reversi.
  # Terminal state or depth reached.
  
  if depth == 0 or is_game_over(board):
    return evaluate_game_state(board)

  if maximizing_player:
    best_score = -float('inf')
    best_move = None
    for row in range(8):
      for col in range(8):
        if is_valid_move(board, row, col, player):
          # Simulate the move
          new_board = board.copy()
          new_board[row, col] = player
          # Recursive evaluation with updated alpha
          score, _ = minimax(new_board, depth - 1, 3 - player, False, alpha, beta)
          alpha = max(alpha, score)  # Update alpha for maximizing player
          if score > best_score:
            best_score = score
            best_move = (row, col)
          # Prune if beta is less than or equal to alpha 
          if beta <= alpha:
            break
    return best_score, best_move
  else:
    worst_score = float('inf')
    for row in range(8):
      for col in range(8):
        if is_valid_move(board, row, col, player):
          # Simulate the move
          new_board = board.copy()
          new_board[row, col] = player
          # Recursive evaluation with updated beta
          score, _ = minimax(new_board, depth - 1, 3 - player, True, alpha, beta)
          beta = min(beta, score)  # Update beta for minimizing player
          if score < worst_score:
            worst_score = score
          # Prune if beta is less than or equal to alpha
          if beta <= alpha:
            break
    return worst_score, None


def find_best_move(board, player, depth=6):
  # Finds the best move for the given player using Minimax algorithm.
  # Depth decides game's difficulty level.
  score, move = minimax(board.copy(), depth, player, True)
  return move

import numpy as np

def print_board(board):
  # Prints the current state of the Reversi game board
  # Symbols for players here player 1: X player2: 0
  symbols = {0: " ", 1: "X", 2: "O"}

  print("   ", end="")
  for col in range(8):
    print(col, end=" ")
  print("")


  for row in range(8):
    print(row, end="  ")
    for col in range(8):
      print(symbols[board[row, col]], end=" ")
    print("")

  print("")  

def main():
  board = ReversiBoard()
  current_player = 1  # Player 1 starts

  while not is_game_over(board.get_board()):
    print_board(board.get_board())

    if current_player == 1:
      # Get human player move
      row, col = input("Enter your move (row, col): ").split(",")
      row, col = int(row), int(col)
      while not is_valid_move(board.get_board(), row, col, current_player):
        print("Invalid move. Try again.")
        row, col = input("Enter your move (row, col): ").split(",")
        row, col = int(row), int(col)
      board.place_disc(row, col, current_player)
    else:
      # Get AI player move (using find_best_move)
      row, col = find_best_move(board.get_board(), current_player)
      board.place_disc(row, col, current_player)
      print(f"AI Player ({current_player}) placed disc at ({row},{col})")

    current_player = 3 - current_player  # Switch player

  # Game Over
  print_board(board.get_board())
  player1_score, player2_score = evaluate_game_state(board.get_board())
  if player1_score > player2_score:
    print("Player 1 wins!")
  elif player1_score < player2_score:
    print("Player 2 wins!")
  else:
    print("It's a tie!")

if __name__ == "__main__":
  main()

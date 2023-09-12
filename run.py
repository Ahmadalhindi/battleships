from random import randint
# Constant variables
size = 5
num_ships = 4

# Other variables
player_board = [[" [ ] " for x in range(size)] for x in range(size)]
computer_board = [[" [ ] " for x in range(size)] for x in range(size)]


# Game logo and starting
print("Welcome to the battleships game")
print(f"Board size: {size}, number of ship: {num_ships}")
print("_" * 30)


# Function to print the board that established
def print_board(board):
    for row in board:
      print(" ".join(row))

# Function to randomly Add ships in the boards
def add_ships(player_board, computer_board):
    for _ in range(num_ships):
      while True:
        user_ship_row = randint(0, size - 1)
        user_ship_col = randint(0, size - 1)
        if player_board[user_ship_row][user_ship_col] == " [ ] ":
            player_board[user_ship_row][user_ship_col] = " [p] "
        computer_ship_row = randint(0, size - 1)
        computer_ship_col = randint(0, size - 1)
        if computer_board[computer_ship_row][computer_ship_col] == " [ ] ":
            computer_board[computer_ship_row][computer_ship_col] = " [c] "
            break

add_ships(player_board, computer_board)
print("Player board:")
print_board(player_board)
print("Computer board:")
print_board(computer_board)
# Create boards for each of participants
# Function to validate the entered data by the player
# Player guesses and turn to play
# Computer turn to play
# Check for scores for each
# Check for the last winner
# Hints

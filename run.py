
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
# Create boards for each of participants
# Function to validate the entered data by the player
# Player guesses and turn to play
# Computer turn to play
# Check for scores for each
# Check for the last winner
# Hints

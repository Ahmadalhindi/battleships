from random import randint
# Constant variables
size = 5
num_ships = 4

# variables for boards
player_board = [["[   ]" for x in range(size)] for x in range(size)]
computer_board = [["[   ]" for x in range(size)] for x in range(size)]

# Game logo and starting
print("Welcome to the battleships game")
print(f"Board size: {size}, number of ship: {num_ships}")
print("_" * 30)


def print_board(board):
    """
    Function to print a board.
    """
    for row in board:
        print(" ".join(row))


def add_ships(player_board, computer_board):
    """
    Function for Add ships randomly in each board.
    """
    for _ in range(num_ships):
        user_ship_row = randint(0, size - 1)
        user_ship_col = randint(0, size - 1)
        comp_ship_row = randint(0, size - 1)
        comp_ship_col = randint(0, size - 1)
        while True:
            if player_board[user_ship_row][user_ship_col] == "[   ]":
                player_board[user_ship_row][user_ship_col] = "[< >]"
            elif computer_board[comp_ship_row][comp_ship_col] == "[   ]":
                computer_board[comp_ship_row][comp_ship_col] = "[> <]"
                break


# Function to guess the locatation of computer's ships by the user
def user_guess():
    """
    Function allows player start playing by guessing
    the row and col numbers on the computer board.
    """
    row_guess = input("Guess Row:\n")
    col_guess = input("Guess col:\n")
    print(f"You guess: ({row_guess}, {col_guess})")


add_ships(player_board, computer_board)
print("Player board:")
print_board(player_board)
print("Computer board:")
print_board(computer_board)
user_guess()
# Create boards for each of participants
# Function to validate the entered data by the player
# Player guesses and turn to play
# Computer turn to play
# Check for scores for each
# Check for the last winner
# Hints

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
        if player_board[user_ship_row][user_ship_col] == "[   ]":
            player_board[user_ship_row][user_ship_col] = "[< >]"
        if computer_board[comp_ship_row][comp_ship_col] == "[   ]":
            computer_board[comp_ship_row][comp_ship_col] = "[> <]"


# Function to guess the locatation of computer's ships by the user
def user_guess():
    """
    Function allows player start playing by guessing
    the row and col numbers on the computer board.
    """
    while True:
        row_guess = input("Guess Row: <number within board size (0-4)> \n")
        col_guess = input("Guess col: <number within board size (0-4)> \n")
        if validate_data(row_guess, col_guess):
            player_turn(row_guess, col_guess)
            break


def validate_data(row_guess, col_guess):
    """
    Inside try check if the inputs are no biger than 4
    and other than integers.
    """
    try:
        if int(row_guess) > size or int(col_guess) > size:
            print(f"the number is out the limit of the board size {size}\n")
            return False
    except ValueError:
        print("Invalid input, please enter a numerical values.\n")
        return False
    return True


def player_turn(row_guess, col_guess):
    """
    Check with feedback if the player hit or miss the
    target on computer board,
    return to guess again if guess the same number again
    """
    if computer_board[int(row_guess)][int(col_guess)] == "[> <]":
        computer_board[int(row_guess)][int(col_guess)] = "[<x>]"
        print(f"You guess: ({row_guess}, {col_guess}), and hit a ship")
    elif computer_board[int(row_guess)][int(col_guess)] == "[   ]":
        computer_board[int(row_guess)][int(col_guess)] = "[ x ]"
        print(f"You guess: ({row_guess}, {col_guess}), and miss a ship")
    else:
        print(f"You already guessed ({row_guess}, {col_guess}). Plz try again")
        user_guess()
    print_board(computer_board)


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

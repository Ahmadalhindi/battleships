from random import randint
# Constant variables
size = 5
num_ships = 5
player_hit = []
computer_hit = []

# variables for boards
player_board = [["[   ]" for x in range(size)] for x in range(size)]
computer_board = [["[   ]" for x in range(size)] for x in range(size)]


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
        # adding ships randomly for both boards.
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
        # variables let user to guess the row and col in computer board
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
    target on computer board.

    Return to guess again if guess the same number again.

    Display a total score for evey hit to the target in the
    player hit list.
    """
    if computer_board[int(row_guess)][int(col_guess)] == "[> <]":
        computer_board[int(row_guess)][int(col_guess)] = "[<x>]"
        print(f"You guessed: ({row_guess}, {col_guess}), and hit")
        player_hit.append(1)
        player_score = sum(player_hit)
        print(f"Your score for this round is: ({player_hit[0]})")
        print(f"Your total score is: {player_score}")
    elif computer_board[int(row_guess)][int(col_guess)] == "[   ]":
        computer_board[int(row_guess)][int(col_guess)] = "[ x ]"
        print(f"You guessed: ({row_guess}, {col_guess}), and missed")
    else:
        print(f"You already guessed ({row_guess}, {col_guess}). Plz try again")
        user_guess()
    computer_turn()


def computer_turn():
    """
    Check with feedback if the computer hit or miss the
    target on player board.

    Return to function again if computer guess the same number again

    display a total score for evey hit to the target in the
    computer hit list
    """
    comp_row_guess = randint(0, size - 1)
    comp_col_guess = randint(0, size - 1)
    if player_board[comp_row_guess][comp_col_guess] == "[< >]":
        player_board[comp_row_guess][comp_col_guess] = "[<x>]"
        print(f"Computer guessed: ({comp_row_guess},{comp_col_guess}) & hit")
        computer_hit.append(1)
        computer_score = sum(computer_hit)
        print(f"Computer score for this round is: ({computer_hit[0]})")
        print(f"Computer total score is: {computer_score}")
    elif player_board[comp_row_guess][comp_col_guess] == "[   ]":
        player_board[comp_row_guess][comp_col_guess] = "[ x ]"
        print(f"Computer guessed:({comp_row_guess},{comp_col_guess}) & missed")
    else:
        computer_turn()


def continue_game():
    """
    continue playing the game from the user guess function
    untill the request if the user wish to end th game.
    """
    user_guess()
    print("")
    print("Computer board:")
    print_board(computer_board)
    print("Player board:")
    print_board(player_board)
    next_round = str(input("Would you like to continue playing? (y, n)\n"))
    if next_round == 'y':
        continue_game()
    elif next_round == 'n':
        print("Thanks for playing.")
    else:
        print("Please answer by y or n.")
        return next_round


def play_game():
    """
    Start the game by welcoming with instructions.

    Print the user and computer boards after adding
    ships randomly for both.
    """
    print("Welcome to the battleships game")
    print(f"Board size: {size}, number of ship: {num_ships}")
    print("_" * 30)
    add_ships(player_board, computer_board)
    print("Computer board:")
    print_board(computer_board)
    print("Player board:")
    print_board(player_board)
    print("_" * 30)
    continue_game()


play_game()
from random import randint
# Constant variables
size = 5
num_ships = 5
rounds = 0
max_round = 7  # Here you can adjust the max round.
player_hit = []
computer_hit = []
# Variables for boards.
# Get a hint to these variables from the course in project example.
player_board = [["[   ]" for x in range(size)] for x in range(size)]
computer_board = [["[   ]" for x in range(size)] for x in range(size)]


# Get a hint to this function from the course in project example.
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
        # Adding ships randomly for both boards.
        user_ship_row = randint(0, size - 1)
        user_ship_col = randint(0, size - 1)
        comp_ship_row = randint(0, size - 1)
        comp_ship_col = randint(0, size - 1)
        if player_board[user_ship_row][user_ship_col] == "[   ]":
            player_board[user_ship_row][user_ship_col] = "[< >]"
        if computer_board[comp_ship_row][comp_ship_col] == "[   ]":
            computer_board[comp_ship_row][comp_ship_col] = "]   ["


# Function to guess the locatation of computer's ships by the user
def user_guess():
    """
    Function allows player start playing by guessing
    the row and col numbers on the computer board.
    """
    while True:
        # Variables allow user to guess the row and col in computer board.
        row_guess = input("Guess Row?(number between 0-4)\n")
        col_guess = input("Guess col?(number between 0-4)\n")
        if validate_data(row_guess, col_guess):
            player_turn(row_guess, col_guess)
            break


# Get a hint to this function from Love Sandwiches Walkthrough Project.
def validate_data(row_guess, col_guess):
    """
    Inside try check if the inputs are numbers and limited to
    the board size.
    """
    try:
        if int(row_guess) > size-1 or int(col_guess) > size-1:
            print(f"The number is out the limit of the board size(0-4)\n")
            return False
    except ValueError:
        print("Invalid input, please enter a numerical value.\n")
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
    global player_score
    if computer_board[int(row_guess)][int(col_guess)] == "]   [":
        computer_board[int(row_guess)][int(col_guess)] = "[<x>]"
        print(f"You guessed: ({row_guess}, {col_guess}), and hit")
        player_hit.append(1)
        player_score = sum(player_hit)
        print(f"Your score now: ({player_hit[0]})")
        print(f"Your total score: ({player_score})")
    elif computer_board[int(row_guess)][int(col_guess)] == "[   ]":
        computer_board[int(row_guess)][int(col_guess)] = "[ x ]"
        print(f"You guessed: ({row_guess},{col_guess}), and missed")
    else:
        print(f"You already guessed ({row_guess}, {col_guess}). Try again")
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
    global computer_score
    comp_row_guess = randint(0, size - 1)
    comp_col_guess = randint(0, size - 1)
    if player_board[comp_row_guess][comp_col_guess] == "[< >]":
        player_board[comp_row_guess][comp_col_guess] = "[<x>]"
        print(f"Computer guessed: ({comp_row_guess},{comp_col_guess}) & hit")
        computer_hit.append(1)
        computer_score = sum(computer_hit)
        print(f"Computer score now: ({computer_hit[0]})")
        print(f"Computer total score: ({computer_score})")
    elif player_board[comp_row_guess][comp_col_guess] == "[   ]":
        player_board[comp_row_guess][comp_col_guess] = "[ x ]"
        print(f"Computer guessed:({comp_row_guess},{comp_col_guess}) & missed")
    else:
        computer_turn()


def continue_game(rounds):
    """
    continue playing the game from the user guess function
    untill the request if the user wish to end th game.
    """
    while True:
        rounds += 1
        print(f"           Round ({rounds})")
        user_guess()
        print("")
        print("Computer board:")
        print_board(computer_board)
        print("Player board:")
        print_board(player_board)
        print("_" * 30)
        while True:
            if rounds <= (max_round-1):
                next_round = str(input("Will you continue playing?(y, n)\n"))
                if next_round == 'y':
                    continue_game(rounds)
                    return False
                elif next_round == 'n':
                    print("Thanks for playing.")
                    return False
                else:
                    print("Please answer by y or n.\n")
            else:
                print("*" * 30)
                print(f"Game reached the last round: ({max_round})")
                if sum(player_hit) > sum(computer_hit):
                    print("Congratulation you win.")
                elif sum(computer_hit) > sum(player_hit):
                    print("Computer win.")
                else:
                    print("Game result: it's a tie.")
                break
        break


def play_game():
    """
    Start the game by welcoming with instructions.

    Print the user and computer boards after adding
    ships randomly for both.
    """
    # Logo; wavy by Brian Krog.
    print("*" * 30)
    print("  Welcome to Battleships game")
    print(f"Board size: {size}, ships number: {num_ships}")
    print(f"         Max round: {max_round}")
    print("   Result on the last round")
    print("    Hit: [<x>], miss: [ x ]")
    print("*" * 30)
    add_ships(player_board, computer_board)
    print("Computer board:")
    print_board(computer_board)
    print("Player board:")
    print_board(player_board)
    print("_" * 30)
    continue_game(rounds)


def main():
    play_game()


main()

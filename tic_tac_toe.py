import time
import os


def game_rules():
    return print("At any point during the game you are able to: "
                 "\nenter 'R' to restart the game, "
                 "\nenter 'Q' to quit the game. "
                 "\nBoard layout corresponds to the numpad grid"
                 "\nGood Luck!")


#  type in your favorite look of the square, examples: '_', '=', '`'
grid_type = '-'
#  creates a list with 9 elements that will be used to build a 3x3 grid for the game
board = [grid_type for x in range(9)]

player_x = 'X'
player_o = 'O'
#  starting player (X)
current_player = player_x


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_board():

    print(board[6] + ' ' + board[7] + ' ' + board[8])
    print(board[3] + ' ' + board[4] + ' ' + board[5])
    print(board[0] + ' ' + board[1] + ' ' + board[2])


def quit_game(user_input):
    return user_input.lower() == 'q'


def restart_game(user_input):
    return user_input.lower() == 'r'


#  checks if the position input is valid- a single digit
def num_input(user_input):
    return user_input.isdigit() and len(user_input) == 1


def row_win():
    row_1 = board[0] == board[1] == board[2] != grid_type
    row_2 = board[3] == board[4] == board[5] != grid_type
    row_3 = board[6] == board[7] == board[8] != grid_type

    return row_1 or row_2 or row_3


def column_win():
    column_1 = board[0] == board[3] == board[6] != grid_type
    column_2 = board[1] == board[4] == board[7] != grid_type
    column_3 = board[2] == board[5] == board[8] != grid_type

    return column_1 or column_2 or column_3


def diagonal_win():
    diagonal_1 = board[0] == board[4] == board[8] != grid_type
    diagonal_2 = board[2] == board[4] == board[6] != grid_type

    return diagonal_1 or diagonal_2


def win():
    return row_win() or column_win() or diagonal_win()


def draw():
    if grid_type in board:
        return False
    else:
        return True


def main():
    game_rules()

    global current_player
    global board

    while True:
        display_board()

        user_input = input(f"Enter a number from 1 to 9, {current_player}'s turn: ").strip()

        #  q or Q input ends the game
        if quit_game(user_input):
            print('\nThanks for playing!')
            time.sleep(1)
            clear_terminal()
            exit()

        #  r or R input restarts the game
        if restart_game(user_input):
            #  clears the board
            board = [grid_type for x in range(9)]
            clear_terminal()
            main()
            break

        #  if num_input(user_input) is not a single digit it returns False
        if not num_input(user_input):
            print("\nWrong input, try again!\n")
            continue
        elif 'O' in board[int(user_input) - 1]:
            print(f"\nPosition {user_input} is already taken, try again!\n")
            continue
        elif 'X' in board[int(user_input) - 1]:
            print(f"\nPosition {user_input} is already taken, try again!\n")
            continue

        #  marks an open space with X or O
        board[int(user_input) - 1] = current_player

        if win():
            display_board()
            print(f'\n{current_player} is a winner!')
            print('Good Game!')
            break

        if draw():
            display_board()
            print('\nDraw!')
            break

        #  swaps players
        if current_player == 'X':
            current_player = player_o
        elif current_player == 'O':
            current_player = player_x

    while True:

        user_input = input("\nWould you like to play again? 'Y'/'N': ").strip()

        if user_input.lower() == 'y':
            board = [grid_type for x in range(9)]
            clear_terminal()
            main()
        elif user_input.lower() == 'n':
            print("\nThanks for playing!")
            time.sleep(1)
            clear_terminal()
            exit()
        else:
            print('\nWrong input!')
            continue


main()

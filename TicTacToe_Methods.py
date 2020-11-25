import os
import random

def clear():
    os.system("clear")


def display_board(board):
    # lear the old board first
    clear()  
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
   

def player_input():
    # Set an initial 'marker' to be empty. It will be filled in the function.
    marker = ''
    # Set condition for while loop.
    not_chosen_marker = True
    while not_chosen_marker:
        marker = input('Player 1, Do you want to be X or O?: ').upper()
        if marker == 'X':
            not_chosen_marker = False
            return ('X', 'O')
        elif marker == 'O':
            not_chosen_marker = False
            return ('O', 'X')
        else:
            # Will continue to loop until 'o' or 'x' are chosen.
            not_chosen_marker = True
            print("\nSorry, I dont understand")

def place_marker(board, marker, position):
    # places the marker on the board
    board[position] = marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
    # Random toss to determine who goes first.
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    # Check if there are empty spaces on the board.
    return board[position] == ' '

def full_board_check(board):
    # Check if the board is full.
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    # Provide the player an option to place their marker.
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose your next position (1-9): ')) 
    return position


def replay():
    # Replay option for the game.
    not_chosen_option = True
    while not_chosen_option:
        option = input('Do you want to play again? Enter Yes or No: ').lower()
        if option == 'y':
            not_chosen_option = False
            return True
        elif option == 'n':
            not_chosen_option = False
            return False
        else:
            print("\nSorry, I don't understand!")
            not_chosen_option = True

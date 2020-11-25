from TicTacToe_Methods import *
import os
import random
import time

print('Welcome to Tic Tac Toe!')

def start():
    while True:
        # Reset the board
        theBoard = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print("\n")
        print(turn + ' will go first!')
        
        play_game = input('Are you ready to play? Yes or No: ')
        
        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                # Player1's turn.
                
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print('\nCongratulations Player 1! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('\nThe game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.
                
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('\nPlayer 2 has won the game!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('\nThe game is a draw!')
                        break
                    else:
                        turn = 'Player 1'

        if not replay():
            clear()
            print("\nThanks for playing! See you soon.")
            time.sleep(1)
            break

start()
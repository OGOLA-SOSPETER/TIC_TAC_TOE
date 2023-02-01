#The tic-tac-toe game

game_board = {'7': '', '8': '', '9': '',
              '4': '', '5': '', '6': '',
              '1': '', '2': '', '3': '',
              }
player = 'X'
count = 0
message = "Congratulations, Player " + player + ". You Won✨🎉🎉"
def printboard(board):
    print(' ' + board['7'] + ' | ', board['8'] + ' | ', board['9'])
    print('-+-+-')
    print(' ' + board['4'] + ' | ', board['5'] + ' | ', board['6'])
    print('-+-+-')
    print(' ' + board['1'] + ' | ', board['2'] + ' | ', board['3'])
    print('-+-+-')

def gameplay():

    global player
    global count
    for a in range(10):
        printboard(game_board)
        print("It is your turn, Player " + player + "  to play.\t Move to which position?")
        move = input()
        if game_board[move] == '':
            game_board[move] = player
            count = count + 1
            counter = count
        else:
            print('Try another position!!')
            count = counter
            continue

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

        if count >= 5:
            if game_board['7'] == game_board['8'] == game_board['9'] == player:  # across the top
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                break
            elif game_board['4'] == game_board['5'] == game_board['6'] == player:  # across the middle
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                break
            elif game_board['1'] == game_board['2'] == game_board['3'] == player:  # across the bottom
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                break
            elif game_board['1'] == game_board['4'] == game_board['7'] == player:  # down the left side
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                break
            elif game_board['2'] == game_board['5'] == game_board['8'] == player:  # down the middle
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                break
            elif game_board['3'] == game_board['6'] == game_board['9'] == player:  # down the right side
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                break
            elif game_board['7'] == game_board['5'] == game_board['3'] == player:  # diagonal
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                break
            elif game_board['1'] == game_board['5'] == game_board['9'] == player:  # diagonal
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                break

            else:
                continue

            # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nRound one Over😁😎.\n")
            print("It's a Tie!!")

            # we have to change the player after every move.




gameplay()

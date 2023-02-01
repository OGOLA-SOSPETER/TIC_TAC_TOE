#The tic-tac-toe game

#Designing the board
game_board = {'7': '', '8': '', '9': '',
              '4': '', '5': '', '6': '',
              '1': '', '2': '', '3': '',
              }
#Player
player = 'X'
count = 0
player1_score = 0
player2_score = 0
player1 = ''
player2 = ''
#Message on winning
message = "Congratulations, Player " + player + ". You Won✨🎉🎉"

#The GameBoard Displayed
def printBoard(board):
    print(' ' + board['7'] + ' | ', board['8'] + ' | ', board['9'])
    print('--+---+--')
    print(' ' + board['4'] + ' | ', board['5'] + ' | ', board['6'])
    print('--+---+--')
    print(' ' + board['1'] + ' | ', board['2'] + ' | ', board['3'])

def getPlayers():
    global player1,player2
    print('Player1, [X], Enter your name: ')
    player1 = input()
    print('Player2, [O], Enter your name: ')
    player2 = input()

def Report():
    global player1_score,player2_score
    # The total Score
    print('\t\t\t' + '-' * 57)
    print('\t' * 7 + 'Tic_Tac_Toe Game Challenge.')
    print('\t\t\t' + '-' * 57)

    print(player1 + '\t' * 3, player1_score)
    print(player2 + '\t' * 3, player2_score)


def printboard(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}   |  {}   |  {}".format(board['7'], board['8'], board['9']))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}   |  {}   |  {}".format(board['4'], board['5'], board['6']))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}   |  {}   |  {}".format(board['1'], board['2'], board['3']))
    print("\t     |     |")
    print("\n")
#The Game
def gameplay():

    global player
    global count
    global player1_score
    global player2_score
    for a in range(10):
        printboard(game_board)
        print("It is your turn, Player " + player + "  to play.\t Move to which position?")
        move = input()
        if game_board[move] == '':
            game_board[move] = player
            count = count + 1

        else:
            print('Try another position!!')
            count = count
            continue

        if player == 'X':
            player = 'O'
        else:
            player = 'X'
#Checking for the winning player
        if count >= 5:
            if game_board['7'] == game_board['8'] == game_board['9'] == player:  # across the top
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                if player == 'X':
                    player1_score += 1
                else:
                    player2_score += 1
                break
            elif game_board['4'] == game_board['5'] == game_board['6'] == player:  # across the middle
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                if player == 'X':
                    player1_score += 1
                else:
                    player2_score += 1
                break
            elif game_board['1'] == game_board['2'] == game_board['3'] == player:  # across the bottom
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                if player == 'X':
                    player1_score += 1
                else:
                    player2_score += 1
                break
            elif game_board['1'] == game_board['4'] == game_board['7'] == player:  # down the left side
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                if player == 'X':
                    player1_score += 1
                else:
                    player2_score += 1
                break
            elif game_board['2'] == game_board['5'] == game_board['8'] == player:  # down the middle
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                if player == 'X':
                    player1_score += 1
                else:
                    player2_score += 1
                break
            elif game_board['3'] == game_board['6'] == game_board['9'] == player:  # down the right side
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                if player == 'X':
                    player1_score += 1
                else:
                    player2_score += 1
                break
            elif game_board['7'] == game_board['5'] == game_board['3'] == player:  # diagonal
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                if player == 'X':
                    player1_score += 1
                else:
                    player2_score += 1
                break
            elif game_board['1'] == game_board['5'] == game_board['9'] == player:  # diagonal
                printboard(game_board)
                print("\nGame Over.\n")
                print(message)
                if player == 'X':
                    player1_score += 1
                else:
                    player2_score += 1
                break

            else:
                continue

            # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nRound one Over😁😎.\n")
            print("It's a Tie!!")

            # we have to change the player after every move.
def GameRestart():
    game_start = []

    for key in game_board:
        game_start.append(key)

    confirm = input("Do want to play Again?(y/n)")

    if confirm == "y" or confirm == "Y":
        for key in game_start:
            game_board[key] = " "
            gameplay()
        
        
#Game Call
getPlayers()
gameplay()
GameRestart()
Report()

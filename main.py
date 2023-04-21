import numpy as np
tictac = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])
count = 0
game_on = True

def ask():
    """It will ask the user for the row and column returns the row, column with the turn
    It will inform whose turn is it and returns that turn for the function which needs for it's computation """
    global count
    if (count%2 == 0):
        print("Turn for 'X'")
        turn = 1
    else:
        print("Turn for 'O'")
        turn = 2
    count +=1
    row, column = input("Enter a row: "), input("Enter a column: ")
    return row, column, turn
def validate_move(row, column ,turn ):
    """It would validate each move the user given"""
    global count
    try:
        row = int(row)
        column = int(column)
        if(tictac[row][column] == 0):
            tictac[row][column] = turn
        else:
            count -=1
            print("It is already populated, Try again!")
    except IndexError:
        print("Error: Row and Column must be between 0-2. Try again!")
        count -=1
    except ValueError:
        print("Error: Row and Column must be between 0-2. Try again!")
        count -=1


def display(game_board=tictac):
    """Displays the gameboard provided."""
    print("    ===============================")
    for row in tictac:
        count = 0
        for c in row:
            if count <=3:
                if c == 1:
                    print("    |    X", end="")
                elif c == 0:
                    print("    |     ", end="")
                else:
                    print("    |    O", end="")
        print(end="    |")
        print()
        print("    ===============================")


def is_game_on(game_board):
    global game_on
    for row in game_board:
        if row[0] == row[1] == row[2] and row[0] != 0:
            game_on = False
            if row[0] == 1:
                print("X wins the game.")
            else:
                print("O wins the game.")
    for i in range(0, 3):
        #  cheak if it is a column win
        if game_board[0][i] == game_board[1][i] == game_board[2][i] and game_board[0][i] != 0:
            game_on = False
            if game_board[0][i] == 1:
                print("X wins the game.")
            else:
                print("O wins the game.")
        # cheak if it is a diagonal win
        if i == 0:
            if game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[1][1] != 0:
                game_on = False
                if game_board[1][1] == 1:
                    print("X wins the game.")
                else:
                    print("O wins the game.")
            #  cheak for if it is another diagonal win
            if game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[1][1] !=0:
                game_on = False
                if game_board[1][1] == 1:
                    print("X wins the game.")
                else:
                    print("O wins the game.")
    if count == 9:
        game_on = False
        print("It is a Draw!")

    return game_on


def play():

    while(is_game_on(tictac)):
        display(tictac)
        row, column, turn = ask()
        validate_move(row, column, turn)
    another_game()

def another_game():
    global count, tictac, game_on
    play_another_game = input("Play anoter Game? Y/N").lower()
    if play_another_game == 'y':
        count = 0
        game_on = True
        tictac = np.array([[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]])
        print("Here You go.\n\n")
        play()
    else:
        print("See you!")




play()







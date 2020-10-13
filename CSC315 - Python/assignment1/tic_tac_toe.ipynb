"""
Course: Python for Scientist (Part-I)
"""
#%%
def author():
    '''
    return your name
    '''
    return 'Isabelle Geller'
#%%
import random
import copy
# %%
def DrawBoard(Board):
    '''
    Parameter: Board is a 3x3 matrix (a nested list).
    Return: None
    Description: this function prints the chess board
    hint: Board[i][j] is ' ' or 'X' or 'O' in row-i and col-j
          use print function
    '''
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if (j == 0 or j==1):
                print('{}|'.format(Board[i][j]), end='')
            else:
                print(Board[i][j], end='')

        if i == 0 or i == 1:
            print('\n-+-+-')

    print('\n')

#%% 
def IsSpaceFree(Board, i ,j):
    '''
    Parameters: Board is the game board, a 3x3 matrix
                i is the row index, j is the col index
    Return: True or False
    Description: 
        (1) return True  if Board[i][j] is empty ' '
        (2) return False if Board[i][j] is not empty
        (3) return False if i or j is invalid (e.g. i = -1 or 100)
        think about the order of (1) (2) (3)
        Board[-1][100] will raise error/exception
    '''
    if (i not in range(0, 3, 1)) or (j not in range(0, 3, 1)) or (Board[i][j] != ' '):
        return False
    elif Board[i][j] == ' ':
        return True

#%%
def GetNumberOfChessPieces(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: the number of chess piceces on Board
            i.e. the total number of 'X' and 'O'
    hint: define a counter and use a nested for loop, like this
          for i in 0 to 3
              for j in 0 to 3
                  add one to the counter if Board[i][j] is not empty
    '''
    totalPieces = 0

    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if Board[i][j] != ' ':
                totalPieces += 1

    return totalPieces

#%%
def IsBoardFull(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is fully occupied
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
    if GetNumberOfChessPieces(Board) == 9:
        return True
    else:
        return False
#%%
def IsBoardEmpy(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is empty
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
    if GetNumberOfChessPieces(Board) == 0:
        return True
    else:
        return False
#%%
def UpdateBoard(Board, Tag, Choice):
    '''
    Parameters: 
        Board is the game board, a 3x3 matrix
        Tag is 'O' or 'X'
        Choice is a tuple (row, col) from HumanPlayer or ComputerPlayer
    Return: None
    Description: 
         Update the Board after a player makes a choice
         Set an element of the Board to Tag at the location (row, col)
    '''
    row = int(Choice[0])
    col = int(Choice[1])
    Board[row][col] = Tag
#%%
def HumanPlayer(Tag, Board):
    '''
    Parameters: 
        Tag is 'X' or 'O'. If Tag is 'X': HumanPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfHumanPlayer, it is a tuple (row, col)
    Description:
        This function will NOT return until it gets a valid input from the user
    Attention:
        Board is NOT modified in this function
    hint: 
        a while loop is needed, see HumanPlayer in rock-papper-scissors
        the user needs to input row-index and col-index, where a new chess will be placed
        use int() to convert string to int
        use try-except to handle exceptions if the user inputs some random string
        if (row, col) has been occupied, then ask the user to choose another spot
        if (row, col) is invalid, then ask the user to choose a valid spot
    '''
    row = None
    col = None
    print('make your choice\n')
    while True:
        if not isinstance(row, int) or row not in range(0,3):
            try:
                row = int(input("row = "))
                Board[row]
                continue
            except ValueError:
                print("Oops! That was not a valid number. Try again...")
            except IndexError:
                print("Oops! That number is out of bounds. Try again...")
        elif not isinstance(col, int) or col not in range(0, 3):
            try:
                col = int(input("col = "))
                Board[col] #does not matter if we check in col area bc its a 3x3
                continue
            except ValueError:
                print("Oops! That was not a valid number. Try again...")
            except IndexError:
                print("Oops! That number is out of bounds. Try again...")
        if not IsSpaceFree(Board, row, col):
            row = None
            col = None
            print("Oops! That space is already taken. Try again...")
        else:
            break

    print('HumanPlayer({}) has made the choice'.format(Tag))
    return (row, col)


#%%
def ComputerPlayer(Tag, Board):
    '''
    Parameters:
        Tag is 'X' or 'O'. If Tag is 'X': ComputerPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfComputerPlayer, it is a tuple (row, col)   
    Description:
        ComputerPlayer will choose an empty spot on the board
        a random strategy in a while loop:
            (1) randomly choose a spot on the Board
            (2) if the spot is empty then return the choice (row, col)
            (3) if the spot is not empty then go to (1)
    Attention:
        Board is NOT modified in this function
    '''
    row = random.randint(0, 3)
    col = random.randint(0, 3)

    while not IsSpaceFree(Board, row, col):
        row = random.randint(0, 3)
        col = random.randint(0, 3)

    print('ComputerPlayer({}) has made the choice'.format(Tag))
    return (row, col)

#%%
def Judge(Board):
    '''
    Parameter:
         Board is the current game board, a 3x3 matrix
    Return: Outcome, an integer
        Outcome is 0 if the game is still in progress
        Outcome is 1 if player X wins
        Outcome is 2 if player O wins
        Outcome is 3 if it is a tie (no winner)
    Description:
        this funtion determines the Outcome of the game
    hint:
        (1) check if anyone wins, i.e., three 'X' or 'O' in
            top row, middle row, bottom row
            lef col, middle col, right col
            two diagonals
            use a if-statment to check if three 'X'/'O' in a row
        (2) if no one wins, then check if it is a tie
            note: if the board is fully occupied, then it is a tie
        (3) otherwise, the game is still in progress
    '''
    xWin = ['X', 'X', 'X']
    oWin = ['O', 'O', 'O']

    # check rows nd cols for win
    # transpose matrix to check cols
    zipped_rows = zip(*Board)
    transpose_matrix = [list(row) for row in zipped_rows]

    for i in range(0, 3, 1):
        if Board[i] == xWin or transpose_matrix[i] ==xWin:
            return 1
        elif Board[i] == oWin or transpose_matrix[i] == oWin:
            return 2

    #check diagonal
    if ([Board[0][0], Board[1][1], Board[2][2]] == xWin) or ([Board[0][2], Board[1][1], Board[2][0]] == xWin):
        return 1
    elif ([Board[0][0], Board[1][1], Board[2][2]] == oWin) or ([Board[0][2], Board[1][1], Board[2][0]] == oWin):
        return 2

    # see if its a tie
    if (IsBoardFull(Board)):
        return 3
    else:
        return 0;

#%%
def ShowOutcome(Outcome, NameX, NameO):
    '''
    Parameters:
        Outcome is from Judge
        NameX is the name of PlayerX who goes first at the beginning
        NameO is the name of PlayerO 
    Return: None
    Description:
        print a meassage about the Outcome
        NameX/NameO may be 'human' or 'computer'
    hint: the message could be
        PlayerX (NameX, X) wins 
        PlayerO (NameO, O) wins
        the game is still in progress
        it is a tie
    '''
    outcomes = {
        0: 'the game is still in progress',
        1: 'PlayerX ({}, X) wins'.format(NameX),
        2: 'PlayerX ({}, X) wins'.format(NameO),
        3: 'it is a tie'
    }
    print(outcomes[Outcome])

#%% read but do not modify this function
def Which_Player_goes_first():
    '''
    Parameter: None
    Return: two function objects: PlayerX, PlayerO
    Description:
        Randomly choose which player goes first.
        PlayerX/PlayerO is ComputerPlayer or HumanPlayer
    '''
    if random.randint(0, 1) == 0:
        print("Computer player goes first")
        PlayerX = ComputerPlayer
        PlayerO = HumanPlayer
    else:
        print("Human player goes first")
        PlayerO = ComputerPlayer
        PlayerX = HumanPlayer
    return PlayerX, PlayerO
#%% the game
def TicTacToeGame():
    #---------------------------------------------------    
    print("Wellcome to Tic Tac Toe Game")
    Board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    DrawBoard(Board)
    # determine the order
    PlayerX, PlayerO = Which_Player_goes_first()
    # get the name of each function object
    NameX = PlayerX.__name__
    NameO = PlayerO.__name__
    #---------------------------------------------------    
    # suggested steps in a while loop:
    while True:
        # (1)  get a choice from PlayerX, e.g. ChoiceX=PlayerX('X', Board)
        choice = PlayerX('X', Board)
        # (2)  update the Board
        UpdateBoard(Board, 'X', choice)
        # (3)  draw the Board
        DrawBoard(Board)
        # (4)  get the outcome from Judge
        outcome = Judge(Board)
        # (5)  show the outcome
        ShowOutcome(outcome, NameX, NameO)
        # (6)  if the game is completed (win or tie), then break the loop
        if outcome == 1 or outcome == 2 or outcome == 3:
            break
        # (7)  get a choice from PlayerO
        choice = PlayerO('O', Board)
        # (8)  update the Board
        UpdateBoard(Board, 'O', choice)
        # (9)  draw the Board
        DrawBoard(Board)
        # (10) get the outcome from Judge
        outcome = Judge(Board)
        # (11) show the outcome
        ShowOutcome(outcome, NameX, NameO)
        # (12) if the game is completed (win or tie), then break the loop
        if outcome == 1 or outcome == 2 or outcome == 3:
            break
    #---------------------------------------------------
    # your code starts from here

#%% play the game many rounds until the user wants to quit
# read but do not modify this function
def PlayGame():
    while True:
        TicTacToeGame()
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print("GameOver")
#%% do not modify anything below
if __name__ == '__main__':
    PlayGame()

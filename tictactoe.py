
def playerCheck(row, column, diagonalElement, playerIdentification):
    decision = True
    if diagonalElement == True:
        for number in board[::(dimension+1)]:
            if number != playerIdentification:
                decision = False
                break
            else:
                pass
        if decision == True:
            return True
        else:
            decision = True

        for number in board[dimension-1:dimension**2-dimension+1:dimension-1]:
            if number != playerIdentification:
                decision = False
                break
            else:
                pass
        
        if decision == True:
            return True
        else:
            decision = True

        for number in board[column::dimension]:
            if number != playerIdentification:
                decision = False
                break
            else:
                pass
        if decision == True:
            return True
        else:
            decision = True

        for number in board[row*dimension:row*dimension+dimension:1]:
            if number != playerIdentification:
                decision = False
                break
            else:
                pass
        if decision == True:
            return True
        else:
            pass

    else:
        for number in board[column::dimension]:
            if number != playerIdentification:
                decision = False
                break
            else:
                pass
        if decision == True:
            return True
        else:
            decision = True
        
        for number in board[row*dimension:row*dimension+dimension:1]:
            if number != playerIdentification:
                decision = False
                break
            else:
                pass
        if decision == True:
            return True
        else:
            pass
    
    return decision

def playerUpdate(player1Input, playerIdentification):
    decision = False
    digonalElement = False
    board[player1Input] = playerIdentification
    row = int(player1Input/dimension)
    column = player1Input % dimension
    if (row + column == (dimension-1)) or row == column:
        digonalElement = True
    else:
        pass

    decision = playerCheck(row, column, digonalElement, playerIdentification)
    return decision

def makeBoard(dimension):
    i = 0
    while i < dimension ** 2:
        board.append(0)
        i = i + 1

def displayBoard():
    i = 0
    while i < dimension**2:
        print(board[i:i+dimension:1])
        i = i + dimension

def askInput(playerIdentification):
    validInput = False
    generalInput = -1
    while(validInput == False):
        generalInput = input()
        generalInput = int(generalInput)
        if(generalInput < 0 or generalInput > (dimension**2 - 1) or board[generalInput]!= 0):
            print(f"Player {playerIdentification} your input is invalid. It is out of bound or the place has already been taken. Please try new input from 0 - {dimension**2 - 1}")
        else:
            validInput = True

    return generalInput

dimension = input("Player 1 and Player 2, discuss and choose the dimension of board y'all would like to play tic tac toe on:")
dimension = int(dimension)
board = []
decision = False
totalMoves = 0
makeBoard(dimension)
print("Your board looks like this:\n")
displayBoard()

while totalMoves < dimension**2:
    print('Player 1 where would you like to place your input?:')
    player1Input = askInput(1)
    decision = playerUpdate(player1Input, 1)
    totalMoves += 1
    if(decision == True):
        print("Game is over. Player 1 won the game\n")
        displayBoard()
        break
    else:
        print("The current state of the game is:")
        displayBoard()
        print('\n')
    
    print('Player 2 where would you like to place your input?:')
    player2Input = askInput(2)
    decision = playerUpdate(player2Input, 2)
    totalMoves += 1
    if(decision == True):
        print("Game is over. Player 2 won the game\n")
        displayBoard()
        break
    else:
        print("The current state of the game is:")
        displayBoard()
        print('\n')
else:
    print("We're out of moves. This game is a draw.\n")





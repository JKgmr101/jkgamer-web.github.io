import random

print("TIC TAC TOES")
print("You are X's and opponent is O's")
print(" _ _ _ ")
board = [["_","_","_"],["_","_","_"],["_","_","_"]]
counter = 0

def printboard():
    global board
    for row in range(0,3):
        print( "|" +str(board[row][0]) + "|" + str(board[row][1]) + "|" + str(board[row][2]) + "|")
        
printboard()

def didSomeoneWin():
    if board[0][0] == board[1][1] == board[2][2] == "X":
        print("You Win!")
        return True
    if board[2][0] == board[1][1] == board[0][2] == "X":
        print("You Win!")
        return True
    for i in range(0,3):
        if board[0][i] == board[1][i] == board[2][i] == "X":
            print("You Win!")
            return True
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2] == "X":
            print("You Win!")
            return True
    return False


def didSomeoneWinforOpponent():
    if board[0][0] == board[1][1] == board[2][2] == "O":
        print("Oppont Wins!")
        return True
    if board[2][0] == board[1][1] == board[0][2] == "O":
        print("Opponent Wins!")
        return True
    for j in range(0,3):
        if board[0][j] == board[1][j] == board[2][j] == "O":
            print("Opponent Wins!")
            return True
    for j in range(0,3):
        if board[j][0] == board[j][1] == board[j][2] == "O":
            print("Opponent Wins!")
            return True
        
    return False

def isBoardFull():
    for i in range(0,3):
        for j in range(0,3):
            if board[j][i] == "_":
                return
    if (didSomeoneWin() == False) or (didSomeoneWinforOpponent == False):
        print("Tie")

def whichRowOrColumn():
    while didSomeoneWin() == False and didSomeoneWinforOpponent() == False:
        chosenRow = int(input("Put the row")) - 1
        chosenColumn = int(input("Put the Column")) - 1
        if (chosenRow == 0 or chosenRow == 1 or chosenRow == 2) and (chosenColumn == 0 or chosenColumn == 1 or chosenColumn == 2):
            if board[chosenRow][chosenColumn] != "_":
                print("Restart please")
                continue
            else:
                board[chosenRow][chosenColumn] = "X"
                didSomeoneWin()
                isBoardFull()  
        else:
            print("Choose a number between 1, 2, 3")
            continue

        

        while True:
            chosenRowforOpponent = random.randint(0,2)
            chosenColumnforOpponent = random.randint(0,2)
            if board[chosenRowforOpponent][chosenColumnforOpponent] == "_":
                board[chosenRowforOpponent][chosenColumnforOpponent] = "O"
                didSomeoneWinforOpponent
                isBoardFull()   
                printboard()
                break


whichRowOrColumn()

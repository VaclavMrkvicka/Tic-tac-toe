"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Václav Mrkvička
email: vasek.mrkvicka@gmail.com
discord: spectra111
"""
line = "-" * 40
doubleLine =  "=" * 40

print(f"""Welcome to Tic Tac Toe
========================================
GAME RULES:
Hello players!
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game""")
print(line)
board = ["_", "_", "_",
        "_", "_", "_",
        "_", "_", "_"]# hraci deska / playing board

currentPlayer = "X"
winner = None
gameRunning = True

# Vypsání hrací desky / printing board
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])


#hráčův input/ players input
def playerInput(board):
    global currentPlayer
    print(doubleLine) 
    inp = int(input(f"""Player {currentPlayer} choose a number from 1 to 9:"""))
    if inp >= 1 and inp <= 9 and board[inp-1] == "_":
        board[inp - 1] = currentPlayer
        playerChange() 
    else: 
        print(doubleLine) 
        print("PLAYER ALREADY TOOK A FIELD OR INVALID INPUT!")
        print(doubleLine) 

 


#kontrola Vyhry v řádků / check win in Row
def checkRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True

#kontrola Vyhry v sloupci / check win in column
def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True

#kontrola Vyhry uhlopříčky / check win Diagonal
def checkDianogal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True

#kontrola remízi / checking Tie
def checkTie(board):
    global gameRunning
    if "_" not in board and winner is None:
        print("TIE")
        gameRunning = False


def playerChange(): #zmena hráče / player change
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def checkWin(): #kontrola výhry/ win check
    global gameRunning
    if checkDianogal(board) or checkRow(board) or checkColumn(board):
        print(f"Congratulations! The winner is player {winner}")
        gameRunning = False

while gameRunning:
    playerInput(board)
    print_board(board)
    checkWin()
    checkTie(board)

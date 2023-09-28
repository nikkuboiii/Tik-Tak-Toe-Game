import random

board = ["-" for _ in range(9)]
currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board):
    while True:
        inp = int(input("Enter a number 1-9: "))
        if 1 <= inp <= 9 and board[inp - 1] == "-":
            board[inp - 1] = currentPlayer
            break
        else:
            print("Invalid input. Try again.")

def checkWin(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "-":
            return board[combo[0]]

    if "-" not in board:
        return "Tie"

    return None

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            break

while gameRunning:
    printBoard(board)
    playerInput(board)
    winner = checkWin(board)
    
    if winner:
        if winner == "Tie":
            print("It's a tie!")
        else:
            print(f"The winner is {winner}!")
        break

    switchPlayer()
    
    printBoard(board)
    computer(board)
    winner = checkWin(board)

    if winner:
        if winner == "Tie":
            print("It's a tie!")
        else:
            print(f"The winner is {winner}!")
        break

    switchPlayer()

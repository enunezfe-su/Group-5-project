import numpy
import random

print("Lets play BattleShip!!")
playerTurn = 0
while playerTurn < 5:
    board = [["0"] * 5 for i in range(5)]
    i = random.randint(0,5)
    j = random.randint(0,5)
    board[i][j] = "1"
    for x in board:
        print(x)

    userY = int(input("enter your y cordinate: "))
    userX = int(input("enter your X cordinate: "))
    playerTurn += 1
    board[userY][userX] = "x"
    if board[userY][userX] == board[i][j]:
        print("HIT!!")
    else:
        print("MISS")




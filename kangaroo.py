board = [["0"] * 5 for i in range(5)]
#Beginning
flowerRow = 0
flowerColum = 1

kangarooRow = 0
kangarooColum = 0
board[flowerRow][flowerColum] = "#"
board[kangarooRow][kangarooColum] = "K"
print("LETS PLAY PLUCK AND PLANT!!")
for i in board:
    print(i)

#initializing
flowerRow = 0
flowerColum = 0

flowerRow = int(input("enter your row cordinate for flower(0-4): "))
flowerColum = int(input("enter your colum cordinatecfor flower(0-4): "))
board[flowerRow][flowerColum] = "#"
print("INITIALIZING")
for i in board:
    print(i)

#plant flower
kangarooColum = 0
kangarooRow = 0

if flowerColum >= 5 or flowerRow >= 5:
    print("not able to put flower there")


if flowerColum == 4:
    kangarooRow = flowerRow
    kangarooColum = flowerColum - 1
    board[kangarooRow][kangarooColum] = "K"

else:
    kangarooColum = flowerColum+1
    kangarooRow = flowerRow
    board[kangarooRow][kangarooColum] = "K"
print("PLANTING FLOWER")
for i in board:
    print(i)


from random import randint 

#Game's life
print("Welcome to the Game's Life !")

x = int(input ("Choose a number : "))
y = x

board = [[randint(0, 1) for k in range(x)] for i in range(y)]

def afficher(tab) :
    print("\n_______\n")
    for i in range(len(tab)):
        print(tab[i])
    print("_______\n")
    print("Press [space] to continue...")

afficher(board)

def cell(x, y, tab) :
    return tab[y][x]

#itere chaque case du board5
    #donc itere sur chaque colonne du board
    #puis sur chaque colonne, itere sur chaque ligne

copyBoard = board
for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i])
        weight = 0
        if board[i-1][j-1] == 1:
            weight += 1
        print("alive ? ", weight)

        if weight > 3:
            board[i][j] = 0

board = copyBoard
for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i])
        weight = 0
        if board[i-1][j-1] == 1:
            weight += 1
        print("alive ? ", weight)

        if weight > 3:
            board[i][j] = 0

#pour chaque cases je vérifie chaque cases voisines (au dessus, au dessous et côtés)




#Rules
#Any live cell with fewer than two live neighbours dies, as if by underpopulation :

#Any live cell with two or three live neighbours lives on to the next generation :

#Any live cell with more than three live neighbours dies, as if by overpopulation  :

#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction :
# [0, 1, 0]
# [0, 0, 1]
# [0, 1, 1]

# espace

# [0, 1, 0]
# [0, 1, 1]
# [0, 1, 1]

# [0, 1, 0]
# alive ? 0



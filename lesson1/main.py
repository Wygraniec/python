# XXX OI
# Zadanie wąż (KOL)
# https://sio2.mimuw.edu.pl/c/oi30-1/p/kol/

def printBoard(arr: list[:int]):
    print()
    for row in arr:
        print(row)
    print()


def move(direction: str):
    global snakeLength
    prevPos: list[:int] = [pos[0], pos[1]]
    # changing position according to direction
    if direction == "L":
        pos[0] -= 1
    elif direction == "P":
        pos[0] += 1
    elif direction == "G":
        pos[1] -= 1
    elif direction == "D":
        pos[1] += 1

    # if the next field is not equal to -1 then there is a treat to be collected
    # therefore no move is necessary (increase of length is enough)
    if board[pos[0]][pos[1]] != -1:
        snakeLength += 1
        return

    # movement of each "block" of the snake
    
    return


m: int = int(input())  # size of board
p: int = int(input())  # amount of snacks
n: int = int(input())  # amount of queries to handle

snakeLength: int = 1  # length of a snake (amount of blocks to move)
pos = [0, 0]  # current position of snake's head

board: list[:int] = []

# Generation of a 2D list (board)
for i in range(m):
    board.append([])
    for j in range(m):
        board[i].append(-1)

board[0][0] = 0  # Snake always starts on (0, 0) position

# Putting snack on their places on the board
for i in range(p):
    (w, k, c) = (int(input()), int(input()), int(input()))
    board[w - 1][k - 1] = c

# Creating snake behaviour (moves and colour queries)
for i in range(n):
    query: str = input()[0]

    # Query for printing snake colour at a given location
    if query == "Z":
        (x, y) = (int(input()), int(input()))
        print(board[x - 1][y - 1])
        continue

    # if query does not start wit 'Z' then it has to be a move instruction
    move(query)
    printBoard(board)  # printing board after every move for game visualization

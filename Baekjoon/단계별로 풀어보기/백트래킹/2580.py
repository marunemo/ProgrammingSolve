from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

def validCheck(puzzle, x, y, currentNumber):
    for i in range(0, 9):
        if puzzle[y][i] == currentNumber and i != x:
            return False
    for i in range(0, 9):
        if puzzle[i][x] == currentNumber and i != y:
            return False
    indexX = (x // 3) * 3
    indexY = (y // 3) * 3

    for i in range(3):
        for j in range(3):
            if puzzle[i + indexY][j + indexX] == currentNumber:
                if i + indexY != y and j + indexX != x:
                    return False
    return True
    

def sudoku(puzzle, x = 0, y = 0):
    if x == 0 and y == 9:
        return True
    
    isComplete = False
    if puzzle[y][x] == 0:
        for i in range(1, 10):
            if validCheck(puzzle, x, y, i):
                puzzle[y][x] = i
                if x == 8:
                    isComplete = sudoku(puzzle, 0, y + 1)
                else:
                    isComplete = sudoku(puzzle, x + 1, y)
        if not isComplete:
            puzzle[y][x] = 0
    else:
        if x == 8:
            isComplete = sudoku(puzzle, 0, y + 1)
        else:
            isComplete = sudoku(puzzle, x + 1, y)

    return isComplete

puzzle = []
for _ in range(9):
    puzzle.append(list(map(int, stdin.readline().split())))

isComplete = sudoku(puzzle)

if isComplete:
    for i in puzzle:
        print(*i)
else:
    print("Not Found!")
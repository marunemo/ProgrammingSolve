from sys import stdin

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
        return
    
    if puzzle[y][x] == 0:
        for i in range(1, 10):
            if validCheck(puzzle, x, y, i):
                puzzle[y][x] = i
                if x == 8:
                    sudoku(puzzle, 0, y + 1)
                else:
                    sudoku(puzzle, x + 1, y)
    else:
        if x == 8:
            sudoku(puzzle, 0, y + 1)
        else:
            sudoku(puzzle, x + 1, y)

puzzle = []
for _ in range(9):
    puzzle.append(list(map(int, stdin.readline().split())))

sudoku(puzzle)

for i in puzzle:
    print(*i)
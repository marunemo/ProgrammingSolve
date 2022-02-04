import sys
sys.setrecursionlimit(10000)

def w(a, b, c):
    global memo

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 각 a, b, c에 따른 결과를 메모이제이션
    if memo[a][b][c] == 0:
        if a < b and b < c:
            memo[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            memo[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    return memo[a][b][c]

# memo = [[[0] * 21] * 21] * 21는 주소 복사(shallow copy)가 발생하므로, 부적절한 사용
memo = [[([0] * 21) for _ in range(21)] for _ in range(21)]

# -1 -1 -1이 나오기 전까지 입력받음
inputList = []
while True:
    abc = list(map(int, sys.stdin.readline().split()))
    if abc == [-1, -1, -1]:
        break
    inputList.append(abc)

# 포맷에 맞게 각 결과 출력
for a, b, c in inputList:
    print("w({0}, {1}, {2}) = {3}".format(a, b, c, w(a, b, c)))
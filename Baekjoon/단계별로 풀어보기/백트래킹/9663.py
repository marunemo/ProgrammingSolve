'''
풀이

퀸이 서로 공격할 수 없도록 하기 위해서는 세가지 조건을 만족해야 한다.
1. 각 퀸이 같은 행에 존재하지 않아야 한다.
2. 각 퀸이 같은 열에 존재하지 않아야 한다.
3. 각 퀸이 대각선으로 만날 수 없어야 한다.

1.과 2.의 조건을 모두 만족하는 방식은 dfs로 구현할 수 있다.
여기에 3.의 조건을 만족하는 지 확인하기 위해 자신과 같은 대각선에 퀸이 존재하는 지를 탐색하면 된다.
각 행열에 각각 -1을 계속하여 만약 퀸이 존재하면 백트래킹하고, 그렇지 않으면 계속 탐색한다.
이후 n개의 퀸의 위치가 모두 확정되면 총 개수에 포함한다.
'''

# 퀸의 개수 세는 함수 생성
def queenCount(isQueenThere, queenLocation, column, n):
    # 마지막으로 배치한 퀸이 대각선으로 다른 퀸과 공격할 수 있을 경우, 그 경우는 제외한다.(조건 3.)
    # 마지막으로 배치한 퀸의 열
    lastColumn = column - 1
    # 마지막으로 배치한 퀸의 위치
    lastRow = queenLocation[lastColumn]
    # 각 대각선의 경우에 대한 존재 가능 여부
    for c in range(lastColumn - 1, -1, -1):
        # y = ±(x - lastColumn) + lastRow의 식을 만족하는 경우, 대각선으로 공격 가능하다.
        # 이때, 각 식은 |y - lastRow| = |x - lastColumn|으로 나타낼 수 있고,
        # x < lastColumn에 대해 |y - lastRow| = lastColumn - x로 나타낼 수 있으므로, 식은 다음과 같다.
        if abs(queenLocation[c] - lastRow) == lastColumn - c:
            return 0
    
    # 만약 위 3.의 조건을 만족하는 퀸들이 n개를 만족할 경우 총 개수에 1을 추가한다.
    if column == n:
        return 1

    # 총 개수 탐색
    totalQueenCount = 0
    
    # 다른 퀸이 존재하지 않는 행을 탐색한다.(조건 2.)
    for i in range(n):
        if not isQueenThere[i]:
            # 퀸이 존재하지 않을 경우 그 열에 퀸을 배치하고, 다음 열에 퀸을 배치한다.(조건 1.)
            queenLocation[column] = i
            isQueenThere[i] = True
            totalQueenCount += queenCount(isQueenThere, queenLocation, column + 1, n)
            isQueenThere[i] = False
    return totalQueenCount

# n*n의 체스판에서 놓을 퀸 n개의 개수
n = int(input())
# 각 행에 퀸이 존재하는 지에 대한 여부
isQueenThere = [False] * n
# 각 열에 따른 퀸의 위치
queenLocation = [0] * n
# 현재 열
column = 0

totalQueenCount = queenCount(isQueenThere, queenLocation, column, n)
print(totalQueenCount)
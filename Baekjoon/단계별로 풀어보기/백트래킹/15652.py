# dfs 함수 생성
def dfs(orderedList, order, n, m):
    if order == m:
        print(*orderedList)
        return
    # 이전 숫자부터 n까지 출력
    for i in range(orderedList[order - 1], n + 1):
        orderedList[order] = i
        dfs(orderedList, order + 1, n, m)

# 입력값 초기화
n, m = map(int, input().split())
orderedList = [1] * m
order = 0

# dfs로 수열 탐색
dfs(orderedList, order, n, m)
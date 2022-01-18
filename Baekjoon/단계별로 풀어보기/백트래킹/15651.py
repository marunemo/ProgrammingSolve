# dfs 함수 생성
def dfs(orderedList, order, n, m):
    if order == m:
        print(*orderedList)
    else:
        # 중복 포함 각 순서에 [1, n] 범위의 값 삽입
        for i in range(n):
            orderedList[order] = i + 1
            dfs(orderedList, order + 1, n, m)

n, m = map(int, input().split())
orderedList = [0] * m
order = 0

dfs(orderedList, order, n, m)
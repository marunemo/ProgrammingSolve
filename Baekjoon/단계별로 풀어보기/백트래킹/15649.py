# dfs 함수 생성
def dfs(n, m, orderedSet, order, isVisited):
    # depth bound 확인 및 백트래킹
    if order == m:
        print(*orderedSet)
        return
    # 각 인덱스에 숫자 확인
    for i in range(1, n + 1):
        # 무한 루프 방지를 위한 방문 여부 확인
        if not isVisited[i]:
            isVisited[i] = True
            orderedSet[order] = i
            dfs(n, m, orderedSet, order + 1, isVisited)
            isVisited[i] = False

# 입력 값 및 초기 데이터 구조 생성
n, m = map(int, input().split())
orderedSet = [0 for _ in range(m)]
isVisited = {i : False for i in range(1, n + 1)}

# 함수 실행 및 결과 출력
dfs(n, m, orderedSet, 0, isVisited)
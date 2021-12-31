# dfs 함수 생성
def dfs(n, m, orderedSet, order):
    # depth bound 확인 및 백트래킹
    if order == m:
        print(*orderedSet)
        return
    # depth bound보다 작은 수에서 최댓값 도달 시 무시
    if orderedSet[order - 1] >= n:
        return
    # 각 인덱스에 숫자 삽입
    for i in range(orderedSet[order - 1] + 1, n + 1):
        orderedSet[order] = i
        dfs(n, m, orderedSet, order + 1)

# 입력 값 및 초기 데이터 구조 생성
n, m = map(int, input().split())
orderedSet = [0 for _ in range(m)]

# 함수 실행 및 결과 출력
dfs(n, m, orderedSet, 0)
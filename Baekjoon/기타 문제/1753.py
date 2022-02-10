'''
풀이

전형적인 다익스트라 알고리즘 문제이다.

adjacency matrix가 주어졌을 때, 그래프 내에서 갈 수 있는 최단 거리를 구하는 문제이다. 
'''

# fast IO
from sys import stdin
input = stdin.readline

# min heap 구현 모듈
import heapq

# 정점과 간선 입력
vertice, edge = map(int, input().split())

# 시작 정점 위치 입력
k = int(input())

# adjacency matrix 생성 (인덱스의 위치를 맞추기 위해 0번 빈 인덱스 추가)
adjMatrix = [{} for _ in range(vertice + 1)]

# adjacency matrix에 간선 추가
for _ in range(edge):
    u, v, w = map(int, input().split())
    if v not in adjMatrix[u] or adjMatrix[u][v] > w:
        adjMatrix[u][v] = w

# 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력
for i in range(1, vertice + 1):
    # weight 0과 첫 시작 정점인 k로 초기화
    minPath = [[0, k]]

    # 현재 위치 초기화 (인덱스가 0인 정점은 존재하지 않음)
    u = 0

    # 현재 위치가 목표 위치에 도달했거나 더이상 이동할 수 없을 때까지 반복
    while u != i and minPath:
        # 가중치와 현재 위치 불러오기
        weight, u = heapq.heappop(minPath)

        # 현재 위치에서의 간선에 대한 도착 정점과 가중치 저장
        for v, w in adjMatrix[u].items():
            if v not in adjMatrix[k] or adjMatrix[k][v] > weight + w:
                adjMatrix[k][v] = weight + w
            heapq.heappush(minPath, [weight + w, v])
    
    # 만약 더이상 이동할 수 없었다면 경로가 존재하지 않는 것으로 간주
    if not minPath:
        print("INF")
    # 그렇지 않으면 최단 경로 출력
    else:
        print(weight)
'''
풀이

전형적인 다익스트라 알고리즘 문제이다.

adjacency matrix가 주어졌을 때, 그래프 내에서 갈 수 있는 최단 거리를 구하는 문제이다.

(1차 수정)
결국 모든 정점에서 구할 필요 없이 하나의 정점에서 갈 수 있는 모든 경우를 구하면 되므로,
각 정점으로 가는 방법을 각각의 경우에 대해서 구하는 것이 아닌 한 번에 모든 정점으로의 가중치를 구하는 방법이 가장 효율적이다.

(2차 수정)
결국 한 정점으로 갔던 거리가 이전 거리와 비교하여 최단 거리가 아니라면,
새로 추가하더라도 최단 거리가 될 수 없으므로 결과를 무시하는 것이 효율성을 크게 높히는 데에 도움이 된다.
(예외적으로 가중치가 음의 값을 가지는 경우라면 무시할 수 없다(그 경우라면 다익스트라 알고리즘 자체를 써서는 안된다))
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

# 1부터 vertice까지의 모든 최단 경로 저장
minPath = ["INF" for _ in range(vertice + 1)]

# 시작점 자신은 0으로 초기화
minPath[k] = 0
    
# weight 0과 첫 시작 정점인 k로 초기화
daikstra = [[0, k]]

# 더이상 경로를 탐색할 수 없을 때까지 반복
while daikstra:
    # 가중치와 현재 위치 불러오기
    weight, u = heapq.heappop(daikstra)

    # 현재 위치에서의 간선에 대한 도착 정점과 가중치 저장
    for v, w in adjMatrix[u].items():
        if minPath[v] == "INF" or minPath[v] > weight + w:
            minPath[v] = weight + w
            heapq.heappush(daikstra, [weight + w, v])

# 각 최단 경로나 발견되지 않은 경로 출력
for weight in minPath[1:]:
    print(weight)
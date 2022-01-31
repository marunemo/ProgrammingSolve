'''
풀이

조건은 매우 간단하다.
자신이 이전 단계에서 선택했던 색과 다른 색을 선택하여 나타날 수 있는 최솟값을 구하면 된다.

이때, 그리디 알고리즘을 통해 생각해본다면, 현재 고를 수 있는 색들 중 나타날 수 있는 최솟값을 구하면 된다.
예로 들어, 이번 색에서 초록색을 골랐다면 빨강과 파랑 중 최솟값을 가지는 색을 선택하면 된다는 것이다.
그리고 해당 최솟값을 가지고 있는 색을 골랐을 때의 누적값을 현재 선택한 색의 값에 추가하고, 해당 값을 다음 값으로 인계한다.
그 후, 마지막에 각 빨강, 초록, 파랑을 골랐을 때의 값들을 비교하여 최솟값을 출력한다.
'''

from sys import stdin
input = stdin.readline

lines = int(input())

r, g, b = 0, 0, 0
for _ in range(lines):
    color = list(map(int, input().split()))
    r, g, b = color[0] + (g if g < b else b), color[1] + (r if r < b else b), color[2] + (r if r < g else g)
print(min(r, g, b))
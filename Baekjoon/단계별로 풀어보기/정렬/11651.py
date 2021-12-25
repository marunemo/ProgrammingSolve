from sys import stdin

# 좌표 개수와 각 좌표 입력
cases = int(input())
coordinate = []
for _ in range(cases):
    coordinate.append(list(map(int, stdin.readline().split())))

# 두 번째 인덱스(y좌표)를 기준으로 오름차순 정렬
coordinate.sort(key=lambda x: (x[1], x[0]))

# 결과 출력
for x,y in coordinate:
    print(x, y)
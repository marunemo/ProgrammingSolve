testcase = int(input())
count = []
for _ in range(testcase):
    x, y = map(int, input().split())
    distance = y - x
    totalCount = 0
    level = 1
    levelCount = distance

    # 한 번에 갈 수 있는 거리를 최대까지 설정
    # 최대로 간 뒤에는 다시 돌아와야 하므로, 좌우 대칭으로 설정
    while level * 2 <= distance:
        distance -= level * 2
        totalCount += 2
        level += 1
    
    # 마지막에 level에 +1이 되어 결론적으로 최대로 이동 가능했던 거리의 +1부터 계산
    # 나머지 distance를 (최대 이동 거리 + 1) 이하의 거리 여러번으로 나타내기
    # 같은 거리가 여러번 나올 수 있으므로 while문 안에 while문 설정
    while distance > 0:
        while distance >= level:
            distance -= level
            totalCount += 1
        level -= 1
    count.append(totalCount)
print(*count, sep='\n')
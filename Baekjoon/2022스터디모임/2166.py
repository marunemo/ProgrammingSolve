# fast IO
from sys import stdin
input = stdin.readline

pointCount = int(input())
pointList = [list(map(int, input().split())) for _ in range(pointCount)]
pointList.sort()

totalSize = 0

a, b, c = pointList[:3]
for i in range(3, pointCount + 1):
    if a[1] > c[1]:
        highPoint = a
        lowPoint = c
    else:
        highPoint = c
        lowPoint = a
    if b[1] >= highPoint[1]:
        partSize = abs((c[0] - a[0]) * (b[1] - lowPoint[1]))

        partSize -= abs((c[0] - a[0]) * (c[1] - a[1])) / 2
        partSize -= abs((b[0] - a[0]) * (b[1] - a[1])) / 2
        partSize -= abs((c[0] - b[0]) * (c[1] - b[1])) / 2
    elif b[1] <= lowPoint[1]:
        partSize = abs((c[0] - a[0]) * (highPoint[1] - b[1]))

        partSize -= abs((c[0] - a[0]) * (c[1] - a[1])) / 2
        partSize -= abs((b[0] - a[0]) * (b[1] - a[1])) / 2
        partSize -= abs((c[0] - b[0]) * (c[1] - b[1])) / 2
    else:
        partSize = abs((c[0] - a[0]) * (highPoint[1] - lowPoint[1]))

        partSize -= abs((c[0] - a[0]) * (c[1] - a[1])) / 2

        partSize -= abs((highPoint[0] - b[0]) * (b[1] - lowPoint[1]))
        partSize -= abs((highPoint[0] - b[0]) * (highPoint[1] - b[1])) / 2
        partSize -= abs((b[0] - lowPoint[0]) * (b[1] - lowPoint[1])) / 2
    
    totalSize += partSize
    if i != pointCount:
        a, b, c = b, c, pointList[i]

print("%.1f" % totalSize)
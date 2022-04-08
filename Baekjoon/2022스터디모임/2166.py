'''
참고

https://www.mathopenref.com/coordpolygonarea2.html
https://darkpgmr.tistory.com/86
'''

# fast IO
from sys import stdin
input = stdin.readline

pointCount = int(input())
pointList = [list(map(int, input().split())) for _ in range(pointCount)]

# 신발끈 정리
totalSize = 0
for i in range(pointCount):
    totalSize += pointList[i][0] * pointList[(i + 1) % pointCount][1]
    totalSize -= pointList[(i + 1) % pointCount][0] * pointList[i][1]
totalSize /= 2

print("%.1f" % abs(totalSize))
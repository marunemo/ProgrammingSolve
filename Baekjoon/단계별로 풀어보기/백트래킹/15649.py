from collections import Counter

# 자연수 n, m 입력
n,m = map(int, input().split())

# 수열 저장
orderedSet = [1 for _ in range(m)]

# 수열 인덱스
end = m - 1
index = 0
isEnd = False

while True:
    onlyOne = True
    orderedSet[end] += 1
    for i in range(m):
        if orderedSet[end - i] == n + 1:
            if i == m - 1:
                isEnd = True
                break
            orderedSet[end - i - 1] += 1
            orderedSet[end - i] = 1
    if isEnd:
        break
    counter = Counter(orderedSet).most_common()
    for i,c in counter:
        if c != 1:
            onlyOne = False
            break
    if onlyOne:
        print(*orderedSet)
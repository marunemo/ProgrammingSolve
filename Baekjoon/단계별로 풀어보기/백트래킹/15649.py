from collections import Counter

# 자연수 n, m 입력
n,m = map(int, input().split())

# 수열 저장
orderedSet = [1 for _ in range(m)]

# 수열 마지막 인덱스
end = m - 1

# 수열을 계속 찾을 지 확인
isFinding = True

while isFinding:
    # 중복 확인
    onlyOne = True
    counter = Counter(orderedSet).most_common()
    for i,c in counter:
        if c != 1:
            onlyOne = False
            break
    if onlyOne:
        print(*orderedSet)
    
    # 마지막 인덱스에 1을 추가
    orderedSet[end] += 1
    for i in range(m):
        # 현재 숫자가 최대를 넘어선 경우
        if orderedSet[end - i] == n + 1:
            # 가장 왼쪽 숫자가 최대를 넘어서면 종료
            if i == m - 1:
                isFinding = False
                break
            # 그 외에는 자신 왼쪽 숫자를 1 늘리고, 자신은 1로 초기화
            orderedSet[end - i - 1] += 1
            orderedSet[end - i] = 1
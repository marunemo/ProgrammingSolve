from sys import stdin

# 개수 입력
_ = int(input())

# 각 좌표의 값을 순서를 고려하여 저장하는 리스트 생성
coordinate = list(map(int, stdin.readline().split()))

# 각 좌표의 중복값을 제거한 set 생성
compressed = set(coordinate)

# 순서대로 정렬
compressed = sorted(list(compressed))

# 각 좌표보다 작은 값의 개수에 대한 메모이제이션
compressed = {c : i for i, c in enumerate(compressed)}

# 각 좌표 압축 (X_i)
zipX = [compressed[i] for i in coordinate]

# 결과 출력
print(*zipX)
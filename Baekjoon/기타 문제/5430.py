'''
풀이

R은 배열을 reverse하는 것이고, D는 리스트에 대하여 dequeue를 하는 것이다.
이때, 배열이 비었을 때, D가 나타나면 에러가 발생한다.

이 문제를 풀 때, 가장 큰 문제는 함수의 개수나 배열의 개수가 모두 최대 100,000개나 된다는 것이다.
게다가 그 시행 횟수가 최대 100회까지 될 수 있다.
따라서 R과 D 함수를 리스트에 일일이 직접 적용하는 것에는 무리가 있다.

그렇기에, 먼저 앞에서 지울 개수와 뒤에서 지울 개수를 구한다.
그리고 해당 배열이 뒤집어졌는지를 판별하고, 지워진 개수만큼을 슬라이스하여 출력한다.
이때, D의 개수가 현재 배열의 길이보다 많아지면 즉시 에러를 출력하면 된다.
'''

# fastIO
from sys import stdin
input = stdin.readline

# 테스트 케이스 입력
testcase = int(input())

# 함수를 수행한 결과를 저장할 리스트
resultList = []

# 테스트 케이스에 대해 함수를 실행
for _ in range(testcase):
    # 함수와 배열의 수를 입력
    func = input()
    arrCount = int(input())

    # 배열을 [x1,...,xn]과 같은 형태로 입력받으므로, 배열의 형태에 맞게 수정
    arr = input()[1:-2].split(",")
    if arr == [""]:
        arr = []
    else:
        arr = list(map(int, arr))

    # 앞뒤에 삭제되는 개수와 역전 여부 확인
    dequeue = 0
    pop = 0
    isReversed = False

    # 함수를 차례대로 실행
    for f in func:
        if f == "R":
            isReversed = not isReversed
        elif f == "D":
            if isReversed:
                pop += 1
            else:
                dequeue += 1

        # 만약 배열의 총 길이보다 D의 개수가 더 많으면 즉시 종료
        if dequeue + pop > arrCount:
            break

    # 배열의 총 길이보다 D의 개수가 더 많으면 에러 출력
    if dequeue + pop > arrCount:
        resultList.append("error")
    # 그렇지 않다면, 앞뒤로 배열을 슬라이싱하여 역전
    else:
        arr = arr[dequeue:arrCount - pop]
        resultList.append(arr[::(-1 if isReversed else 1)])

# 결과 차례로 출력
for result in resultList:
    print(result)
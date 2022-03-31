'''
풀이

스택에 대하여 push와 pop을 통해 임의의 수열을 만들 수 있는 지 판별하고, 가능하다면 그 push와 pop의 연산 순서를 출력하는 문제이다.
python에는 리스트에 내장 메서드로 append와 pop가 존재하므로, [-1]를 통해 마지막 인덱스를 확인하면 된다.
이 방법을 사용하게 된다면, 현재까지 push된 최댓값을 저장하여 마지막 인덱스보다 주어진 수열의 원소가 크다면, 최댓값의 1 큰 수 씩 append하면 된다.
마지막 인덱스가 더 작을 경우에는 pop을 하되, 만약 pop으로 얻어진 원소가 현재 인덱스의 원소와 다르다면 불가능으로 간주해버리면 된다.
그러나 당연히 리스트에 직접 추가 및 삭제하는 방법은 오버헤드가 발생하므로, 100,000개의 숫자를 처리하는 데에는 무리가 있다.
(실제로는 안해봐서 모르지만, 가능하더라도 다른 방법을 찾아보기로 했다)

그래서 다른 방법으로 우선 불가능이 나타나는 경우를 정리해보기로 했다.
push에서는 불가능한 경우가 나타나지 않는다. 스택의 top보다 큰 수가 나타나면 그만큼 push를 해주면 되기 때문이다.
하지만 pop의 경우 1씩 줄어들면서 그 값을 출력하므로, 출력이 pop에 의존되는 이상 두 칸을 건너뛰는 것은 불가능해진다.
즉, 마지막 인덱스가 현재 출력해야 하는 인덱스의 값보다 차가 1보다 큰 값으로 작아지게 된다면, 임의의 수열대로의 출력이 불가능해진다는 것이다.

이 점을 고려하여 리스트에 입력 및 삭제되는 방식을 구현해본다면 다음과 같다.

(1차 수정)
시간초과가 발생하여 코드의 수정이 필요해졌다.
생각해보면 방문되지 않은 최소 인덱스는 항상 (push된 인덱스 중 최댓값 + 1)를 push한 것과 같아진다는 것을 알게 되었다.
방문되지 않은 최소 인덱스를 찾아가는 경우는 pop을 하다보니 결국 0의 인덱스에 도달하는 경우인데, 이는 즉 현재 스택에 데이터가 없다는 것이다.
그렇다면 0에 도달했지만 0과 push된 인덱스 중 최댓값 사이에 데이터가 있는 경우는 없는가에 대한 문제가 발생한다.
하지만 pop을 통해 0에 도달하기 전에 데이터가 있다면, 무조건 불가능 혹은 pop이 이루어질 수 밖에 없다.
결론적으로 0의 인덱스가 도달하는 경우는 push된 인덱스 중 최댓값부터 0까지 데이터 없는 경우 밖에 없는 것이다.
'''

# fast IO
from sys import stdin
input = stdin.readline

# 수열에 넣을 수를 결정
numCount = int(input())

# 길이가 numCount인 임의의 수열 입력
randomSeq = [int(input()) for _ in range(numCount)]

# pop 여부를 확인할 데이터 세트와 스택의 top을 표시할 변수 생성
seqVisited = {(i + 1) : False for i in range(numCount)}
top = 1

# push되었던 최댓값 저장
maxTop = 1

# 최종적으로 출력될 연산 생성(무조건 1을 거치므로, +로 시작)
operationSeq = "+"

# 임의의 수열을 첫 원소부터 찾아가며, 불가능 여부 탐색 및 연산 순서 저장
flag = False
lastIndex = randomSeq[-1]
for seqIndex in randomSeq:
    if top < seqIndex:
        # 목표 인덱스와 같아질 때까지 push하는 것으로 간주(연산 추가)
        while top < seqIndex:
            if not seqVisited[top]:
                operationSeq += "+"
            top += 1
        
        # 최대 인덱스 갱신
        if top > maxTop:
            maxTop = top
    else:
        # 만약 스택의 top이 현재 출력해야할 원소와 다르다면, 불가능으로 간주
        if top != seqIndex:
            flag = True
            break

    # 현재 인덱스와 같을 경우, 방문되지 않은 최소 인덱스로 이동 및 연산 추가(pop)
    seqVisited[top] = True
    operationSeq += "-"
    while top > 0 and seqVisited[top]:
        top -= 1
    if top == 0 and seqIndex != lastIndex:
        maxTop += 1
        top = maxTop
        operationSeq += "+"

# 불가능 여부 및 연산 순서 출력
if flag:
    print("NO")
else:
    for oper in operationSeq:
        print(oper)
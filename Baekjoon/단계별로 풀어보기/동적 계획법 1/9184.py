'''
풀이

다음과 같은 재귀함수 w(a, b, c)가 있다.
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

이를 해석하면
1. a, b, c 중 하나 이상 0 또는 음수가 있다면 1을 반환한다.
2. a, b, c 중 하나 이상 20 이상의 수가 있다면 전부 20으로 초기화한다.
3. a, b, c가 오름차순이라면, w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)을 실행한다.
4. 그 외의 경우, w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)을 실행한다.
로 나타낼 수 있다.

이로써 유추할 수 있는 것은 결국 값을 결정하는 것은 1.의 값 1이므로, a, b, c 중 하나 이상이 0 또는 음수가 되는 경우들만 고려하면 된다.

여기서 알 수 있는 내용들을 나열해본다.
- b >= c 인 경우, 
'''
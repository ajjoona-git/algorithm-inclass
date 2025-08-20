# 5097. 회전

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 수열(list)을 deque 형태로 변환
    arr_deque = deque(arr)
    # deque의 rotate 메서드 활용
    # 왼쪽으로 M칸 만큼 회전한다.
    arr_deque.rotate(-M)

    print(f'#{tc} {arr_deque[0]}')
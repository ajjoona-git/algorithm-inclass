# 0000. delta 연습문제

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 배열의 크기는 NxN
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 4방향 델타 배열 (상하좌우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 절대값의 누적합
    result = 0

    # 현재 위치를 이동
    for r in range(N):
        for c in range(N):
            # 인접한 4방향 탐색
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                # 배열의 범위를 넘어가는 경우 계산하지 않는다.
                if nr < 0 or N <= nr or nc < 0 or N <= nc:
                    continue

                # 현재 요소와 인접한 요소의 차이만큼 누적합
                diff = arr[nr][nc] - arr[r][c]
                # 두 값의 차이가 음수일 경우 -1을 곱해 절대값을 구한다.
                if diff < 0:
                    diff *= (-1)
                result += diff

    print(f'#{test_case} {result}')
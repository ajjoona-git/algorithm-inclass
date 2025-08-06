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

                # 인접한 4방향에 대한 벽 체크
                if 0 <= nr < N and 0 <= nc < N:
                #     # 현재 요소와 인접한 요소의 차이만큼 누적합
                    result += abs(arr[nr][nc] - arr[r][c])

    print(f'#{test_case} {result}')
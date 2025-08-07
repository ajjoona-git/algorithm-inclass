# 12712: 파리퇴치3

import sys
sys.stdin = open("in1.txt")

T = int(input())

def kill_flies_plus(arr, r, c, M):
    """+ 형태로 분사될 때의 파리 수를 반환하는 함수"""
    flies_cnt = arr[r][c]
    # 인접한 요소 탐색을 위한 델타 배열 (상하좌우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for step in range(1, M):
        for i in range(4):
            nr = r + dr[i] * step
            nc = c + dc[i] * step
            # 벽 체크
            if 0 <= nr < N and 0 <= nc < N:
                flies_cnt += arr[nr][nc]

    return flies_cnt


def kill_flies_x(arr, r, c, M):
    """x 형태로 분사될 때의 파리 수를 반환하는 함수"""
    flies_cnt = arr[r][c]
    # 인접한 요소 탐색을 위한 델타 배열 (좌상-우상-좌하-우하)
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]

    for step in range(1, M):
        for i in range(4):
            nr = r + dr[i] * step
            nc = c + dc[i] * step
            # 벽 체크
            if 0 <= nr < N and 0 <= nc < N:
                flies_cnt += arr[nr][nc]

    return flies_cnt


for tc in range(1, T+1):
    N, M = map(int, input().split())  # 배열의 크기 N, 스프레이의 세기 M
    flies = [list(map(int, input().split())) for _ in range(N)]

    # 현재 위치 초기화 (0, 0)
    r, c = 0, 0
    max_flies = 0  # 최대 파리수

    # 현재 위치를 이동
    for r in range(N):
        for c in range(N):
            # 인접한 요소를 탐색하면서 파리의 수 합산
            plus_cnt = kill_flies_plus(flies, r, c, M)
            x_cnt = kill_flies_x(flies, r, c, M)
            # 최대 파리수 갱신
            max_flies = max(max_flies, plus_cnt, x_cnt)

    print(f'#{tc} {max_flies}')
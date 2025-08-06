# 1210. Ladder1

import sys
sys.stdin = open("input.txt")

T = 10  # 테스트 케이스의 수

for _ in range(T):
    test_case = int(input())
    N = 100  # 배열의 크기는 100x100
    arr = [list(input().split()) for _ in range(N)]

    # 도착부터 탐색을 시작할건데,
    # 도착은 100번째 행의 값 중 '2'를 찾아야 한다.
    r = N - 1
    c = arr[r].index('2')

    # 경로 탐색을 위한 델타 배열 (좌-우-상)
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    # 첫 번째 행에 도달할 때까지 경로를 탐색한다.
    while r > 0:
        # 인접한 요소 탐색 (좌우상)
        for i in range(3):
            nr = r + dr[i]
            nc = c + dc[i]

            # 벽 체크를 만족하면서 값이 '1'일 때만 이동할 수 있다.
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '1':
                r, c = nr, nc
                # 방문한 곳은 다시 방문하지 않기 위해 값은 '0'으로 바꾼다.
                arr[r][c] = '0'
                break

    # 알고 싶은 값은 r = 0 일 때의 c 값
    print(f'#{test_case} {c}')
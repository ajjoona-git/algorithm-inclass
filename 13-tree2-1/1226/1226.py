# 1226. 미로1

from collections import deque


def bfs(sr, sc):
    visited = [[False] * N for _ in range(N)]
    q = deque()

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited[sr][sc] = True
    q.append((sr, sc))

    while q:
        r, c = q.popleft()

        # 4방향 인접노드 탐색
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 1. 경계 체크 2. 방문 체크
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                # 도착('3')
                if grid[nr][nc] == '3':
                    return 1
                # 통로('0')
                if grid[nr][nc] == '0':
                    visited[nr][nc] = True
                    q.append((nr, nc))

    return 0


def find_start_point():
    # 출발('2') 찾기
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '2':
                return i, j


T = 10
for _ in range(1, T + 1):
    tc = int(input())
    N = 16
    grid = [input() for _ in range(N)]

    sr, sc = find_start_point()

    print(f'#{tc} {bfs(sr, sc)}')

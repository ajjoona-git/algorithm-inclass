# 5105. 미로의 거리

from collections import deque


def bfs(sr, sc):
    visited = [[-1] * N for _ in range(N)]
    q = deque()

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited[sr][sc] = 0
    q.append((sr, sc))

    while q:
        r, c = q.popleft()

        # 4방향 인접노드 탐색
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 1. 경계 체크 2. 방문 체크
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                # 도착('3')
                if grid[nr][nc] == '3':
                    return visited[r][c]
                # 통로('0')
                if grid[nr][nc] == '0':
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

    return 0


def find_start_point():
    # 출발('2') 찾기
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '2':
                return i, j


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [input() for _ in range(N)]

    sr, sc = find_start_point()

    print(f'#{tc} {bfs(sr, sc)}')

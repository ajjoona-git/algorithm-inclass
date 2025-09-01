# 연습문제. 도로 이동 시간

from collections import deque

# 인접한 4방향 탐색을 위한 델타 (상하좌우 순)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(i, j):
    """(i, j)부터 시작해서 연결된 땅을 bFS 방식으로 모두 방문 처리하는 함수"""
    q = deque()
    visited[i][j] = 1
    q.append((i, j))

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 1) 벽 체크, 2) 방문 체크, 3) 도로('1') 체크
            if (
                0 <= nr < N and 0 <= nc < M
                and not visited[nr][nc]
                and grid[nr][nc] == '1'
            ):
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))


N, M = map(int, input().split())
# NxM 크기의 격자 정보: 도로면 '1', 장애물이면 '0'
grid = [input().strip() for _ in range(N)]
visited = [[0] * M for _ in range(N)]

bfs(0,0)
print(visited[N-1][M-1] - 1)
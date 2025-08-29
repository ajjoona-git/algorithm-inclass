# 연습문제. 섬 찾기


# 인접한 8방향 탐색을 위한 델타 (12시부터 시계 방향 순)
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(r, c):
    """(r, c)부터 시작해서 연결된 땅을 DFS 방식으로 모두 방문 처리하는 함수"""
    visited[r][c] = True
    
    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]
        # 1) 벽 체크, 2) 방문 체크, 3) 땅('1') 체크
        if (
            0 <= nr < N and 0 <= nc < M
            and not visited[nr][nc]
            and grid[nr][nc] == '1'
        ):
            dfs(nr, nc)


N, M = map(int, input().split())
# NxM 크기의 격자 정보: 땅이면 '1', 물이면 '0'
grid = [input().strip() for _ in range(N)]

island_count = 0
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        # 방문하지 않은 땅이면 섬 발견!
        if grid[i][j] == '1' and not visited[i][j]:
            # 섬의 개수 +1
            island_count += 1
            # 연결된 땅 모두 방문 처리
            dfs(i, j)

print(island_count)
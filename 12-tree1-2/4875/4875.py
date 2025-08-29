# 4875. 미로 


def find_start():
    """출발지('2')의 좌표를 반환하는 함수"""
    for r in range(N):
        for c in range(N):
            if grid[r][c] == '2':
                return r, c
        
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c):
    """(r, c)에서 시작해서 DFS로 탐색한다. 도착지를 찾으면 1을, 길이 없다면 0을 반환한다."""
    global result
    visited[r][c] = True

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        # 벽 체크, 방문 체크
        if (
            0 <= nr < N and 0 <= nc < N
            and not visited[nr][nc]
        ):
            # 도착('3')인 경우, 1을 반환하고, 탐색을 종료한다.
            if grid[nr][nc] == '3':
                result = 1
                return
            
            # 통로('0')인 경우, 탐색을 계속한다.
            elif grid[nr][nc] == '0':
                dfs(nr, nc)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # '0'(통로), '1'(벽), '2'(출발), '3'(도착)
    grid = [input() for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    # 출발지 찾기
    start_r, start_c = find_start()

    # 도착지 찾기
    result = 0
    dfs(start_r, start_c)

    print(f'#{tc} {result}')
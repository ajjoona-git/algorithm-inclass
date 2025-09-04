# 5188. 최소합

# 오른쪽, 아래
dr = [0, 1]
dc = [1, 0]

def calculate(r, c, total):
    global result

    # 종료조건
    if (r, c) == (N-1, N-1):
        result = min(result, total)
        return

    # 가지치기
    if total >= result:
        return

    # 오른쪽 또는 아래로 이동
    if r < N and c + 1 < N and not visited[r][c+1]:
        visited[r][c+1] = True
        calculate(r, c+1, total + grid[r][c+1])
        visited[r][c+1] = False

    if r + 1 < N and c < N and not visited[r+1][c]:
        visited[r+1][c] = True
        calculate(r+1, c, total + grid[r+1][c])
        visited[r+1][c] = False



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    result = float('inf')
    calculate(0, 0, grid[0][0])

    print(f'#{tc} {result}')

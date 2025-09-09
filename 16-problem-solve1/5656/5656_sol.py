# 5656. 벽돌깨기

"""
구슬 N번 - 맨 위에 있는 벽돌만 깨트릴 수 있다.
-> 모든 위치에서 시도한다. N번 반복 (백트래킹)
    1 <= N <= 4
    2 <= W <= 12
    2 <= H <= 15

구슬이 명중한 벽돌은 상하좌우로 (벽돌에 적힌 숫자 -1)칸만큼 같이 제거. 연쇄작용.
-> BFS

1. 완전탐색
    - 모든 경우의 수 12 ^ 4 = 약 25만 번
    - 백트래킹
        - 한번 쏘았을 때 벽돌들이 연쇄적으로 깨진다.
        - 현재 기준으로 퍼져나가면서 탐색(BFS)
        - 빈칸 메우기

2. 최소 벽돌: 현재 벽돌이 다 깨지면 더 이상 할 필요 없다.
    -> 현재 벽돌 수를 관리
"""

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def shoot(cnt, remains, copy_arr):
    global min_blocks
    # 종료 조건: N개의 구슬을 모두 발사하거나 남은 벽돌이 0이면
    if cnt == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return
    
    # 모든 열에 한 줄씩 떨구자
    for col in range(W):
        # 백트래킹: 기존 벽돌들의 상태 저장
        # 방법1. 원본을 복사해두고, 다시 되돌리는 방법
        # 1. col 위치에 떨구기 전 상태를 복사 (얕은 복자 주의)
        # 2. 원본 리스트의 col 위치에 떨구고
        # 3. cnt + 1 번 재귀 상태로 이동
        # 4. 떨구기 전 상태로 복구

        # 방법2. 복구 시간이 없는 방식
        # 1. col 위치에 떨구기 전 상태를 복사
        # 2. 복사한 리스트의 col 위치에 떨군다.
        # 3. cnt + 1 번 상태로 이동할 때, copy_arr 을 함께 전달
        copy_arr = [row[:] for row in arr]

        row = -1
        # 가장 위 벽돌을 검색
        for r in range(H):
            if copy_arr[r][col]:  # 벽돌이 있으면
                row = r
                break
        
        # 벽돌이 없는 열은 pass
        if row == -1:
            continue

        # 해당 row, col의 숫자부터 시작해서 BFS
        # 행, 열, 숫자를 모두 담아야 한다.
        q = deque([(row, col, copy_arr[row][col])])
        now_remains = remains - 1

        copy_arr[row][col] = 0  # 구슬이 처음 만나는 벽돌 자리

        # 주변 벽돌들을 순차적으로 파괴
        while q:
            r, c, p = q.popleft()
            # 상하좌우의 p칸을 모두 제거
            for k in range(1, p):
                for i in range(4):
                    nr = r + dr[i] * k
                    nc = c + dc[i] * k

                    # 범위 밖이면 pass
                    if nr < 0 or nr >= H or nc <0 or nc >= W:
                        continue

                    # 벽돌이 없으면 pass
                    if copy_arr[nr][nc] == 0:
                        continue

                    q.append((nr, nc, copy_arr[nr][nc]))
                    copy_arr[nr][nc] = 0
                    now_remains -= 1

        # 빈칸 메우기
        for c in range(W):
            idx = H - 1  # 벽돌이 위치할 index
            for r in range(H - 1, -1, -1):
                if copy_arr[r][c]:
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1

        shoot(cnt + 1, now_remains, copy_arr)

    

T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]

    min_blocks = 1e9  # 최소 벽돌 수
    # 남은 벽돌 수
    blocks = 0  
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1

    shoot(0, blocks, arr)
    print(f'#{tc} {min_blocks}')
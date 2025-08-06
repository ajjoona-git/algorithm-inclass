# 9490. 풍선팡

# import sys
# sys.stdin = open('input1.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 인접한 요소 탐색을 위한 델타 배열 (상하좌우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 꽃가루 합의 최대값
    max_flowers = 0

    # 2차원 배열에서 현재 위치를 이동
    for r in range(N):
        for c in range(M):
            flowers = arr[r][c]  # 매 위치에서 계산할 꽃가루의 합 초기화
            # 종이 꽃가루 개수(k)만큼 탐색 거리를 지정한다.
            for k in range(1, arr[r][c]+1):
                # 인접한 요소 탐색 (상하좌우)
                for i in range(4):
                    nr = r + dr[i] * k
                    nc = c + dc[i] * k

                    # 벽 체크 후 꽃가루의 합 계산
                    if 0 <= nr < N and 0 <= nc < M:
                        flowers += arr[nr][nc]

                # 최대값 갱신
                if flowers > max_flowers:
                    max_flowers = flowers

    print(f'#{test_case} {max_flowers}')
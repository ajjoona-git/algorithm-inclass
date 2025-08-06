# 1954. 달팽이 숫자

import sys
sys.stdin = open("input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    # 달팽이 모양으로 이동하기 위한 델타 배열 (우하좌상)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r = 0
    c = 0
    number = 1
    snail[r][c] = number  # 첫 번째 숫자초기화
    
    # N*N 개의 숫자를 할당했다면 종료
    while number < N * N:
        # 이동할 방향을 설정하고 (우하좌상)
        for i in range(4):
            # 몇 번 이동할 지 설정 (최대 N번)
            for _ in range(N):
                nr = r + dr[i]
                nc = c + dc[i]
    
                # 배열의 범위 이내이면서 이동한 위치의 값이 0일때만 값을 할당한다.
                if 0 <= nr < N and 0 <= nc < N and snail[nr][nc] == 0:
                    number += 1
                    r, c = nr, nc  # 현재 위치 갱신
                    snail[r][c] = number
                else:
                    break
    
    # 결과 출력
    print(f'#{test_case}')
    for r in range(N):
        for c in range(N):
            print(snail[r][c], end=' ')
        print()
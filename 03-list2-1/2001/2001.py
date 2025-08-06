# 2001. 파리 퇴치

# import sys
# sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    # 파리의 개수를 담은 NxN 배열
    flies = [list(map(int, input().split())) for _ in range(N)]
    max_flies = 0  # 파리의 합 최대값 초기화

    # 현재 위치 (0,0)으로 초기화
    r = c = 0

    # 현재 위치를 이동하면서
    for r in range(N):
        for c in range(N):
            # MxM 크기의 부분 배열의 합을 구한다.
            num_of_flies = 0  # 파리의 합 초기화
            for i in range(M):
                for j in range(M):
                    nr = r + i
                    nc = c + j
                    # 경계 체크
                    if 0 <= nr < N and 0 <= nc < N:
                        num_of_flies += flies[nr][nc]
            # 파리의 합 최대값 갱신
            max_flies = max(max_flies, num_of_flies)

    print(f'#{test_case} {max_flies}')
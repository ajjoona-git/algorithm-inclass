# 1209. Sum

import sys
sys.stdin = open("input.txt")

T = 10  # 테스트 케이스의 수

for test_case in range(1, T+1):
    _ = input()  # 입력받은 테스트 케이스의 번호는 test_case로 대체

    # 100x100 크기의 배열 생성
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 각 행의 합, 각 열의 합, 각 대각선의 합 중에서 최대값
    max_sum = 0

    # 행 연산
    for r in range(N):
        row_sum = 0  # 각 행의 합 초기화
        for c in range(N):
            row_sum += arr[r][c]
        # 최대값 갱신
        if row_sum > max_sum:
            max_sum = row_sum

    # 열 연산
    for c in range(N):
        col_sum = 0  # 각 열의 합 초기화
        for r in range(N):
            col_sum += arr[r][c]
        # 최대값 갱신
        if col_sum > max_sum:
            max_sum = col_sum

    # 대각선 연산(\)
    diagonal_sum = 0
    for i in range(N):
        diagonal_sum += arr[i][i]
        if diagonal_sum > max_sum:
            max_sum = diagonal_sum

    # 대각선 연산(/)
    diagonal_sum = 0
    for i in range(N):
        diagonal_sum += arr[i][N-1 - i]
        if diagonal_sum > max_sum:
            max_sum = diagonal_sum

    print(f'#{test_case} {max_sum}')
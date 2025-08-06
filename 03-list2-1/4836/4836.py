# 4836. 색칠하기

# import sys
# sys.stdin = open("sample_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 칠할 영영의 수

    # 색깔 정보를 저장할 2차원 배열(격자)
    # 0: 빈 칸, 1: 빨강, 2: 파랑, 3: 보라
    colors = [[0] * 10 for _ in range(10)]

    # 색깔 영역 정보(N개)를 받아와 2차원 배열에 적용한다.
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                colors[r][c] += color

    result = 0  # 보라색 칸의 수

    # 보라색이 된 칸(3)의 수를 계산한다.
    for r in range(10):
        for c in range(10):
            if colors[r][c] == 3:
                result += 1

    print(f'#{test_case} {result}')
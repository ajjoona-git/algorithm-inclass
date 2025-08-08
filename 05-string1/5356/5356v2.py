# 5356. 의석이의 세로로 말해요

# import sys
# sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트 케이스의 수

for tc in range(1, T+1):
    letters = [input() for _ in range(5)]
    result = ""

    # 열 우선 탐색
    for c in range(15):
        for r in range(5):
            try:
                result += letters[r][c]
            except IndexError:  # 값이 없는 경우 지나간다.
                continue

    print(f"#{tc} {result}")
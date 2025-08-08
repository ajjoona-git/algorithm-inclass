# 5356. 의석이의 세로로 말해요

# import sys
# sys.stdin = open("sample_input.txt")

from itertools import zip_longest

T = int(input())  # 테스트 케이스의 수

for tc in range(1, T+1):
    letters = [input() for _ in range(5)]
    result = ""

    # zip() 함수 이용하되, 빈 값을 빈 문자열('')로 처리해야 하므로
    # itertools 모듈의 zip_longest 함수를 사용함
    for letter in zip_longest(*letters, fillvalue=''):
        for char in letter:  # letter 예시: ('A', 'a', '0', 'F', 'f')
            result += char

    print(f"#{tc} {result}")
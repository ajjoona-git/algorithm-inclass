# 연습문제. 문자열 뒤집기

import sys
sys.stdin = open("input.txt")

T = int(input())  # 테스트 케이스의 수


for tc in range(1, T+1):
    s = input()  # 문자열 입력받기
    reversed_s = ""

    for char in s:
        reversed_s = char + reversed_s

    print(f"#{tc} {reversed_s}")
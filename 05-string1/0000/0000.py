# 연습문제. 문자열 뒤집기

import sys
sys.stdin = open("input.txt")

T = int(input())  # 테스트 케이스의 수

def reverse_str(s):
    """입력받은 문자열(s)을 역방향으로 순회하면서 뒤집어진 문자열을 반환하는 함수"""
    # 1. 빈 문자열에 마지막 글자를 하나씩 추가
    reversed_s = []
    for i in range(len(s)):
        reversed_s.append(s[-1-i])

    # 2. 리스트를 문자열 형태로 변환
    reversed_s = "".join(reversed_s)

    return reversed_s


for tc in range(1, T+1):
    s = input()  # 문자열 입력받기
    print(f'#{tc} {reverse_str(s)}')
# 연습문제. 문자열 뒤집기

import sys
sys.stdin = open("input.txt")

T = int(input())  # 테스트 케이스의 수

def reverse_str(s):
    """입력받은 문자열(s)의 인덱스를 이용한 swap으로 뒤집어진 문자열 반환"""
    # 1. 리스트 형태로 변환
    s = list(s)

    # 2. 문자열의 길이의 반만큼 swap을 반복한다.
    for i in range(len(s)//2):
        s[i], s[-1-i] = s[-1-i], s[i]

    # 3. 리스트를 문자열 형태로 변환
    reversed_s = "".join(s)

    return reversed_s


for tc in range(1, T+1):
    s = input()  # 문자열 입력받기
    print(f'#{tc} {reverse_str(s)}')
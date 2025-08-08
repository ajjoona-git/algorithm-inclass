# 연습문제. integer to ascii

import sys
sys.stdin = open("input.txt")

def itoa(integer_value):
    """주어진 정수(integer_value)를 문자열로 반환하는 함수"""
    # 0 예외 처리
    if integer_value == 0:
        return '0'

    # 음수면 양수로 바꿔서 처리
    is_negative = (integer_value < 0)
    if is_negative:
        integer_value = -integer_value

    # 문자열 생성
    string_value = ""

    while integer_value > 0:
        # 10으로 나눈 나머지, 즉 일의 자리 수부터 문자열에 추가
        ones_place = integer_value % 10
        # chr()은 아스키 코드 값을 문자로 변환해주는 함수, 정수 0은 ascii 48
        string_value = chr(ones_place + 48) + string_value
        integer_value //= 10

    # 음수면 '-' 추가
    if is_negative:
        string_value = '-' + string_value

    return string_value

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T+1):
    value = int(input())
    result = itoa(value)
    print(f"#{tc} {result} {type(result)}")
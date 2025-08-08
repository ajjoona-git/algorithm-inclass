# 5432. 쇠막대기 자르기

import sys
sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트 케이스의 수

for tc in range(1, T+1):
    info = input()  # 레이저와 쇠막대기의 배치 정보(str)
    stick = []  # 쇠막대기의 정보를 저장할 리스트
    result = 0  # 조각의 수

    for i in range(len(info)):
        # 1. '('이면 일단 stick에 저장
        if info[i] == '(':
            stick.append(i)
        # 2. ')'이면 가장 최근에 저장한 (의 인덱스 확인
        else:
            # 2-1. stick의 마지막 값이 직전 인덱스라면 레이저
            if stick.pop() == (i - 1):
                # 현재 stick에 있는 쇠막대기 수만큼 추가
                result += len(stick)
            # 2-2. 아니라면 stick의 마지막 값이 현재 쇠막대기의 끝점
            else:
                result += 1

    print(f'#{tc} {result}')
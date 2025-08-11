# 연습 문제. Baby Gin

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 0~9 사이의 숫자카드 6장
    cards = [int(i) for i in input()]

    # 카운트 배열 생성(0~9 + run 검사를 위한 2개의 여분)
    count = [0] * 12
    for card in cards:
        count[card] += 1

    triplet = 0
    run = 0
    idx = 0

    # 카운트 배열을 순회하면서 triplet, run 검사
    # 검사를 continue로 끝냄으로써 각 검사를 한 번 더 수행하도록 함
    while idx < 10:
        # 1. triplet 검사
        if count[idx] >= 3:
            count[idx] -= 3
            triplet += 1
            continue

        # 2. run 검사
        if count[idx] >= 1 and count[idx+1] >= 1 and count[idx+2] >= 1:
            count[idx] -= 1
            count[idx+1] -= 1
            count[idx+2] -= 1
            run += 1  
            continue
        
        idx += 1

    # 3. baby-gin 검사
    if triplet + run == 2:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')
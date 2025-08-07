# 연습문제. subset

import sys
sys.stdin = open("input.txt")

def has_zero_subset(arr):
    """
    10개의 정수로 구성된 리스트(arr)에서 
    합이 0이 되는 부분집합이 존재하는지 확인하는 함수
    - 반환값
        0: 존재하지 않음. 1: 존재함.
    """
    n = len(arr)
    # 모든 부분집합(2^n개)을 확인한다.
    # 이때 공집합은 제외한다.
    for i in range(1, 1 << n):
        # 각 부분집합의 합을 계산할 변수
        sub_sum = 0

        # j번째 인덱스의 값에 대하여
        for j in range(n):
            # 이진수 i의 j번째 값이 1인지 확인한다.
            # 1이면 True, 값을 포함한다.
            if i & (1 << j):
                sub_sum += arr[j]

        # 부분집합의 합이 0이면 탐색을 종료
        if sub_sum == 0:
            return 1
        
    # 합이 0이 되는 부분집합이 없다면 0을 반환
    return 0

T = int(input())

for test_case in range(1, T+1):
    # 10개의 정수를 입력받아 리스트로 저장한다.
    arr = list(map(int, input().split()))  
    print(f"#{test_case} {has_zero_subset(arr)}")

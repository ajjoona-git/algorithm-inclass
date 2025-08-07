# 4837. 부분집합의 합

# import sys
# sys.stdin = open("sample_input.txt")

A = tuple(range(1, 13))  # 1부터 12까지의 숫자를 원소로 가지는 집합
T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    # 부분 집합 원소의 수 N, 부분 집합의 합 K
    N, K = map(int, input().split())
    count = 0  # 부분 집합의 수

    # N개의 원소를 택한 경우부터 탐색하기 위해 min_i, max_i를 설정 (=> 실행시간 1700ms)
    min_i = 2 ** N - 1
    max_i = min_i << (12 - N)
    for i in range(min_i, max_i + 1):
        sum_of_subset = 0  # 부분집합 원소의 합
        len_of_subset = 0  # 부분집합 원소의 개수
        for j in range(i):
            if i & (1 << j):
                sum_of_subset += A[j]
                len_of_subset += 1
            # 탐색 건너뛰기: N개 초과한 요소를 포함하거나, 합이 K보다 클 경우
            if len_of_subset > N or sum_of_subset > K:
                break
        # 부분집합의 원소가 N개이고 합이 K이면, count +1
        if len_of_subset == N and sum_of_subset == K:
            count += 1

    print(f'#{test_case} {count}')

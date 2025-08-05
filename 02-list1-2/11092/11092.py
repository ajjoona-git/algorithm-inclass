# 11092. 최대 최소의 간격

# import sys
# sys.stdin = open("sample_input.txt")

T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    N = int(input())  # 양의 정수의 수
    arr = list(map(int, input().split()))  # 양의 정수 리스트

    # 최대값의 위치와 최소값의 위치
    min_idx = 0
    max_idx = 0

    # 배열을 순회하면서 최대값과 최소값의 위치를 갱신한다.
    # 이때 최소는 가장 먼저 나오는 위치, 최대는 마지막으로 나오는 위치로 한다.
    for i in range(1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] <= arr[i]:
            max_idx = i

    # 결과를 절대값으로 출력한다.
    print(f'#{test_case} {abs(max_idx - min_idx)}')
# Gravity

# import sys
# sys.stdin = open("input.txt")

T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    N = int(input())  # 방의 가로길이
    boxes = list(map(int, input().split()))  # 상자의 개수

    drop = [0] * N  # 각 상자의 낙차를 저장할 리스트

    # boxes를 순회하면서
    for i in range(N):
        count = 0
        # 오른쪽 상자의 개수 중 현재 개수보다 작은 열의 길이를 센다.
        for j in range(i+1, N):
            if boxes[j] < boxes[i]:
                count += 1
        # 낙차량을 리스트에 저장한다.
        drop[i] = count

    max_drop = drop[0]  # 최대 낙차량
    # 그중 최대값을 찾는다.
    for i in range(1, N):
        if drop[i] > max_drop:
            max_drop = drop[i]

    # 결과를 출력한다.
    print(f'#{test_case} {max_drop}')
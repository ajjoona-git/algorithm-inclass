# 9386. 연속한 1의 개수

# import sys
# sys.stdin = open("input1.txt")

T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    N = int(input())  # 수열의 길이
    binary = input()  # 0과 1로 구성된 수열
    count = 0  # 연속된 1의 개수
    max_count = 0  # 연속된 1의 개수 중 최대값

    # 수열을 순회하면서 연속된 1의 개수를 카운트한다.
    for i in binary:
        if i == '1':
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0

    # 연속된 1로 수열이 끝나는 경우
    if count > max_count:
        max_count = count

    # 결과를 출력한다.
    print(f'#{test_case} {max_count}')
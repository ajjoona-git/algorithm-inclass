# 1945. 간단한 소인수분해

# import sys
# sys.stdin = open("input.txt")

T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    N = int(input())
    exp = [0] * 5  # 2, 3, 5, 7, 11의 지수를 담을 리스트

    # 2, 3, 5, 7, 11의 곱으로 소인수분해
    while N > 1:
        if N % 11 == 0:
            exp[4] += 1
            N //= 11
        elif N % 7 == 0:
            exp[3] += 1
            N //= 7
        elif N % 5 == 0:
            exp[2] += 1
            N //= 5
        elif N % 3 == 0:
            exp[1] += 1
            N //= 3
        else:
            exp[0] += 1
            N //= 2

    # 결과를 출력한다.
    print(f'#{test_case}', end=' ')
    for i in range(5):
        print(exp[i], end=' ')
    print()


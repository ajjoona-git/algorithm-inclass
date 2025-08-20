# 1225. 암호생성기

T = 10
for _ in range(T):
    tc = int(input())
    passcode = list(map(int, input().split()))

    i = 0

    while 0 not in passcode:
        # 1부터 5까지 반복한다.
        i += 1 
        if i > 5:
            i = 1

        # 첫 번째 숫자를 pop
        number = passcode.pop(0)
        # i만큼 감소한 뒤
        number -= i
        if number < 0:
            number = 0
        # 뒤로 이동한다.
        passcode.append(number)

    print(f'#{tc}', *passcode)

        
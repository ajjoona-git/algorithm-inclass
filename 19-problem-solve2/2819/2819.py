# 1861. 정사각형 방



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    input_list = list(map(int, input().split()))

    min_charge = N


    print(f'#{tc} {min_charge}')

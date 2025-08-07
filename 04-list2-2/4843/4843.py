# 4843: 특별한 정렬

# 선택정렬로

# import sys
# sys.stdin = open("sample_input (1).txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 확정할 위치의 인덱스를 지정: 10개까지 출력
    for i in range(10):
        # 짝수번째는 내림차순
        if i % 2 == 0:
            # 가장 큰 값을 골라서 i번째에 할당한다.
            max_idx = i
            for j in range(i + 1, N):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        
        # 홀수번째는 오름차순
        else:
            # 가장 작은 값을 골라서 i번째에 할당한다.
            min_idx = i
            for j in range(i + 1, N):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(f"#{tc}", end=" ")
    print(*arr[:10])
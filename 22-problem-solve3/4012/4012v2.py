# 4012. 요리사


def calculate_synergy(items):
    """주어진 식재료 리스트에서 식재료 조합에 따른 시너지의 합을 계산한다."""
    total = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            total += arr[items[i]][items[j]] + arr[items[j]][items[i]]
    return total


def get_taste():
    """A음식과 B음식의 맛의 차이를 계산한다."""
    A_items, B_items = [], []
    for i in range(N):
        if food[i] == 1:
            A_items.append(i)
        else:
            B_items.append(i)

    diff = abs(calculate_synergy(A_items) - calculate_synergy(B_items))
    return diff


def pick_items(count, idx):
    """N개의 재료 중에서 N//2개의 식재료를 뽑아 A음식, 나머지는 B음식의 재료로 분배한다.
        food 리스트에 A음식이면 1, B음식이면 0으로 표시한다.
        맛의 차이의 최소값을 갱신한다."""
    global min_diff

    if count == N // 2:
        diff = get_taste()
        min_diff = min(min_diff, diff)
        return
    
    for next_idx in range(idx + 1, N):
        if food[next_idx] == 1:
            continue

        food[next_idx] = 1
        pick_items(count + 1, next_idx)
        food[next_idx] = 0



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # arr: 시너지 S_ij의 값
    arr = [list(map(int, input().split())) for _ in range(N)]

    # food: 재료별 음식의 종류
    food = [0] * N
    min_diff = float('inf')
    pick_items(0, 0)

    print(f'#{tc} {min_diff}')
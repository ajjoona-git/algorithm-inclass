# 0000. Baby Gin

import itertools


def is_triplet(arr):
    """3개의 숫자로 구성된 리스트(arr)를 입력받고, 모두 같은 숫자면 True"""
    return arr[0] == arr[1] == arr[2]


def is_run(arr):
    """3개의 숫자로 구성된 리스트(arr)를 입력받고, 연속된 번호라면 True"""
    for i in range(2):
        if arr[i+1] != arr[i] + 1:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    cards = list(int(i) for i in input())
    result = 0

    # 주어진 6장의 카드로 만들 수 있는 모든 경우의 수(순열)
    for card_set in itertools.permutations(cards, 6):
        if (
            (is_triplet(card_set[:3]) or is_run(card_set[:3]))
            and (is_triplet(card_set[3:]) or is_run(card_set[3:]))
        ):
            result = 1
            break
    
    print(f'#{tc} {result}')
            
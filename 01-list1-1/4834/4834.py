# 1. dict의 key를 카드의 숫자로, value를 카운트로.

# import sys
# sys.stdin = open('sample_input.txt')


T = int(input())  # 테스트 케이스의 수

# 테스트 케이스의 수만큼 아래 연산을 반복한다.
for tc in range(1, T+1):
    N = int(input())  # 카드 장수
    # 입력받은 문자열을 for문으로 요소 하나씩 받아서
    # 정수형(int)으로 변환한 후, 리스트를 생성한다.
    cards = [ int(card) for card in input() ]

    # 카드 숫자와 장 수를 저장할 딕셔너리를 생성한다.
    count_cards = {}

    # cards를 순회하면서
    for card in cards:
        # card가 count_cards 딕셔너리에 없다면, value = 0으로 초기화한다.
        count_cards.setdefault(card, 0)
        # 그리고 value += 1
        count_cards[card] += 1

    # 가장 많은 카드에 대한 정보를 저장할 변수를 초기화한다.
    max_count = 0
    max_num = 0
    # count_cards 딕셔너리를 순회하면서
    for num, count in count_cards.items():
        # 현재 카드의 장수가 max_count보다 크다면
        if count > max_count:
            # 최대값을 갱신한다.
            max_count = count
            max_num = num
        # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
        elif count == max_count and num > max_num:
            max_num = num

    # 결과를 출력한다.
    print(f'#{tc} {max_num} {max_count}')
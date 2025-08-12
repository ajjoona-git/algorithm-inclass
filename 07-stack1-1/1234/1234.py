# 1234. 비밀번호

# import sys
# sys.stdin = open("input.txt")


def peek(stack):
    """주어진 스택(stack)에서 마지막 데이터를 제거하지 않고 반환하는 함수"""
    if len(stack) != 0:
        return stack[-1]
    return None


def remove_pair(s):
    """주어진 문자열(s)에서 반복되는 문자쌍을 제거한 문자열을 반환하는 함수"""
    stack = []  # 문자열의 문자들을 저장할 스택

    for char in s:
        # 1. 현재 문자가 이전 문자와 동일한 경우
        if char == peek(stack):
            stack.pop()
        # 2. 현재 문자가 이전 문자와 다른 경우
        else:
            stack.append(char)

    # 모든 문자를 확인한 후에 stack에 남은 문자열을 반환
    return ''.join(stack)


T = 10
for tc in range(1, T+1):
    N, string = input().split()
    print(f'#{tc} {remove_pair(string)}')
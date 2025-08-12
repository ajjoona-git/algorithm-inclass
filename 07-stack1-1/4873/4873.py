# 4873. 반복문자 지우기 

# import sys
# sys.stdin = open('sample_input.txt')


def peek(s):
    """주어진 스택(s)의 마지막 원소를 반환하되, 제거하지 않는다."""
    if len(s) != 0:
        return s[-1]
    return None


def remove_char(s):
    """주어진 문자열(s)을 순회하면서 반복문자를 지운 문자열을 반환하는 함수"""
    # stack: 문자를 저장할 스택
    stack = []
    
    # 문자열을 순회하면서 스택에 저장한다.
    for char in s:
        # 1. 현재 문자가 스택의 마지막 값과 다른 경우
        if char != peek(stack):
            stack.append(char)
        # 2. 현재 문자가 스택의 마지막 값과 같은 경우
        else:
            stack.pop()

    # stack에 남아있는 문자들을 하나의 문자열 형태로 반환
    return ''.join(stack)
    

T = int(input())
for tc in range(1, T+1):
    s = input()
    removed_s = remove_char(s)
    print(f'#{tc} {len(removed_s)}')
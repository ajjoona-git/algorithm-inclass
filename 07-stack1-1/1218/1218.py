# 1218. 괄호 짝짓기

# import sys
# sys.stdin = open("input.txt")


def check_brackets(string):
    """4종류의 괄호문자 (), {}, [], <>로 이루어진 문자열(string)이 유효한지 검사하는 함수"""
    # stack: 여는 괄호를 저장할 스택
    stack = []
    
    # bracket_pair: 짝이 맞는지 확인하기 위한 괄호쌍 딕셔너리
    bracket_pair = { ')': '(', '}': '{', ']': '[', '>': '<' }

    # 문자열을 순회하면서 괄호 검사를 진행한다.
    for char in string:
        # 1. 여는 괄호
        if char in '({[<':
            stack.append(char)
        # 2. 닫는 괄호
        elif char in ')}]>':
            # 2-1. 스택이 비어있는 경우 0을 반환
            if len(stack) == 0:
                return 0
            # 2-2. 짝이 맞지 않는 경우 0을 반환
            else:
                if stack.pop() != bracket_pair[char]:
                    return 0
        # 3. 괄호가 아닌 문자
        else:
            continue

    if stack:
        return 0  # 모든 문자를 처리한 후에도 스택이 비어 있지 않다면, 0 반환
    else:
        return 1  # 그 외의 경우는 1을 반환
    

T = 10
for tc in range(1, T+1):
    N = int(input())
    string = input()
    print(f'#{tc} {check_brackets(string)}')
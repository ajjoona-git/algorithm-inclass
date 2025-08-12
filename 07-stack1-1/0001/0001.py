# 연습문제. 괄호 검사  

import sys
sys.stdin = open('input.txt')


def check_brackets_no_dict(string):
    # stack: 여는 괄호를 저장할 스택
    stack = []
    
    # 문자열을 순회하면서 괄호 검사를 진행한다.
    for i in string:
        # 1. 여는 괄호
        if i == '(':
            stack.append(i)
        # 2. 닫는 괄호
        else:
            # 2-1. 스택이 비어있는 경우 -1을 반환
            if len(stack) == 0:
                return -1
            # 2-2. 여는 괄호를 pop (짝맞는 괄호는 제거)
            else:
                stack.pop()

    if stack:
        return -1  # 모든 문자를 처리한 후에도 스택이 비어 있지 않다면, -1 반환
    else:
        return 1  # 그 외의 경우는 1을 반환
    

T = int(input())
for tc in range(1, T+1):
    string = input()
    print(f'#{tc} {check_brackets_no_dict(string)}')
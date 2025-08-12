# 4866. 괄호 검사

# import sys
# sys.stdin = open('sample_input.txt')


def check_brackets_no_dict(string):
    # stack: 여는 괄호를 저장할 스택
    stack = []
    
    # 문자열을 순회하면서 괄호 검사를 진행한다.
    for i in string:
        # 1. 여는 괄호
        if i in '({':
            stack.append(i)
        # 2. 닫는 괄호
        elif i in ')}':
            # 2-1. 스택이 비어있는 경우 0을 반환
            if len(stack) == 0:
                return 0
            # 2-2. 짝이 맞지 않는 경우 0을 반환
            else:
                top_char = stack.pop()
                if i == ')' and top_char != '(':
                    return 0
                elif i == '}' and top_char != '{':
                    return 0
        # 3. 괄호가 아닌 문자
        else:
            continue

    if stack:
        return 0  # 모든 문자를 처리한 후에도 스택이 비어 있지 않다면, 0 반환
    else:
        return 1  # 그 외의 경우는 1을 반환
    

T = int(input())
for tc in range(1, T+1):
    string = input()
    print(f'#{tc} {check_brackets_no_dict(string)}')
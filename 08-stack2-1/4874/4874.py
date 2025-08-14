# 4874. Forth

# import sys
# sys.stdin = open("sample_input.txt")


def calculate_postfix(expression):
    """주어진 후위 표기식(expression)을 계산한 값을 반환하는 함수"""
    # tokens: 후위 표기식이 빈칸으로 구분되어 있으므로 각 토큰을 요소로 하는 리스트 생성
    tokens = expression.split()
    # stack: 계산에 사용할 피연산자(숫자)를 저장할 스택
    stack = []

    for token in tokens:
        # 1. 피연산자(숫자)
        if token.isdigit():
            stack.append(int(token))
        
        # 2. '.' -> 연산 결과를 정수로 출력
        elif token == '.':
            # 스택에 남은 값이 하나가 아닌 경우 'error'를 출력한다.
            if len(stack) != 1:
                return 'error'
            else:
                return int(stack.pop())

        # 3. 연산자
        else:
            # 연산이 불가능한 경우 'error'를 출력한다.
            if len(stack) <= 1:
                return 'error'
            else:
                # 스택의 숫자 두 개를 pop
                # 먼저 꺼낸 숫자를 두번째 피연산자로 사용한다.
                right = stack.pop()
                left = stack.pop()
                
                # 연산
                if token == '+':
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left * right
                elif token == '/':
                    try:
                        result = left / right
                    except ZeroDivisionError:
                        return 'error'
                else:
                    raise ValueError('error')

                # 연산한 결과를 다시 스택에 push
                stack.append(result)


T = int(input())
for tc in range(1, T+1):
    postfix = input()
    print(f"#{tc} {calculate_postfix(postfix)}")
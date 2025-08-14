# 1223. 계산기2

def infix_to_postfix(expression):
    """주어진 중위 표기식(expression)을 후위 표기식으로 반환하는 함수"""
    # 연산자 우선순위 (숫자가 클수록 우선순위가 높다.)
    precedence = {
        '+': 1, '*': 2,
    }    
    # 연산자를 임시보관할 스택
    stack = []
    # 후위 표기식을 담을 리스트
    result = []

    # 중위 표기식을 토큰 단위로 순회
    for token in expression:
        # 1. 피연산자
        if token.isdigit():
            # 결과 리스트에 추가
            result.append(token)

        # 2. 연산자(+, *)
        else:
            # isp >= icp이면 pop하여 결과 리스트에 추가
            while stack and precedence.get(stack[-1], 0) >= precedence.get(token, 0):
                result.append(stack.pop())
            # isp < icp이면 스택에 push
            stack.append(token)
        
    # 중위 표기식의 모든 토큰을 처리한 후에, 
    # 스택에 남은 연산자를 모두 pop하여 결과 리스트에 추가
    while stack:
        result.append(stack.pop())
    
    # 하나의 문자열 형태로 반환
    return ''.join(result)


def calculate_postfix(expression):
    """주어진 후위 표기식(expression)을 계산한 값을 반환하는 함수"""
    # stack: 계산에 사용할 피연산자(숫자)를 저장할 스택
    stack = []

    for token in expression:
        # 1. 피연산자(숫자)
        if token.isdigit():
            stack.append(int(token))
        
        # 2. 연산자(+, *)
        else:
            # 스택의 숫자 두 개를 pop
            # 먼저 꺼낸 숫자를 두번째 피연산자로 사용한다.
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                # 연산한 결과를 다시 스택에 push
                stack.append(left + right)
            elif token == '*':
                stack.append(left * right)
    
    return stack.pop()


T = 10
for tc in range(1, T+1):
    N = int(input())  # 문자열 계산식의 길이
    expression = input()
    postfix = infix_to_postfix(expression)
    result = calculate_postfix(postfix)
    print(f'#{tc} {result}')
# 연습문제. 후위 표기법

# def infix_to_postfix(expression):
#     """주어진 중위 표기식(expression)을 후위 표기식으로 반환하는 함수"""
#     # 연산자 우선순위 (숫자가 클수록 우선순위가 높다.)
#     precedence = {
#         '+': 1, '-': 1, '*': 2, '/': 2,
#     }

#     # 연산자를 임시보관할 스택
#     stack = []
#     # 후위 표기식을 담을 리스트
#     result = []

#     # 중위 표기식을 토큰 단위로 순회
#     for token in expression:
#         # 1. 피연산자
#         if token.isalnum():
#             # 결과 리스트에 추가
#             result.append(token)

#         # 2. 여는 괄호 '('
#         elif token == '(':
#             # 스택에 추가
#             stack.append(token)

#         # 3. 닫는 괄호 ')'
#         elif token == ')':
#             # 여는 괄호가 나올 때까지 스택에서 pop하여 결과 리스트에 추가
#             while stack and stack[-1] != '(':
#                 result.append(stack.pop())
#             # 여는 괄호는 pop하여 제거
#             stack.pop()

#         # 4. 연산자
#         else:
#             # isp >= icp이면 pop하여 결과 리스트에 추가
#             while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(token, 0):
#                 result.append(stack.pop())
#             # isp < icp이면 스택에 push
#             stack.append(token)
        
#     # 중위 표기식의 모든 토큰을 처리한 후에, 
#     # 스택에 남은 연산자를 모두 pop하여 결과 리스트에 추가
#     while stack:
#         result.append(stack.pop())
    
#     # 하나의 문자열 형태로 반환
#     return ''.join(result)

def num_first(expression):
    """수식 문자열을 읽어서 피연산자는 바로 출력하고 연산자는 스택에 push 하여
    수식이 끝나면 스택의 남아있는 연산자를 모두 pop하여 출력하는 함수"""
    stack = []
    result = []

    for token in expression:
        # 1. 연산자(사칙연산)
        if token in '+-*/':
            stack.append(token)
        # 2. 피연산자
        else:
            result.append(token)

    # 수식이 끝나고 스택에 남아있는 연산자를 모두 pop
    while stack:
        result.append(stack.pop())

    return ''.join(result)


import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    postfix = input()
    print(f'#{tc} {num_first(postfix)}')
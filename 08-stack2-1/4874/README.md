# 4874. Forth | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AWTQc1MKQiIDFAVT&probBoxId=AZh-M3iq4UfHBINp&type=PROBLEM&problemBoxTitle=Stack&problemBoxCnt=16)

## 💡 접근 방식
### 1. 사용 알고리즘
* **스택(Stack)** 자료구조
* **후위 표기식(Postfix Notation)** 계산

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 후위 표기식 문자열을 입력받습니다.
2.  후위 표기식을 계산하는 `calculate_postfix` 함수를 정의합니다.
3.  입력받은 문자열을 공백 기준으로 분리하여 토큰 리스트를 생성하고, 계산에 사용할 스택을 초기화합니다.
4.  토큰 리스트를 순회하며 각 토큰의 종류에 따라 다르게 처리합니다.
5.  **토큰이 숫자일 경우**: 정수로 변환하여 스택에 추가합니다.
6.  **토큰이 연산자일 경우**: 스택에 두 개의 피연산자가 있는지 확인하고, 부족하면 'error'를 반환합니다. 그렇지 않으면 스택에서 두 개의 숫자를 꺼내 연산하고 결과를 다시 스택에 넣습니다. (먼저 꺼낸 숫자가 두 번째 피연산자가 됨)
7.  **토큰이 `'.'`일 경우**: 스택에 하나의 숫자만 남아있는지 확인하고, 아니면 'error'를 반환합니다. 하나만 남아있다면 그 값을 반환합니다.
8.  모든 연산이 끝났는데도 스택에 하나의 값만 남아있지 않다면 'error'를 반환합니다.
9.  각 테스트 케이스마다 `calculate_postfix` 함수를 호출하여 결과를 얻고, 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [4874.py](4874.py)
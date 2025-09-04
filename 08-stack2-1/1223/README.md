# 1223. 계산기 2 | D4

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AV14nnAaAFACFAYD&probBoxId=AZh-M3iq4UfHBINp&type=PROBLEM&problemBoxTitle=Stack&problemBoxCnt=16)

## 💡 접근 방식

### 1. 사용 알고리즘
* **스택(Stack)** 자료구조
* **중위 표기식(Infix)을 후위 표기식(Postfix)으로 변환**
* **후위 표기식(Postfix) 계산**

### 2. 문제 풀이 과정
1.  이 문제는 두 단계로 나눌 수 있습니다. 첫 번째는 중위 표기식으로 주어진 수식을 후위 표기식으로 변환하는 것이고, 두 번째는 변환된 후위 표기식을 계산하는 것입니다. 두 단계 모두 **스택(Stack)** 자료구조를 활용합니다.
2.  **`infix_to_postfix` 함수**: 중위 표기식을 후위 표기식으로 변환하는 역할을 합니다.
    * 수식을 순회하며 피연산자(숫자)는 결과 리스트에 바로 추가합니다.
    * 연산자(`+`, `*`)는 스택에 임시로 저장합니다. 이때, **연산자 우선순위**를 고려하여 스택의 연산자와 현재 연산자를 비교합니다. 현재 연산자보다 우선순위가 높거나 같은 연산자는 스택에서 `pop`하여 결과 리스트에 추가합니다.
3.  **`calculate_postfix` 함수**: 후위 표기식을 계산하여 최종 결과를 도출합니다.
    * 후위 표기식(문자열)을 순회하며 피연산자(숫자)는 스택에 쌓습니다.
    * 연산자(`+`, `*`)를 만나면 스택에서 숫자 두 개를 `pop`하여 연산하고, 그 결과를 다시 스택에 `push`합니다.
4.  모든 연산이 끝나면 스택에 마지막으로 남아있는 값이 최종 계산 결과가 됩니다.

---

## 💻 코드
* [1223.py](1223.py)
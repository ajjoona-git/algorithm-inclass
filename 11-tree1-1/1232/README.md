# 1232. 사칙연산 | D4

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AV141J8KAIcCFAYD&probBoxId=AZjPzi56xljHBIO0&type=PROBLEM&problemBoxTitle=Tree&problemBoxCnt=3)

## 💡 접근 방식

### 1. 사용 알고리즘
* **트리 (Tree)** / **식 트리 (Expression Tree)**
* **후위 순회 (Post-order Traversal)**
* **재귀 (Recursion)**

### 2. 문제 풀이 과정
1.  **문제 이해 및 트리 모델링**: 주어진 사칙연산은 연산자가 부모 노드가 되고 피연산자가 자식 노드가 되는 **식 트리(Expression Tree)**로 모델링할 수 있습니다. 이 트리 구조를 계산하기 위해서는 자식 노드의 계산이 먼저 완료되어야 합니다.
2.  **후위 순회(Post-order) 선택**: '왼쪽 자식 -> 오른쪽 자식 -> 부모 노드 방문' 순서로 순회하는 **후위 순회(Post-order Traversal)** 방식은 자식 노드의 값을 먼저 얻은 후, 부모 노드에서 해당 값들을 연산하는 흐름과 정확히 일치합니다. 따라서 후위 순회를 사용하여 이 문제를 해결합니다.
3.  **재귀 함수 구현**:
    * `postorder(node)`라는 재귀 함수를 정의합니다. 이 함수는 특정 노드를 루트로 하는 서브트리의 연산 결과를 반환합니다.
    * **Base Case (기저 조건)**: 현재 노드가 리프 노드(피연산자, 즉 숫자)일 경우, 해당 숫자 값을 `float`으로 변환하여 반환합니다.
    * **Recursive Step (재귀 단계)**: 현재 노드가 연산자일 경우,
        1.  `postorder` 함수를 재귀적으로 호출하여 왼쪽 자식과 오른쪽 자식 서브트리의 계산 결과(`left`, `right`)를 각각 얻습니다. **(L, R)**
        2.  현재 노드의 연산자를 확인하고, `left`와 `right` 값을 해당 연산자로 계산합니다. **(V)**
        3.  연산 결과를 상위 노드로 반환합니다.
4.  **실행 및 결과 출력**:
    * 입력값을 받아 트리를 구성합니다.
    * 루트 노드인 `1`부터 `postorder(1)`을 호출하여 전체 트리의 연산을 시작합니다.
    * 최종적으로 반환된 실수형 결과를 정수형으로 변환하여 형식에 맞게 출력합니다.


---

## 💻 코드
* [1232.py](1232.py)
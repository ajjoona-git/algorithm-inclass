# 1231. 중위순회 | D4

## 문제 출처
![SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AV140YnqAIECFAYD&probBoxId=AZjPzi56xljHBIO0&type=PROBLEM&problemBoxTitle=Tree&problemBoxCnt=3)

## 💡 접근 방식

### 1. 사용 알고리즘
* **트리 (Tree)**
* **재귀 (Recursion)**
* **중위 순회 (In-order Traversal)**

### 2. 문제 풀이 과정
1.  **트리 정보 저장**: 정점의 개수 `N`을 입력받고, `edge`라는 리스트를 생성하여 각 정점(노드)의 정보를 저장합니다. `edge[i]`에는 `i`번 정점의 [데이터, 왼쪽 자식, 오른쪽 자식] 정보가 리스트 형태로 저장됩니다.
2.  **중위 순회(In-order) 함수 정의**: 재귀를 사용하여 중위 순회를 구현합니다. 중위 순회는 **L(왼쪽 자식) -> V(방문) -> R(오른쪽 자식)** 순서로 동작합니다.
    * `inorder(node)` 함수는 현재 노드 `node`를 인자로 받습니다.
    * 순회 결과를 저장할 `result` 리스트를 전역 변수로 사용합니다.
    * **Base Case**: 리프 노드(자식이 없는 노드)에 도달하면 재귀가 자연스럽게 종료됩니다.
    * **Recursive Step (LVR)**:
        1.  **L(Left)**: 현재 노드에 왼쪽 자식이 있다면, `inorder(left_child)`를 호출하여 왼쪽 서브트리를 먼저 순회합니다.
        2.  **V(Visit)**: 왼쪽 서브트리 순회가 끝나면, 현재 노드의 데이터(문자)를 `result` 리스트에 추가합니다.
        3.  **R(Right)**: 현재 노드에 오른쪽 자식이 있다면, `inorder(right_child)`를 호출하여 오른쪽 서브트리를 순회합니다.
3.  **순회 시작 및 결과 출력**:
    * 루트 노드인 `1`을 시작으로 `inorder(1)` 함수를 호출하여 전체 트리 순회를 시작합니다.
    * 순회가 모두 끝나면 `result` 리스트에는 중위 순회 순서대로 문자 데이터가 저장됩니다.
    * `join()` 함수를 사용하여 `result` 리스트의 문자들을 하나의 문자열로 합쳐 최종 결과를 출력합니다.



---

## 💻 코드
* [1231.py](1231.py)
# 5174. subtree | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AWTay1Z64cQDFAVT&probBoxId=AZjPzi56xljHBIO0&type=PROBLEM&problemBoxTitle=Tree&problemBoxCnt=3)

## 💡 접근 방식

### 1. 사용 알고리즘
* **트리 (Tree)**
* **재귀 (Recursion)**
* **트리 순회 (Tree Traversal)**

### 2. 문제 풀이 과정
1.  **트리 구성**: 주어진 간선(`E`)의 개수와 노드 정보를 바탕으로 트리를 구현합니다. 각 노드의 왼쪽 자식과 오른쪽 자식을 저장하는 `left`, `right` 리스트를 생성하고, 입력받은 부모-자식 관계에 따라 리스트를 채워줍니다.
2.  **서브트리 순회 함수 정의**: 특정 노드(`N`)를 루트로 하는 서브트리의 노드 개수를 세기 위해, 재귀를 이용한 순회 함수 `preorder(node)`를 정의합니다.
3.  **노드 개수 카운팅**:
    * 노드의 개수를 저장할 전역 변수 `cnt_node`를 `0`으로 초기화합니다.
    * `preorder` 함수는 현재 방문한 노드가 유효할 경우(0이 아닐 경우), `cnt_node`를 1 증가시킵니다.
    * 그 후, 현재 노드의 왼쪽 자식과 오른쪽 자식에 대해 각각 `preorder` 함수를 재귀적으로 호출하여 모든 자손 노드를 방문하도록 합니다.
4.  **순회 시작 및 결과 출력**: 입력으로 주어진 노드 `N`을 시작점으로 `preorder(N)` 함수를 호출합니다. 재귀 호출이 모두 끝나면 `cnt_node`에는 `N`을 포함한 서브트리의 전체 노드 개수가 저장되며, 이 값을 형식에 맞게 출력합니다.



---

## 💻 코드
* [5174.py](5174.py)
# 1865. 동철이의 일 분배 | D4

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc&categoryId=AV5LuHfqDz8DFAXc&categoryType=CODE&problemTitle=1865&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

## 💡 접근 방식

### 1. 사용 알고리즘
* **완전 탐색 (Brute-force Search) / 순열 (Permutations)**
* **깊이 우선 탐색 (DFS, Depth-First Search)**
* **백트래킹 (Backtracking)**
* **가지치기 (Pruning)**

### 2. 문제 풀이 과정
1.  **문제 모델링**: N명의 직원에게 N개의 일을 하나씩 중복 없이 배분하여, 성공 확률의 곱이 최대가 되는 경우를 찾는 문제입니다. 이는 직원 순서에 따라 할당할 수 있는 일의 모든 순서, 즉 **순열(Permutation)**을 고려해야 하는 **완전 탐색** 문제입니다.
2.  **DFS와 백트래킹을 이용한 순열 생성**:
    * 재귀 함수 `get_percent(i, percent)`를 사용하여 깊이 우선 탐색(DFS) 방식으로 모든 할당 경우의 수를 탐색합니다.
    * `i`는 현재 일을 할당할 직원의 번호, `percent`는 `i-1`번 직원까지 일을 할당했을 때의 누적 성공 확률을 의미합니다.
    * `allocated` 배열을 통해 특정 일이 이미 다른 직원에게 할당되었는지 여부를 확인합니다.
    * `i`번 직원에게 `j`번 일을 할당하는 모든 경우(`for j in range(N)`)를 탐색합니다.
    * **백트래킹**: `i`번 직원에게 `j`번 일을 할당하는 경우를 탐색(재귀 호출)한 뒤에는, `allocated[j] = False`로 상태를 원상 복구합니다. 이를 통해 다른 직원이 `j`번 일을 할당받는 새로운 경우의 수를 탐색할 수 있습니다.
3.  **가지치기(Pruning)를 통한 최적화**:
    * 확률은 곱할수록 1보다 작거나 같아지므로, 누적 확률값(`percent`)은 계속 감소하거나 유지됩니다.
    * 따라서 탐색 도중 `percent`가 이미 이전에 찾은 최대 확률 `max_percent`보다 작거나 같아진다면, 더 이상 탐색을 진행해도 더 좋은 결과를 얻을 수 없습니다.
    * 이 경우, 즉시 `return`하여 불필요한 탐색을 중단하고 효율성을 높입니다.
4.  **종료 조건**:
    * `i`가 `N`이 되면 모든 직원에게 일이 할당된 것입니다. 이때의 최종 확률을 `max_percent`와 비교하여 최대값을 갱신합니다.
5.  **실행**: 0번 직원부터(`i=0`), 초기 확률 1로(`percent=1`) 탐색을 시작하고, 모든 탐색이 끝난 뒤 `max_percent`에 저장된 최종 값을 형식에 맞게 출력합니다.

---

## 💻 코드
* [1865.py](1865.py)
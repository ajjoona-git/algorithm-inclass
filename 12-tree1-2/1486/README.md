# 1486. 장훈이의 높은 선반 | D4

## 문제 출처
![SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw&categoryId=AV2b7Yf6ABcBBASw&categoryType=CODE&problemTitle=1486&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)


## 💡 접근 방식

### 1. 사용 알고리즘
* **깊이 우선 탐색 (DFS, Depth-First Search)**
* **재귀 (Recursion)**
* **백트래킹 (Backtracking) / 가지치기 (Pruning)**

### 2. 문제 풀이 과정
1.  **문제 모델링**: 점원들의 모든 부분 집합의 합을 구하는 문제입니다. 이 문제는 각 점원을 부분 집합에 포함시키거나 포함시키지 않는 모든 경우의 수를 탐색하는 것과 같으며, **깊이 우선 탐색(DFS)** 방식의 재귀로 해결할 수 있습니다.
2.  **재귀 함수 설계**:
    * `sum_heights(i, curr_height)` 함수는 `i`번째 점원까지를 포함하여 만든 탑의 높이가 `curr_height`일 때, `i+1`번째 점원부터 추가하여 만들 수 있는 모든 탑의 높이를 탐색하는 역할을 합니다.
    * `for` 루프를 통해 `i+1`번째부터 `N-1`번째까지의 각 점원(`next_idx`)을 현재 탑에 추가하는 경우를 재귀적으로 호출합니다. `i`보다 큰 인덱스만 탐색함으로써, 같은 부분 집합이 중복으로 생성되는 것을 방지합니다. (예: `(0번, 1번)` 탑만 고려하고 `(1번, 0번)` 탑은 고려하지 않음)
3.  **가지치기 (Pruning)를 통한 최적화**:
    * 재귀 호출 중에 현재까지 쌓은 탑의 높이(`curr_height`)가 선반의 높이(`B`)를 넘어서는 순간, 더 이상 점원을 추가하는 것은 무의미합니다. 추가할수록 `B`와의 차이만 더 커지기 때문입니다.
    * 따라서, `curr_height >= B`인 경우, `min_diff`를 갱신하고 즉시 `return`하여 불필요한 탐색을 중단합니다(가지치기).
4.  **탐색 시작 및 실행**:
    * 메인 로직에서는 `for` 루프를 통해 0번 점원부터 N-1번 점원까지 각각을 **시작 점원**으로 하여 `sum_heights` 함수를 호출합니다.
    * 예를 들어, `sum_heights(0, heights[0])` 호출은 0번 점원을 반드시 포함하는 모든 부분 집합을 탐색하게 됩니다.
    * 이 과정을 모든 점원에 대해 반복하여 모든 가능한 부분 집합을 검토하고, 최종적으로 `min_diff`에 저장된 최소 차이 값을 출력합니다.


---

## 💻 코드
* [1486.py](1486.py)
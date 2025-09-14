# 2819. 격자판의 숫자 이어붙이기 | D4


## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE&problemTitle=2819&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&)

## 💡 접근 방식

### 1. 사용 알고리즘
* **깊이 우선 탐색 (DFS, Depth-First Search)**
* **재귀 (Recursion)**
* **메모이제이션 (Memoization) / 가지치기 (Pruning)**
* **백트래킹 (Backtracking)**

### 2. 문제 풀이 과정
1.  **문제 모델링**: 4x4 격자판의 각 칸을 정점으로, 인접한 칸들을 간선으로 하는 그래프에서 길이가 7인 모든 경로를 찾는 문제로 볼 수 있습니다. 각 경로를 구성하는 숫자들을 이어 붙여 만들 수 있는 고유한 7자리 숫자의 개수를 구하는 것이 목표입니다.
2.  **DFS를 이용한 경로 탐색**: 모든 경로를 탐색하기 위해 **깊이 우선 탐색(DFS)** 방식의 재귀 함수 `get_number(r, c, num_str, count)`를 사용합니다.
    * `(r, c)`는 현재 위치, `num_str`은 현재까지 만들어진 숫자 문자열, `count`는 문자열의 길이를 의미합니다.
    * **종료 조건**: `count`가 7이 되면 7자리 숫자가 완성된 것이므로, `numbers`라는 `set`에 추가하여 중복을 자동으로 제거합니다.
3.  **메모이제이션을 통한 최적화**:
    * 이 문제는 동일한 위치에 동일한 부분 문자열로 도달하는 경우가 매우 많아, 단순 DFS로는 시간 초과가 발생할 수 있습니다.
    * 이를 해결하기 위해 `memo[r][c]`라는 2차원 배열을 사용해 **메모이제이션**을 적용합니다. `memo[r][c]`는 `(r, c)` 위치에서 이미 탐색을 시작했던 모든 부분 문자열을 `set` 형태로 저장합니다.
    * 재귀 함수가 호출될 때, `num_str`이 `memo[r][c]`에 이미 존재한다면, 이는 이전에 동일한 상태에서 탐색을 이미 완료했다는 의미이므로, 더 이상 탐색하지 않고 즉시 `return`하여 불필요한 중복 계산을 방지합니다(가지치기).
4.  **전체 탐색 실행**:
    * `for` 루프를 사용하여 격자판의 모든 칸 `(r, c)`를 한 번씩 시작점으로 삼아 `get_number` 함수를 호출합니다.
    * 모든 탐색이 완료되면 `numbers` set에 저장된 고유한 7자리 숫자의 총개수를 출력합니다.


---

## 💻 코드
* [2819.py](2819.py)
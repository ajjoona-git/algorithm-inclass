# 4012. 요리사

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&categoryId=AWIeUtVakTMDFAVH&categoryType=CODE&problemTitle=4012&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

## 💡 접근 방식 1: 조합

### 1. 사용 알고리즘
* **조합 (Combinations)**
* **브루트포스 (Brute-force)**

### 2. 문제 풀이 과정
1.  N개의 식재료를 N/2개씩 두 그룹으로 나누는 모든 경우의 수를 탐색하여, 두 그룹(음식)의 맛 차이가 최소가 되는 경우를 찾는 문제입니다.
2.  먼저 N개의 식재료(인덱스 0부터 N-1) 중 첫 번째 음식(A)에 사용할 N/2개의 식재료를 선택합니다. 이 과정은 Python의 `itertools` 모듈에 있는 `combinations` 함수를 사용하여 구현합니다. `combinations(range(N), N//2)`는 가능한 모든 조합을 생성합니다.
3.  A음식에 포함될 식재료 조합(`group_a`)이 정해지면, 나머지 식재료는 자연스럽게 두 번째 음식(B)의 재료(`group_b`)가 됩니다.
4.  각 그룹 내에서 맛(시너지의 총합)을 계산합니다. 그룹 내의 모든 식재료 쌍`(i, j)`에 대해 시너지 값 `S_ij`와 `S_ji`를 모두 더해줍니다. 이 역시 `combinations(group, 2)`를 통해 모든 쌍을 효율적으로 구할 수 있습니다.
5.  두 음식 A와 B의 맛을 각각 계산한 후, 두 값의 차이(`abs(synergy_a - synergy_b)`)를 구합니다.
6.  이 차이 값을 이전에 계산된 최소 차이(`min_diff`)와 비교하여 더 작은 값으로 `min_diff`를 계속 갱신합니다.
7.  모든 조합을 탐색하고 나면 `min_diff`에 최종적인 최소값이 남게 되며, 이를 형식에 맞춰 출력합니다.

### 💻 코드
* [4012.py](4012.py)

---

## 💡 접근 방식 2: 재귀

### 1. 사용 알고리즘
* **완전 탐색 (Brute-force Search) / 조합 (Combinations)**
* **깊이 우선 탐색 (DFS, Depth-First Search)**
* **재귀 (Recursion) & 백트래킹 (Backtracking)**

### 2. 문제 풀이 과정
1.  **문제 모델링**: N개의 식재료를 N/2개씩 두 그룹(A음식, B음식)으로 나누는 모든 경우의 수를 탐색하여, 두 음식의 맛 차이가 최소가 되는 경우를 찾는 문제입니다. 이는 N개의 재료 중 A음식에 사용할 N/2개의 재료를 선택하는 **조합(Combination)**을 모두 구하는 것과 같습니다.
2.  **DFS와 백트래킹을 이용한 조합 생성**:
    * 재귀 함수 `pick_items(count, idx)`를 사용하여 깊이 우선 탐색(DFS) 방식으로 A음식에 들어갈 N/2개의 재료 조합을 모두 생성합니다.
    * `count`는 현재까지 A음식 재료로 선택된 재료의 개수, `idx`는 조합의 중복 생성을 막기 위한 시작 인덱스입니다.
    * **재귀 호출**: `idx` 다음 재료부터 하나를 선택하여 A음식 재료로 포함시키고(`food[next_idx] = 1`), `count`를 1 증가시켜 다음 재료를 선택하기 위해 재귀 호출을 합니다.
    * **백트래킹**: 한 재료에 대한 재귀 호출이 끝난 후에는, 해당 재료를 다시 B음식 재료로 되돌려(`food[next_idx] = 0`) 다른 조합을 탐색할 수 있도록 합니다.
3.  **종료 조건 및 맛 계산**:
    * `count`가 `N // 2`가 되면 A음식에 필요한 재료 선택이 완료된 것입니다.
    * `food` 배열을 기준으로 A음식과 B음식의 재료 목록을 나누고, 각 음식의 시너지 합을 계산하여 맛의 차이를 구합니다.
    * 계산된 맛의 차이를 `min_diff`와 비교하여 최소값을 갱신합니다.
4.  **실행**: `pick_items(0, -1)` (또는 유사한 초기값)을 호출하여 탐색을 시작하고, 모든 조합에 대한 탐색이 끝난 뒤 `min_diff`에 저장된 최종 최소값을 출력합니다.

### 💻 코드
* [4012v2.py](4012v2.py)

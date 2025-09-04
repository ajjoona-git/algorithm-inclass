# 4012. 요리사

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&categoryId=AWIeUtVakTMDFAVH&categoryType=CODE&problemTitle=4012&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

## 💡 접근 방식

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

---

## 💻 코드
* [4012.py](4012.py)
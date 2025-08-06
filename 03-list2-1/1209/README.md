# 1209. Sum | D3

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=1209&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **2차원 배열 순회**

### 2. 문제 풀이 과정
1.  먼저 100x100 크기의 2차원 배열 `arr`를 입력받아 저장합니다.
2.  각 행의 합, 각 열의 합, 두 대각선의 합 중에서 최대값을 저장할 변수 `max_sum`을 `0`으로 초기화합니다.
3.  **행의 합**을 계산하기 위해 이중 반복문을 사용하여 각 행의 합(`row_sum`)을 구하고, `max_sum`과 비교하여 더 큰 값으로 갱신합니다.
4.  **열의 합**을 계산하기 위해 다시 이중 반복문을 사용하여 각 열의 합(`col_sum`)을 구하고, `max_sum`과 비교하여 갱신합니다.
5.  **메인 대각선(`\`)의 합**을 계산하기 위해 단일 반복문을 사용합니다. `arr[i][i]`의 합을 구한 후 `max_sum`과 비교하여 갱신합니다.
6.  **반대 대각선(`/`)의 합**을 계산하기 위해 다시 단일 반복문을 사용합니다. `arr[i][N-1-i]`의 합을 구한 후 `max_sum`과 비교하여 갱신합니다.
7.  모든 계산이 끝난 후, 최종적으로 `max_sum`에 저장된 값을 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [1209.py](1209.py)
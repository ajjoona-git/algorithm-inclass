# 2005. 파스칼의 삼각형 | D2

## 문제 출처
![SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE&problemTitle=2005&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **재귀(Recursion)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 파스칼의 삼각형의 크기 `N`을 입력받습니다.
2.  `nth_pascal_triangle(N)` 함수를 정의하여 `N`번째 파스칼의 삼각형 한 줄을 리스트 형태로 반환하도록 재귀적으로 구현합니다.
3.  **기저 조건(Base Case)**: `N`이 1일 경우, 첫 번째 줄인 `[1]`을 반환합니다.
4.  **재귀 단계**:
    * `nth_pascal_triangle(N-1)`을 재귀 호출하여 이전 줄을 가져옵니다.
    * 이전 줄의 양 끝에 `0`을 추가하여 `prior_line`을 만듭니다. (예: `[1, 2, 1]` -> `[0, 1, 2, 1, 0]`)
    * `for` 반복문을 사용하여 `prior_line`을 순회하면서 인접한 두 숫자의 합을 계산하여 새로운 줄(`new_line`)을 만듭니다.
5.  함수는 `new_line`을 반환합니다.
6.  각 테스트 케이스마다 `for` 반복문을 사용하여 `1`부터 `N`까지 `nth_pascal_triangle` 함수를 호출하고, 반환된 리스트를 `*`를 이용해 공백으로 구분하여 출력합니다.


---

## 💻 코드
* [2005.py](2005.py)
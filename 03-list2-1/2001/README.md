# 2001. 파리 퇴치 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE&problemTitle=2001&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **슬라이딩 윈도우(Sliding Window)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 `N x N` 크기의 배열 `flies`와 파리채의 크기 `M`을 입력받습니다.
2.  이 문제는 `N x N` 배열에서 `M x M` 크기의 부분 배열의 합을 구하는 문제이므로 **슬라이딩 윈도우** 기법을 적용할 수 있습니다.
3.  파리채로 잡을 수 있는 파리의 수의 최대값을 저장할 `max_flies` 변수를 `0`으로 초기화합니다.
4.  이중 반복문을 사용하여 `flies` 배열을 순회하면서 `M x M` 크기의 윈도우를 이동시킵니다. 바깥쪽 반복문은 행의 시작 위치 `r`을, 안쪽 반복문은 열의 시작 위치 `c`를 결정합니다.
5.  각 윈도우의 시작점 `(r, c)`에서 다시 이중 반복문을 사용하여 윈도우 내부에 있는 모든 파리의 수를 합산합니다. `num_of_flies` 변수에 `flies[r+i][c+j]` 값을 더합니다.
6.  이 과정에서 윈도우가 배열의 경계를 벗어나지 않도록 `0 <= nr < N`과 `0 <= nc < N`과 같은 조건으로 경계 체크를 합니다.
7.  `M x M` 윈도우의 합산이 끝나면, `max(max_flies, num_of_flies)`를 통해 `max_flies`를 갱신합니다.
8.  모든 윈도우에 대한 계산이 끝나면, `max_flies`에 저장된 최종 값을 테스트 케이스 번호와 함께 출력 형식에 맞춰 출력합니다.



---

## 💻 코드
* [2001.py](2001.py)
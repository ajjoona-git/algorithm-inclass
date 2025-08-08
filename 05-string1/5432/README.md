# 5432. 쇠막대기 자르기 | D4

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AWVl47b6DGMDFAXm&probBoxId=AZh-M3iq4UjHBINp&type=PROBLEM&problemBoxTitle=String&problemBoxCnt=5)

## 💡 접근 방식

### 1. 사용 알고리즘
* **스택(Stack)** 자료구조

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 쇠막대기와 레이저의 배치 정보가 담긴 문자열 `info`를 입력받습니다.
2.  쇠막대기의 시작점을 저장할 `stick` 리스트(스택)를 초기화하고, 잘린 쇠막대기 조각의 총 수를 저장할 `result` 변수를 `0`으로 초기화합니다.
3.  `info` 문자열을 처음부터 끝까지 순회합니다.
4.  현재 문자가 **`'('`**이면, 쇠막대기의 시작점이므로 해당 인덱스를 `stick` 스택에 `append`합니다.
5.  현재 문자가 **`')'`**이면, 가장 최근에 열린 괄호가 닫힌다는 뜻이므로 `stick` 스택에서 마지막 요소를 `pop`합니다.
6.  `pop`한 인덱스와 현재 인덱스 `i`를 비교하여 레이저인지 쇠막대기의 끝인지 판단합니다.
    * 만약 `pop`한 인덱스가 `i - 1`이라면, `'()'` 형태이므로 레이저입니다. 레이저는 현재 `stick` 스택에 남아있는 쇠막대기 수(`len(stick)`)만큼 조각을 만드므로, `result`에 이 값을 더합니다.
    * 만약 `pop`한 인덱스가 `i - 1`이 아니라면, 쇠막대기의 끝입니다. 쇠막대기의 끝에서는 그 자체로 하나의 조각이 생기므로 `result`에 `1`을 더합니다.
7.  모든 문자열 순회가 끝나면 `result`에 저장된 최종 조각의 수를 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [5432.py](5432.py)
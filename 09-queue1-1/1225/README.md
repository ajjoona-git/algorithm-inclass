# 1225. 암호생성기 | D3

## 문제 출처
![SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AV14uWl6AF0CFAYD&probBoxId=AZh9VAAaxs3HBINp&type=PROBLEM&problemBoxTitle=Queue&problemBoxCnt=6)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **큐(Queue)** 자료구조 - 리스트 활용

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`가 10으로 고정되어 있으며, 각 테스트 케이스마다 암호문을 담은 리스트 `passcode`를 입력받습니다.
2.  이 문제는 큐의 동작 방식인 **FIFO(First-In, First-Out)**를 사용하여 풀 수 있습니다. 파이썬 리스트의 `pop(0)`와 `append()` 메소드를 활용하여 큐처럼 구현합니다.
3.  `i` 변수를 `0`으로 초기화하여 감소시킬 숫자를 1부터 5까지 순환하도록 설정합니다.
4.  `while 0 not in passcode` 반복문을 사용하여 암호문에 `0`이 포함되지 않을 때까지 큐 연산을 반복합니다.
5.  매 반복마다 `i`를 1 증가시키고, `i`가 5를 초과하면 다시 1로 초기화하여 1부터 5까지 순환하도록 합니다.
6.  `pop(0)`를 사용하여 리스트의 첫 번째 숫자를 꺼낸 후, `i`만큼 감소시킵니다.
7.  감소된 숫자가 `0`보다 작아지면 `0`으로 만들고, 이 숫자를 리스트의 끝에 `append`합니다.
8.  `while` 반복문이 종료되면 `passcode` 리스트에는 `0`이 포함된 최종 암호문이 남게 됩니다.
9.  최종 암호문을 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [1225.py](1225.py)
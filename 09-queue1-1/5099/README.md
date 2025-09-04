# 5099. 피자 굽기 | D3

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AWTVlVB6bvMDFAVT&probBoxId=AZh9VAAaxs3HBINp&type=PROBLEM&problemBoxTitle=Queue&problemBoxCnt=6&&&&&&)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **큐(Queue)** 자료구조 - 원형 큐

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 화덕의 크기 `N`과 피자의 개수 `M`을 입력받습니다.
2.  피자의 치즈 양을 저장할 리스트 `pizza`를 생성합니다.
3.  피자를 굽는 과정을 시뮬레이션하기 위해 **원형 큐(CircularQueue)**를 사용하여 화덕을 구현합니다. 이 큐에는 피자의 번호(인덱스)가 저장됩니다.
4.  `for` 반복문을 통해 대기 중인 피자들을 화덕에 차례대로 넣습니다.
5.  `while` 반복문을 사용하여 화덕에 피자가 하나만 남을 때까지 피자를 순환시킵니다.
6.  화덕에서 피자를 하나 꺼내(`dequeue`), 치즈의 양을 절반으로 줄입니다.
7.  치즈가 아직 남아있다면(`pizza[check] > 0`), 그 피자를 다시 화덕에 넣습니다(`enqueue`).
8.  치즈가 모두 녹았고(`pizza[check] <= 0`) 대기 중인 피자가 있다면, 새로운 피자를 화덕에 넣습니다.
9.  화덕에 피자가 하나만 남게 되면, 해당 피자의 번호를 `last_pizza`에 저장하고 반복문을 종료합니다.
10. 최종적으로 `last_pizza`에 저장된 값을 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [5099.py](5099.py)
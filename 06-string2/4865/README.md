# 4865. 글자수 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **딕셔너리(Dictionary)**를 활용한 빈도수 계산

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 두 개의 문자열 `str1`과 `str2`를 입력받습니다.
2.  `str1`의 각 문자와 해당 문자의 출현 횟수를 저장할 딕셔너리 `str_count`를 생성합니다. `setdefault()` 메소드를 사용하여 `str1`의 각 문자를 키로, 초기값 `0`을 값으로 설정합니다.
3.  `str2`를 순회하면서, `str2`의 각 문자 `char`가 `str_count`의 키에 포함되는지 확인합니다.
4.  `char`가 `str_count`에 존재하면 해당 키의 값을 1 증가시킵니다.
5.  `str2`의 모든 문자에 대한 순회가 끝나면, `str_count` 딕셔너리에 `str1`의 각 문자가 `str2`에 몇 번씩 포함되었는지 기록됩니다.
6.  `max(str_count.values())`를 사용하여 딕셔너리의 값들 중 최댓값을 찾아 `max_count`에 저장합니다.
7.  최종적으로 `max_count` 값을 테스트 케이스 번호와 함께 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [4865.py](4865.py)
# 1234. 비밀번호 | D3

## 문제 출처
![SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14_DEKAJcCFAYD&categoryId=AV14_DEKAJcCFAYD&categoryType=CODE&problemTitle=1234&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

## 💡 접근 방식

### 1. 사용 알고리즘
* **스택(Stack)** 자료구조

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 길이 `N`과 비밀번호 문자열 `string`을 입력받습니다.
2.  이 문제는 스택을 이용하여 연속되는 동일한 문자쌍을 제거하는 방식으로 해결할 수 있습니다.
3.  스택의 맨 위 요소를 확인하는 함수 `peek(stack)`를 정의합니다. 스택이 비어있지 않다면 마지막 원소를 반환하고, 비어있다면 `None`을 반환하여 예외 처리를 대신합니다.
4.  반복 문자쌍을 제거하는 함수 `remove_pair(s)`를 정의합니다.
5.  함수 내부에서 빈 스택을 생성하고, 입력받은 문자열 `s`를 순회합니다.
6.  현재 문자가 스택의 맨 위 값과 동일하다면, 연속된 문자쌍이 발생한 것이므로 스택에서 `pop()`하여 제거합니다.
7.  현재 문자가 스택의 맨 위 값과 다르다면, 스택에 `append()` 합니다.
8.  문자열의 모든 문자에 대한 순회가 끝나면, 스택에 남아있는 문자들을 `"".join(stack)`을 사용하여 하나의 문자열로 결합한 후 반환합니다.
9.  최종적으로 `remove_pair` 함수를 호출하여 반환된 문자열을 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [1234.py](1234.py)
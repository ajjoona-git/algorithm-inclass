# 1218. 괄호 짝짓기 | D4

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14eWb6AAkCFAYD&categoryId=AV14eWb6AAkCFAYD&categoryType=CODE&problemTitle=1218&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

## 💡 접근 방식

### 1. 사용 알고리즘
* **스택(Stack)** 자료구조
* **딕셔너리(Dictionary)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 길이 `N`과 괄호 검사를 진행할 문자열 `string`을 입력받습니다.
2.  괄호의 짝을 효율적으로 검사하기 위해 **스택(Stack)** 자료구조와 괄호쌍을 저장할 **딕셔너리(`bracket_pair`)**를 활용합니다.
3.  `check_brackets(string)` 함수를 정의하여 괄호 검사 로직을 구현합니다.
4.  함수 내부에서 빈 스택을 생성하고, `string`을 순회하면서 괄호 문자를 처리합니다.
5.  현재 문자가 **여는 괄호(`(`, `{`, `[`, `<`)**일 경우, 스택에 `push`(리스트의 `append`)합니다.
6.  현재 문자가 **닫는 괄호(`)`, `}`, `]`, `>`)**일 경우, 스택이 비어있는지 확인합니다.
    * 스택이 비어있다면 닫는 괄호에 해당하는 여는 괄호가 없다는 의미이므로 `0`을 반환합니다.
    * 스택이 비어있지 않다면 스택의 맨 위 요소를 `pop()`하여 `bracket_pair` 딕셔너리를 통해 현재 닫는 괄호와 짝이 맞는지 확인합니다. 짝이 맞지 않으면 `0`을 반환합니다.
7.  괄호가 아닌 문자는 `continue`를 통해 무시합니다.
8.  `string`의 모든 문자를 처리한 후, 스택이 비어있다면 모든 괄호의 짝이 맞으므로 `1`을 반환합니다. 스택에 괄호가 남아있다면 짝이 맞지 않은 것이므로 `0`을 반환합니다.
9.  최종적으로 `check_brackets` 함수의 반환 값을 출력 형식에 맞춰 출력합니다.



---

## 💻 코드
* [1218.py](1218.py)
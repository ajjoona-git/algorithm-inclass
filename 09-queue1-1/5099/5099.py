# 5099. 피자 굽기


# import sys
# sys.stdin = open("sample_input.txt")


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.items = [None] * self.capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        """큐가 비어있는지 확인"""
        return self.front == self.rear
    
    def is_full(self):
        """큐가 가득 찼는지 확인"""
        return (self.rear + 1) % self.capacity == self.front
    
    def enqueue(self, item):
        """큐에 새로운 요소(item)을 추가"""
        # 큐가 가득찼는지 확인
        if self.is_full():
            raise IndexError("큐가 가득 찼습니다.")
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item

    def dequeue(self):
        """큐에서 데이터를 반환하고 삭제"""
        # 큐가 비었는지 확인
        if self.is_empty():
            raise IndexError("큐가 비었습니다.")
        self.front = (self.front + 1) % self.capacity
        item = self.items[self.front]
        self.items[self.front] = None
        return item
    
    def get_size(self):
        """현재 큐에 저장된 데이터의 개수를 반환"""
        return (self.rear - self.front + self.capacity) % self.capacity



T = int(input())
for tc in range(1, T+1):
    # N: 화덕의 크기, M: 피자의 개수
    N, M = map(int, input().split())
    # pizza[i]: i번 피자의 치즈의 양 (1 <= i <= M)
    # 인덱스 0은 사용하지 않는다.
    pizza = [0] + list(map(int, input().split()))

    # oven: 화덕, 원형 큐
    # 화덕에 있는 값은 피자의 번호(인덱스)를 의미한다.
    oven = CircularQueue(N)

    # 대기중인 피자의 가장 앞번호
    # (1번부터 M번까지 순서대로 화덕에 넣는다.)
    i = 1
    last_pizza = 0

    while sum(pizza) >= 0:
        # print(oven.items)
        # 초기 1회전은 순차적으로 대기중인 피자를 화덕에 넣는다.
        if i <= N:
            oven.enqueue(i)
            i += 1

        # 지금부터는 화덕이 가득 찬 상태
        # dequeue한 값의 절반을 다시 enqueue한다. 
        else:
            # 화덕에 남은 피자가 하나라면 반복을 종료한다.
            if oven.get_size() == 1:
                last_pizza = oven.dequeue()
                break

            # 현재 확인하고 있는 피자의 번호(인덱스)
            check = oven.dequeue()
            # 치즈의 양을 절반으로 변경한다.
            pizza[check] //= 2

            # 치즈가 녹지 않은 경우, 화덕에 입력된 값은 피자의 인덱스이므로 그대로 입력한다.
            if pizza[check] > 0:
                oven.enqueue(check)
            # 치즈가 모두 녹았고(값이 0) 대기중인 피자가 있다면, 대기중인 피자를 넣는다.
            elif i <= M:
                oven.enqueue(i)
                i += 1
            # 치즈는 모두 녹았는데 더이상 대기중인 피자가 없는 경우, dequeue한 상태로 둔다.
            else:
                continue
            
    
    print(f'#{tc} {last_pizza}')
# 연습문제. Queue
# 원형 큐 class 생성

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
        return self.items[self.front]
    
    
queue = CircularQueue(3)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.items)  # [None, 1, 2, 3]

print(queue.dequeue())  # 1
print(queue.dequeue())  # 2
print(queue.dequeue())  # 3
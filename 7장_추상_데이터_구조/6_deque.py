from queue import Queue


class Deque(Queue):
    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        return self.items.pop(0)


if __name__ == '__main__':
    deque = Deque()
    print(f"데크(Deque)가 비었나요? {deque.isEmpty()}")
    print("데크에 숫자 0~9를 추가합니다.")
    for i in range(10):
        deque.enqueue(i)
    print(f"데크 크기: {deque.size()}")
    print(f"peek: {deque.peek()}")
    print(f"dequeue: {deque.dequeue()}")
    print(f"peek: {deque.peek()}")
    print(f"데크가 비었나요? {deque.isEmpty()}")
    print(deque)

    print("\n데크 메서드를 사용합니다.")
    print(f"dequeue (앞): {deque.dequeue_front()}")
    print(f"peek: {deque.peek()}")
    print(deque)
    print("enqueue (뒤)를 수행합니다.")
    deque.enqueue_back(50)
    print(f"peek: {deque.peek()}")
    print(deque)
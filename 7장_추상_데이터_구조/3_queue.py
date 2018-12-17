class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def __repr__(self):
        return f"{self.items}"


if __name__ == "__main__":
    queue = Queue()
    print(f"큐가 비었나요? {queue.isEmpty()}")
    print("큐에 숫자 0~9를 추가합니다.")
    for i in range(10):
        queue.enqueue(i)
    print(f"큐 크기: {queue.size()}")
    print(f"peek: {queue.peek()}")
    print(f"dequeue: {queue.dequeue()}")
    print(f"peek: {queue.peek()}")
    print(f"큐가 비었나요? {queue.isEmpty()}")
    print(queue)
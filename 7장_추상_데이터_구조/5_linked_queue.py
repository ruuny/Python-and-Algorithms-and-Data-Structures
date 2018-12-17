class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = None


class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return not bool(self.head)

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            return value
        else:
            print("Queue is empty, cannot dequeue.")

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.pointer = node
            self.tail = node

    def size(self):
        node = self.head
        num_nodes = 0
        while node:
                num_nodes += 1
                node = node.pointer
        return num_nodes

    def peek(self):
        return self.head.value

    def _print(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()


if __name__ == "__main__":
    queue = LinkedQueue()
    print(f"큐가 비었나요? {queue.isEmpty()}")
    print("큐에 숫자 0~9를 추가합니다.")
    for i in range(10):
        queue.enqueue(i)
    print(f"큐가 비었나요? {queue.isEmpty()}")
    queue._print()

    print(f"큐 크기: {queue.size()}")
    print(f"peek: {queue.peek()}")
    print(f"dequeue: {queue.dequeue()}")
    print(f"peek: {queue.peek()}")
    queue._print()
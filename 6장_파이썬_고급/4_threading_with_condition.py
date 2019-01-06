import threading


def consumer(cond):
    name = threading.currentThread().getName()
    print(f"{name} 시작")
    with cond:
        print(f"{name} 대기")
        cond.wait()
        print(f"{name} 자원 소비")


def producer(cond):
    name = threading.currentThread().getName()
    print(f"{name} 시작")
    with cond:
        print(f"{name} 자원 생산 후 모든 소비자에게 알림")
        cond.notifyAll()


if __name__ == "__main__":
    condition = threading.Condition()
    consumer1 = threading.Thread(
        name="소비자1", target=consumer, args=(condition,))
    consumer2 = threading.Thread(
        name="소비자2", target=consumer, args=(condition,))
    producer = threading.Thread(name="생산자", target=producer, args=(condition,))

    consumer1.start()
    consumer2.start()
    producer.start()

from threading import Thread, Lock
import threading


def worker(mutex, data, thread_safe):
    if thread_safe:
        mutex.acquire()
    try:
        print(f"쓰레드 {threading.get_ident()}: {data}\n")
    finally:
        if thread_safe:
            mutex.release()


if __name__ == "__main__":
    threads = []
    thread_safe = True
    mutex = Lock()
    for i in range(20):
        t = Thread(target=worker, args=(mutex, i, thread_safe))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

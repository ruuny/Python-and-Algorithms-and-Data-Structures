"""
https://www.bogotobogo.com/python/Multithread/python_multithreading_Event_Objects_between_Threads.php
"""

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)s) %(message)s',)


def wait_for_event(event):
    logging.debug("wait_for_event 시작")
    event_is_set = event.wait()
    logging.debug("이벤트 셋: {0}".format(event_is_set))


def wait_for_event_timeout(event, t):
    while not event.isSet():
        logging.debug("wait_for_event_timeout 시작")
        event_is_set = event.wait(t)
        logging.debug("이벤트 셋: {0}".format(event_is_set))
        if event_is_set:
            logging.debug("이벤트 수행")
        else:
            logging.debug("다른 일 수행")


if __name__ == "__main__":
    event = threading.Event()
    t1 = threading.Thread(name="Blocking",
                          target=wait_for_event,
                          args=(event,))
    t1.start()

    t2 = threading.Thread(name="Non-Blocking",
                          target=wait_for_event_timeout,
                          args=(event, 2))
    t2.start()

    logging.debug("Event.set()이 호출될 때까지 대기")
    time.sleep(3)
    event.set()
    logging.debug("이벤트 설정됨")

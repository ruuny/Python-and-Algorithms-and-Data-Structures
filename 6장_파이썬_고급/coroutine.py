"""
[코딩도장] 코루틴 
https://dojang.io/mod/page/view.php?id=1122
"""


def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x)
    except GeneratorExit:
        print("종료")


def sum_coroutine():
    try:
        total = 0
        while True:
            x = (yield total)
            if x is None:
                return total  # raise StopIteration(total)
            total += x
    except RuntimeError as e:
        print(e)
        yield total


def accumulate():
    while True:
        total = yield from sum_coroutine()
        print(total)


if __name__ == "__main__":
    # 1
    co = number_coroutine()
    next(co)
    co.send(1)
    co.send(2)
    co.send(3)
    co.close()

    # 2
    sco = sum_coroutine()
    print(next(sco))
    print(sco.send(1))
    print(sco.send(2))
    print(sco.send(3))
    print(sco.throw(RuntimeError, "예외"))

    # 3
    aco = accumulate()
    next(aco)

    for i in range(11):
        aco.send(i)
    aco.send(None)

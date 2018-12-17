from functools import wraps


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


def fib(i):
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)


@memo
def fib2(i):
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)


if __name__ == "__main__":
    fibonacci = memo(fib)
    print(fibonacci(35))
    print(fib2(35))  # 데커레이터 사용

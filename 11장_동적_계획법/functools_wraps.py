# https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
from functools import wraps


def logged(func):
    def with_logging(*args, **kwargs):
        """with_logging() 함수"""
        print(func.__name__ + " 호출")
        return func(*args, **kwargs)
    return with_logging


@logged
def f(x):
    """첫 번째, 데커레이터 사용 """
    return x + x * x


def f2(x):
    """두 번째, 데커레이터 사용 X """
    return x + x * x


def logged2(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " 호출")
        return func(*args, **kwargs)
    return with_logging


@logged2
def f3(x):
    """세 번째, wraps와 데커레이터 사용 """
    return x + x * x


if __name__ == "__main__":
    print("결과: {0}".format(f(5)))
    print("__name__: {0}".format(f.__name__))
    print("__doc__: {0}".format(f.__doc__))
    print("-----------------------------")
    f2 = logged(f2)
    print("결과: {0}".format(f2(5)))
    print("__name__: {0}".format(f2.__name__))
    print("__doc__: {0}".format(f2.__doc__))
    print("-----------------------------")
    print("결과: {0}".format(f3(5)))
    print("__name__: {0}".format(f3.__name__))
    print("__doc__: {0}".format(f3.__doc__))

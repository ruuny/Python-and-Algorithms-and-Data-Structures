from itertools import combinations
from functools import wraps
from bisect import bisect

from timeit import timeit


# 단순 반복문
def naive_longest_inc_subseq(seq):
    for length in range(len(seq), 0, -1):
        for sub in combinations(seq, length):
            if list(sub) == sorted(sub):
                return len(sub)


# 동적 프로그래밍
def dp_longest_inc_subseq(seq):
    L = [1] * len(seq)
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1 + L[pre])
    return max(L)


# 메모이제이션
def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


def memoized_longest_inc_subseq(seq):
    @memo
    def L(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1 + L(pre))
        return res
    return max(L(i) for i in range(len(seq)))


# 이진 검색
def longest_inc_bisec(seq):
    end = []
    for val in seq:
        idx = bisect(end, val)
        if idx == len(end):
            end.append(val)
        else:
            end[idx] = val
    return len(end)


@timeit
def test_naive_longest_inc_subseq():
    print(naive_longest_inc_subseq(s1))


@timeit
def test_dp_longest_inc_subseq():
    print(dp_longest_inc_subseq(s1))


@timeit
def test_memoized_longest_inc_subseq():
    print(memoized_longest_inc_subseq(s1))


@timeit
def test_longest_inc_bisec():
    print(longest_inc_bisec(s1))


if __name__ == "__main__":
    from random import randrange
    s1 = [randrange(100) for i in range(20)]
    print(s1)
    test_naive_longest_inc_subseq()
    test_dp_longest_inc_subseq()
    test_memoized_longest_inc_subseq()
    test_longest_inc_bisec()

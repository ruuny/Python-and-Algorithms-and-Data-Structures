def quick_sort(seq):
    if len(seq) < 2:
        return seq
    ipivot = len(seq)//2
    pivot = seq[ipivot]
    before = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    after = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]
    return quick_sort(before) + [pivot] + quick_sort(after)


# 퀵 정렬을 두 함수로 나누어서 구현한다.
def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi


def quick_sort_divided(seq):
    if len(seq) < 2:
        return seq
    lo, pi, hi = partition(seq)
    return quick_sort_divided(lo) + [pi] + quick_sort_divided(hi)


# 퀵 정렬을 제자리 정렬로 구현한다(효율적이지 않다).
def quick_sort_in(seq):
    if len(seq) < 2:
        return seq
    if len(seq) == 2 and seq[0] > seq[1]:
        seq[0], seq[1] = seq[1], seq[0]
    pivot = seq[0]
    p1, p2 = 1, len(seq) - 1
    while p1 < p2:
        if seq[p1] <= pivot:
            seq[p1], seq[p2] = seq[p2], seq[p1]
            p2 -= 1
        else:
            p1 += 1
    seq[0], seq[p1] = seq[p1], pivot
    return quick_sort_in(seq[p1+1:]) + [seq[p1]] + quick_sort_in(seq[:p1])


def test_quick_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert(quick_sort(seq) == sorted(seq))
    assert(quick_sort_divided(seq) == sorted(seq))
    print('테스트 통과!')


if __name__ == "__main__":
    test_quick_sort()

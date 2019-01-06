def quick_sort_cache(seq):
    """
    1) 한 함수로 구현한다(캐시 사용).
    """
    if len(seq) < 2:
        return seq
    ipivot = len(seq) // 2  # 피벗 인덱스
    pivot = seq[ipivot]  # 피벗

    before = []
    after = []
    for i, x in enumerate(seq):
        if i != ipivot:
            if x <= pivot:
                before.append(x)
            else:
                after.append(x)
    # 위와 같지만 다음 코드는 seq에 대한 반복문을 두 번 실행한다.
    # before = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    # after = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]
    return quick_sort_cache(before) + [pivot] + quick_sort_cache(after)


def partition_devided(seq):
    """
    2) 1)의 퀵 정렬을 두 함수로 나누어 구현한다(캐시 사용).
    """
    pivot, seq = seq[0], seq[1:]
    before = []
    after = []
    for x in seq:
        if x <= pivot:
            before.append(x)
        else:
            after.append(x)
    # before = [x for x in seq if x <= pivot]
    # after = [x for x in seq if x > pivot]
    return before, pivot, after


def quick_sort_cache_devided(seq):
    if len(seq) < 2:
        return seq
    before, pivot, after = partition_devided(seq)
    return quick_sort_cache_devided(before) \
        + [pivot] \
        + quick_sort_cache_devided(after)


def partition(seq, start, end):
    """
    3) 두 함수로 나누어서 구현한다(캐시 사용 안함)
    """
    pivot = seq[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and seq[left] <= pivot:
            left += 1
        while left <= right and pivot < seq[right]:
            right -= 1
        if right < left:
            done = True
        else:
            seq[left], seq[right] = seq[right], seq[left]
    seq[start], seq[right] = seq[right], seq[start]
    # print(right, seq)
    return right


def quick_sort(seq, start, end):
    if start < end:
        pivot = partition(seq, start, end)
        quick_sort(seq, start, pivot - 1)
        quick_sort(seq, pivot + 1, end)
    return seq


def test_quick_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert(quick_sort_cache(seq) == sorted(seq))
    assert(quick_sort_cache_devided(seq) == sorted(seq))
    assert(quick_sort(seq, 0, len(seq)-1) == sorted(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_quick_sort()

import random


def quick_select_cache(seq, k):
    len_seq = len(seq)
    if len_seq < 2:
        return seq[0]

    # 피벗을 무작위로 선택할 수 있다.
    # pivot = random.choice(seq)
    ipivot = len_seq // 2
    pivot = seq[ipivot]

    smallerList = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    largerList = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]

    m = len(smallerList)
    if k == m:
        return pivot
    elif k < m:
        return quick_select_cache(smallerList, k)
    else:
        return quick_select_cache(largerList, k-m-1)


def swap(seq, x, y):
    seq[x], seq[y] = seq[y], seq[x]


def quick_select(seq, k, left=None, right=None):
    left = left or 0
    right = right or len(seq) - 1
    ipivot = random.randint(left, right)
    pivot = seq[ipivot]

    # 피벗을 정렬 범위 밖으로 이동한다.
    swap(seq, ipivot, right)
    swapIndex, i = left, left
    while i < right:
        if pivot < seq[i]:
            swap(seq, i, swapIndex)
            swapIndex += 1
        i += 1

    # 피벗 위치를 확정한다.
    swap(seq, right, swapIndex)

    # 피벗 위치를 확인한다.
    rank = len(seq) - swapIndex
    if k == rank:
        return seq[swapIndex]
    elif k < rank:
        return quick_select(seq, k, swapIndex+1, right)
    else:
        return quick_select(seq, k, left, swapIndex-1)


if __name__ == "__main__":
    seq = [3, 7, 2, 1, 4, 6, 5, 10, 9, 11]
    k = len(seq) // 2
    print(sorted(seq))
    print(quick_select_cache(seq, k-1))

    # 아래 함수는 원본을 수정하므로 깊은 복사 실행
    import copy
    seq_copy = copy.deepcopy(seq)
    print(quick_select(seq_copy, k))

    # 중앙값(median) 출력을 위해서 넘파이를 사용함
    import numpy
    print(numpy.median(seq))

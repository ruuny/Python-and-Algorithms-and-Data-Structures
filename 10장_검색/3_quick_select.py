import random


def quickSelect(seq, k):
    # 이 부분은 퀵 정렬과 같다.
    len_seq = len(seq)
    if len_seq < 2:
        return seq[0]
    # 피벗을 무작위로 선택할 수 있다.
    # pivot = random.choice(seq)
    ipivot = len_seq // 2
    pivot = seq[ipivot]

    smallerList = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    largerList = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]

    # 이 부분에서 퀵 정렬과 다르다.
    m = len(smallerList) + 1
    if k == m:
        return pivot
    elif k < m:
        return quickSelect(smallerList, k)
    else:
        return quickSelect(largerList, k-m-1)


if __name__ == "__main__":
    seq = [10, 60, 100, 50, 60, 75, 31, 50, 30, 20, 120, 170, 200]
    # seq = [3, 7, 2, 1, 4, 6, 5, 10, 9, 11]

    k = len(seq) // 2
    print(sorted(seq))
    print(quickSelect(seq, k))
    # 중앙값(median) 출력을 위해서 넘파이를 사용함
    import numpy
    print(numpy.median(seq))

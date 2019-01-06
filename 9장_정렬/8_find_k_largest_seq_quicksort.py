import random


def swap(A, x, y):
    A[x], A[y] = A[y], A[x]


def qselect(A, k, left=None, right=None):
    left = left or 0
    right = right or len(A) - 1
    pivot = random.randint(left, right)
    pivotVal = A[pivot]

    swap(A, pivot, right)
    swapIndex, i = left, left
    while i <= right - 1:
        if A[i] < pivotVal:
            swap(A, i, swapIndex)
            swapIndex += 1
        i += 1

    swap(A, right, swapIndex)
    rank = len(A) - swapIndex
    if k == rank:
        return A[swapIndex]
    elif k < rank:
        return qselect(A, k, left=swapIndex+1, right=right)
    else:
        return qselect(A, k, left=left, right=swapIndex-1)


def find_k_largest_seq_quickselect(seq, k):
    kth_largest = qselect(seq, k)
    result = []
    for item in seq:
        if item >= kth_largest:
            result.append(item)
    return result


if __name__ == "__main__":
    seq = [3, 10, 4, 5, 1, 8, 9, 11, 5]
    k = 3
    print(find_k_largest_seq_quickselect(seq, k))

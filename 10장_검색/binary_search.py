# 재귀함수
def binary_search_rec(seq, target, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    if target == seq[mid]:
        return mid
    elif target < seq[mid]:
        return binary_search_rec(seq, target, low, mid-1)
    else:
        return binary_search_rec(seq, target, mid+1, high)


# 반복문
def binary_search_iter(seq, target):
    high, low = len(seq), 0
    while low < high:
        mid = (high + low) // 2
        if target == seq[mid]:
            return mid
        elif target < seq[mid]:
            high = mid
        else:
            low = mid + 1
    return None

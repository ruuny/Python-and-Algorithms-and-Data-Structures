def ordered_sequential_search(seq, n):
    item = 0
    for item in seq:
        if item > n:
            return False
        if item == n:
            return True
    return False


def test_ordered_sequential_search():
    seq = [1, 2, 4, 5, 6, 8, 10]
    n1 = 10
    n2 = 7
    assert(ordered_sequential_search(seq, n1) is True)
    assert(ordered_sequential_search(seq, n2) is False)
    print("테스트 통과!")


if __name__ == "__main__":
    test_ordered_sequential_search()

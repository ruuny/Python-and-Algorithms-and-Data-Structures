def sequential_search(seq, n):
    for item in seq:
        if item == n:
            return True
    return False


def test_sequential_search():
    seq = [1, 5, 6, 8, 3]
    n1 = 5
    n2 = 7
    assert(sequential_search(seq, n1) is True)
    assert(sequential_search(seq, n2) is False)
    print("테스트 통과!")


if __name__ == "__main__":
    test_sequential_search()

def set_operations_with_dict():
    pairs = [("a", 1), ("b", 2), ("c", 3)]
    d1 = dict(pairs)
    print(f"딕셔너리1\t: {d1}")

    d2 = {"a": 1, "c": 2, "d": 3, "e": 4}
    print(f"딕셔너리2\t: {d2}")

    intersection = d1.keys() & d2.keys()
    print(f"d1 ∩ d2 (키)\t: {intersection}")

    intersection_items = d1.items() & d2.items()
    print(f"d1 ∩ d2 (키,값)\t: {intersection_items}")

    subtraction1 = d1.keys() - d2.keys()
    print(f"d1 - d2 (키)\t: {subtraction1}")

    subtraction2 = d2.keys() - d1.keys()
    print(f"d2 - d1 (키)\t: {subtraction2}")

    subtraction_items = d1.items() - d2.items()
    print(f"d1 - d2 (키,값)\t: {subtraction_items}")

    """ 딕셔너리의 특정 키를 제외한다. """
    d3 = {key: d2[key] for key in d2.keys() - {"c", "d"}}
    print(f"d2 - {{c, d}}\t: {d3}")


if __name__ == "__main__":
    set_operations_with_dict()

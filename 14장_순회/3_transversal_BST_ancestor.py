from transversal_BST_recursively import BSTwithTransversalRecursively


def find_ancestor(path, low_value, high_value):
    while path:
        current_value = path[0]
        if current_value < low_value:
            try:
                path = path[2:]
            except:
                return current_value
        elif current_value > high_value:
            try:
                path = path[1:]
            except:
                return current_value
        elif low_value <= current_value <= high_value:
            return current_value


if __name__ == "__main__":
    bst = BSTwithTransversalRecursively()
    l = [10, 5, 15, 1, 6, 11, 50]
    for i in l:
        bst.addNode(i)
    path = bst.preorder()
    print("중위 순회: ", path)

    print("1과 6의 최소 공통 조상 :", find_ancestor(path, 1, 6))
    print("1과 11의 최소 공통 조상: ", find_ancestor(path, 1, 11))
    print("11과 50의 최소 공통 조상: ", find_ancestor(path, 11, 50))
    print("5와 15의 최소 공통 조상: ", find_ancestor(path, 5, 15))

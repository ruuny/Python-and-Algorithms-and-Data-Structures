from transversal_BST_recursively import BSTwithTransversalRecursively


def find_ancestor(path, low_value, high_value):
    # 두 인수는 트리에 존재하는 노드여야 하며 두 번째 인수가 더 커야 한다.
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
    l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]
    for i in l:
        bst.add_node(i)
    path = bst.preorder()
    print("전위 순회: ", path)

    print("1과 6의 최소 공통 조상 :", find_ancestor(path, 1, 6))
    print("1과 11의 최소 공통 조상: ", find_ancestor(path, 1, 11))
    print("1과 4의 최소 공통 조상: ", find_ancestor(path, 1, 4))
    print("8와 9의 최소 공통 조상: ", find_ancestor(path, 8, 9))

from binary_tree import NodeBT, BinaryTree


class NodeBST(NodeBT):

    def __init__(self, item=None, level=0):
        self.item = item
        self.level = level
        self.left = None
        self.right = None

    def _addNextNode(self, value, level_here=1):
        new_node = NodeBST(value, level_here)
        if not self.item:
            self.item = new_node
        else:
            if value > self.item:
                self.right = self.right and self.right._addNextNode(
                    value, level_here+1) or new_node
            elif value < self.item:
                self.left = self.left and self.left._addNextNode(
                    value, level_here+1) or new_node
            else:
                print("중복 노드를 허용하지 않습니다.")
        return self

    def _searchForNode(self, value):
        if self.item == value:
            return self
        elif self.left and value < self.item:
            return self.left._searchForNode(value)
        elif self.right and value > self.item:
            return self.right._searchForNode(value)
        else:
            return False


class BinarySearchTree(BinaryTree):

    def __init__(self):
        self.root = None

    def addNode(self, value):
        if not self.root:
            self.root = NodeBST(value)
        else:
            self.root._addNextNode(value)


if __name__ == "__main__":
    bst = BinarySearchTree()
    for i in range(1, 10):
        bst.addNode(i)
    print("노드 8은 말단 노드입니까? ", bst.isLeaf(8))
    print("노드 8의 레벨은? ", bst.getNodeLevel(8))
    print("노드 10은 루트 노드입니까? ", bst.isRoot(10))
    print("노드 1은 루트 노드입니까? ", bst.isRoot(1))
    print("트리의 높이는? ", bst.getHeight())
    print("이진 탐색 트리입니까? ", bst.isBST())
    print("균형 트리입니까? ", bst.isBalanced())

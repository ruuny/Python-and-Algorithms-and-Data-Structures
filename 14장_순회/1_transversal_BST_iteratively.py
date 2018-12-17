from collections import deque
from binary_tree import BinaryTree, NodeBT


class BSTwithTransversalIterative(BinaryTree):

    def inorder(self):
        current = self.root
        nodes, stack = [], []
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                nodes.append(current.item)
                current = current.right
        return nodes

    def preorder(self):
        current = self.root
        nodes, stack = [], []
        while stack or current:
            if current:
                nodes.append(current.item)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        return nodes

    def preorder2(self):
        nodes = []
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current:
                nodes.append(current.item)
                stack.append(current.right)
                stack.append(current.left)
        return nodes

    def BFT(self):
        current = self.root
        nodes = []
        queue = deque()
        queue.append(current)
        while queue:
            current = queue.popleft()
            nodes.append(current.item)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return nodes


if __name__ == "__main__":
    bst = BSTwithTransversalIterative()
    l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]
    for i in l:
        bst.addNode(i)

    print("노드 8은 말단 노드입니까? ", bst.isLeaf(8))
    print("노드 8의 레벨은? ", bst.getNodeLevel(8))
    print("노드 10은 루트 노드입니까? ", bst.isRoot(10))
    print("노드 1은 루트 노드입니까? ", bst.isRoot(1))
    print("트리의 높이는? ", bst.getHeight())
    print("이진 탐색 트리입니까? ", bst.isBST())
    print("균형 트리입니까? ", bst.isBalanced())

    print("전위 순회: ", bst.preorder())
    print("전위 순회2: ", bst.preorder2())
    print("중위 순회: ", bst.inorder())
    print("너비 우선 탐색: ", bst.BFT())

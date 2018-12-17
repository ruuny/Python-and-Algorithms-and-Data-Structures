from binary_tree import BinaryTree, NodeBT


class BSTwithTransversalRecursively(BinaryTree):

    def __init__(self):
        self.root = None
        self.nodes_BFS = []
        self.nodes_pre = []
        self.nodes_post = []
        self.nodes_in = []

    def BFT(self):
        self.root.level = 0
        queue = [self.root]
        current_level = self.root.level

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.level > current_level:
                current_level += 1
            self.nodes_BFS.append(current_node.item)

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)

        return self.nodes_BFS

    def inorder(self, node=None, level=0):
        if not node and level == 0:
            node = self.root
        if node:
            self.inorder(node.left,  level+1)
            self.nodes_in.append(node.item)
            self.inorder(node.right, level+1)
        return self.nodes_in

    def preorder(self, node=None, level=0):
        if not node and level == 0:
            node = self.root
        if node:
            self.nodes_pre.append(node.item)
            self.preorder(node.left, level+1)
            self.preorder(node.right, level+1)
        return self.nodes_pre

    def postorder(self, node=None, level=0):
        if not node and level == 0:
            node = self.root
        if node:
            self.postorder(node.left,  level+1)
            self.postorder(node.right,  level+1)
            self.nodes_post.append(node.item)
        return self.nodes_post


if __name__ == "__main__":
    bst = BSTwithTransversalRecursively()
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
    print("후위 순회: ", bst.postorder())
    print("중위 순회: ", bst.inorder())
    print("너비 우선 탐색: ", bst.BFT())

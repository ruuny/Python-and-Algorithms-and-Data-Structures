from binary_search_tree import BinarySearchTree, NodeBST


class BSTwithTransversalRecursively(BinarySearchTree):

    def __init__(self):
        self.root = None
        self.nodes_BFS = []
        self.nodes_pre = []
        self.nodes_post = []
        self.nodes_in = []

    def BFT(self):
        self.root.level = 1
        queue = [self.root]
        current_level = self.root.level

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.level > current_level:
                current_level += 1
            self.nodes_BFS.append(current_node.value)

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
            self.nodes_in.append(node.value)
            self.inorder(node.right, level+1)
        return self.nodes_in

    def preorder(self, node=None, level=0):
        if not node and level == 0:
            node = self.root
        if node:
            self.nodes_pre.append(node.value)
            self.preorder(node.left, level+1)
            self.preorder(node.right, level+1)
        return self.nodes_pre

    def postorder(self, node=None, level=0):
        if not node and level == 0:
            node = self.root
        if node:
            self.postorder(node.left,  level+1)
            self.postorder(node.right,  level+1)
            self.nodes_post.append(node.value)
        return self.nodes_post

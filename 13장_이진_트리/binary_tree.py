class NodeBT(object):
    def __init__(self, item=None, level=0):
        self.item = item
        self.level = level
        self.left = None
        self.right = None

    def __repr__(self):
        return '{}'.format(self.item)

    def _addNextNode(self, value, level_here=1):
        new_node = NodeBT(value, level_here)
        if not self.item:
            self.item = new_node
        elif not self.left:
            self.left = new_node
        elif not self.right:
            self.right = new_node
        else:
            self.left = self.left._addNextNode(value, level_here+1)
        return self

    def _searchForNode(self, value):
        if self.item == value:
            return self
        else:
            found = None
            if self.left:
                found = self.left._searchForNode(value)
            if self.right:
                found = found or self.right._searchForNode(value)
            return found

    def _isLeaf(self):
        return not self.right and not self.left

    def _getMaxHeight(self):
        # 노드에서 최대 높이를 얻는다 - O(n)
        levelr, levell = 0, 0
        if self.right:
            levelr = self.right._getMaxHeight() + 1
        if self.left:
            levell = self.left._getMaxHeight() + 1
        return max(levelr, levell)

    def _getMinHeight(self, level=0):
        # 노드에서 최소 높이를 얻는다 - O(n)
        levelr, levell = -1, -1
        if self.right:
            levelr = self.right._getMinHeight(level + 1)
        if self.left:
            levell = self.left._getMinHeight(level + 1)
        return min(levelr, levell) + 1

    def _isBalanced(self):
        # 높이를 계산하여, 균형 트리인지 확인한다 - O(n^2)
        if self._getMaxHeight() - self._getMinHeight() < 2:
            return False
        else:
            if self._isLeaf():
                return True
            elif self.left and self.right:
                return self.left._isBalanced() and self.right._isBalanced()
            elif not self.left and self.right:
                return self.right._isBalanced()
            elif not self.right and self.left:
                return self.left._isBalanced()

    def _isBST(self, mintree=None, maxtree=None):
        # 중위 순회(inorder)로 이진 탐색 트리인지 확인한다.
        if self.item:
            if not mintree:
                mintree = self.item
            if not maxtree:
                maxtree = self.item

            if self._isLeaf():
                return True
            elif self.left:
                if self.left.item < self.item and mintree > self.left.item:
                    mintree = self.left.item
                    return self.left._isBST(mintree, maxtree)
                else:
                    return False
            elif self.right:
                if self.right.item > self.item and maxtree < self.right.item:
                    maxtree = self.right.item
                    return self.right._isBST(mintree, maxtree)
                else:
                    return False
        else:
            print('빈 트리입니다.')


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def addNode(self, value):
        if not self.root:
            self.root = NodeBT(value)
        else:
            self.root._addNextNode(value)

    def isLeaf(self, value):
        node = self.root._searchForNode(value)
        return node._isLeaf()

    def getNodeLevel(self, item):
        node = self.root._searchForNode(item)
        if node:
            return node.level
        else:
            raise Exception('노드를 찾을 수 없습니다.')

    def isRoot(self, value):
        return self.root.item == value

    def getHeight(self):
        return self.root._getMaxHeight()

    def isBalanced(self):
        return self.root._isBalanced()

    def isBST(self):
        return self.root._isBST()

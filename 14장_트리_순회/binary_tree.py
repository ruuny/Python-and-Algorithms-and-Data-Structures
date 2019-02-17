class Height(object):
    def __init__(self):
        self.height = 0


class NodeBT(object):
    def __init__(self, value=None, level=1):
        self.value = value
        self.level = level
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.value)

    def _add_next_node(self, value, level_here=2):
        new_node = NodeBT(value, level_here)
        if not self.value:
            self.value = new_node
        elif not self.left:
            self.left = new_node
        elif not self.right:
            self.right = new_node
        else:
            self.left = self.left._add_next_node(value, level_here+1)
        return self

    def _search_for_node(self, value):
        if self.value == value:
            return self
        else:
            found = None
            if self.left:
                found = self.left._search_for_node(value)
            if self.right:
                found = found or self.right._search_for_node(value)
            return found

    def _is_leaf(self):
        return not self.right and not self.left

    def _get_max_height(self):
        # 노드에서 최대 높이를 얻는다 - O(n)
        l, r = 0, 0
        if self.left:
            l = self.left._get_max_height() + 1
        if self.right:
            r = self.right._get_max_height() + 1

        return max(l, r)

    def _is_balanced(self, height=Height()):
        # 균형 트리인지 확인한다 - O(n)
        lh = Height()
        rh = Height()

        if self.value is None:
            return True

        l, r = True, True
        if self.left:
            l = self.left._is_balanced(lh)
        if self.right:
            r = self.right._is_balanced(rh)

        height.height = max(lh.height, rh.height) + 1

        if abs(lh.height - rh.height) <= 1:
            return l and r

        return False

    def _is_bst(self, left=None, right=None):
        # 이진 탐색 트리인지 확인한다 - O(n)
        if self.value:
            if left and self.value < left:
                return False
            if right and self.value > right:
                return False

            l, r = True, True
            if self.left:
                l = self.left._is_bst(left, self.value)
            if self.right:
                r = self.right._is_bst(self.value, right)
            return l and r
        else:
            return True


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def add_node(self, value):
        if not self.root:
            self.root = NodeBT(value)
        else:
            self.root._add_next_node(value)

    def is_leaf(self, value):
        node = self.root._search_for_node(value)
        if node:
            return node._is_leaf()
        else:
            return False

    def get_node_level(self, value):
        node = self.root._search_for_node(value)
        if node:
            return node.level
        else:
            return False

    def is_root(self, value):
        return self.root.value == value

    def get_height(self):
        return self.root._get_max_height()

    def is_balanced(self):
        return self.root._is_balanced()

    def is_bst(self):
        return self.root._is_bst()

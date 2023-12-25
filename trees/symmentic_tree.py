# https://leetcode.com/problems/symmetric-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def insert_binary_tree_node(_arr, i, _n):
    _root = None
    if i < _n:
        _root = TreeNode(_arr[i])
        """
        we just calculate level wise node, cuz every binary tree's node has only 2 adjacency node.
        """
        _root.left = insert_binary_tree_node(_arr, 2 * i + 1, _n)
        _root.right = insert_binary_tree_node(_arr, 2 * i + 2, _n)
    return _root


def in_order_tree(_root):
    if _root.left:
        in_order_tree(_root.left)
    print(_root.val)
    if _root.right:
        in_order_tree(_root.right)


class Solution:
    def isSymmetric(self, _root) -> bool:
        return self.is_mirror(_root, _root)

    def is_mirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (t1.val == t2.val) and self.is_mirror(t1.right, t2.left) and self.is_mirror(t1.left, t2.right)


arr = [1, 2, 2, 3, 4, 4, 3]
n = len(arr)
root = insert_binary_tree_node(arr, 0, n)
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.right = TreeNode(None)
# root.right.right = TreeNode(3)
# in_order_tree(root)

s = Solution()
print(s.isSymmetric(root))

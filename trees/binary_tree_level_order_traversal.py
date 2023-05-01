# https://leetcode.com/problems/binary-tree-level-order-traversal/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def insert_binary_tree_node(arr, i, n):
    root = None
    if i < n:
        root = TreeNode(arr[i])
        """
        we just calculate level wise node, cuz every binary tree's node has only 2 adjacency node.
        """
        root.left = insert_binary_tree_node(arr, 2 * i + 1, n)
        root.right = insert_binary_tree_node(arr, 2 * i + 2, n)
    return root


def in_order_tree(_root):
    if _root.left:
        in_order_tree(_root.left)
    print(_root.val)
    if _root.right:
        in_order_tree(_root.right)


class Solution:
    def levelOrder(self, root) -> list:
        if root is None:
            return []
        arr = list()
        level = []
        queue = [root]
        next_queue = []
        while queue:
            for node in queue:
                if node.val is not None:
                    level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            arr.append(level)
            queue = next_queue
            next_queue = []
            level = []
        return arr


# arr = [3, 9, 20, None, None, 15, 7]
# arr = [1]
# arr = [1, 2, 3, 4, None, None, 5]
# arr = [3,9,20,None,None,15,7]
arr = [1, 2, 3, 4, None, None, 5]
n = len(arr)
root = insert_binary_tree_node(arr, 0, n)
# print(in_order_tree(root))
s = Solution()
print(s.levelOrder(root))



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def insert_data(root, data):
    if root:
        if data < root.val:
            if root.left is None:
                root.left = TreeNode(data)
            else:
                insert_data(root.left, data)
        elif data > root.val:
            if root.right is None:
                root.right = TreeNode(data)
            else:
                insert_data(root.right, data)


def in_order_tree(_root):
    if _root.left:
        in_order_tree(_root.left)
    print(_root.val)
    if _root.right:
        in_order_tree(_root.right)


root = TreeNode(10)
for i in [5, 6, 7, 8, 4, 33, 44]:
    insert_data(root, i)


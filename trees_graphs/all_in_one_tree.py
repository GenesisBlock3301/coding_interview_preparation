# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order(root):
    if root:
        print(root.val,end=" ")
        pre_order(root.left)
        pre_order(root.right)


def in_order(root):
    if root:
        in_order(root.left)
        print(root.val,end=" ")
        in_order(root.right)


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val,end=" ")


root = TreeNode(10)
five = TreeNode(5)
twenty = TreeNode(20)
three = TreeNode(3)
seven = TreeNode(7)
thirty = TreeNode(30)
root.left = five
root.right = twenty
root.left.left = three
root.left.right = seven
root.right.right = thirty
print("Pre order")
pre_order(root)
print("\n")
print("In order: ")
in_order(root)
print("\n")
print("Post order")
post_order(root)
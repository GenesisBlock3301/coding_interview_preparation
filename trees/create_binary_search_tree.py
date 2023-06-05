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
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
def sortedArrayToBST(nums):
    divide_array(nums)

def divide_array(nums):
    if len(nums) == 1:
        return TreeNode(nums[0])
    if len(nums) == 0:
        return  None

    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = divide_array(nums[:mid])
    root.right = divide_array(nums[mid+1:])
    return root





nums = [-10,-3,0,5,9]
# [0,-3,9,-10,null,5]
print(sortedArrayToBST(nums))
# root = TreeNode(4)
# insert_data(root, 2)
# insert_data(root, 5)
# insert_data(root, 1)
# insert_data(root, 3)
# insert_data(root, 6)
# print(root)
# print(root.left)
# print(root.right)
# print(root.left.left)
# print(root.left.right)
# print(root.right.right)


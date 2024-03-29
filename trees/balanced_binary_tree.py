# https://leetcode.com/problems/balanced-binary-tree/

# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def preorder(self, root):
        if root:
            print(root.val, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def insert(self, data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data


r1 = [4, 2, 7, 1, 3, 6, 9]
# root = TreeNode()
# root.insert


root = TreeNode(r1[0])
for i in r1[1:]:
    root.insert(i)

# root.preorder(root)
print(root.maximum_depth(root))

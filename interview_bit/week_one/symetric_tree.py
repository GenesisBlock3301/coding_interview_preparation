# https://www.interviewbit.com/problems/symmetric-binary-tree/?study_plan=study-plan-3-months&/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        return self.symmetric_tree(A, A)

    def symmetric_tree(self, t1, t2):
        if t1 is None and t2 is None:
            return 1
        if t1 is None or t2 is None:
            return 0
        answer = t1.val == t2.val and self.symmetric_tree(t1.left, t2.right) and self.symmetric_tree(t1.right, t2.left)
        return 1 if answer else 0


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)

s = Solution()
print(s.isSymmetric(root))
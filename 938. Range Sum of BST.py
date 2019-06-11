# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        if root == None:
            return 0
        sum = 0
        if root.val < L:
            sum += self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            sum += self.rangeSumBST(root.left, L, R)
        elif root.val >= L and root.val <= R:
            sum += root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        return sum
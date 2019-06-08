# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        def LDR(root):
            if root == None:
                return 0
            return max(LDR(root.left), LDR(root.right)) + 1
        
        return LDR(root)
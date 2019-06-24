# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(root, val):
            if root == None:
                return True
            if root.val != val:
                return False
            elif root.val == val:
                return dfs(root.left, val) and dfs(root.right, val)
        
        return dfs(root, root.val)
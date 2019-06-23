"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        
        ans = []
        ans.append(root.val)
        for tree in root.children:
            ans.extend(self.preorder(tree))
        return ans
'''
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
'''
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        
        ans = []
        for tree in root.children:
            ans.extend(self.postorder(tree))
        ans.append(root.val)
        return ans
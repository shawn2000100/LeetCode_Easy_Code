# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        def DLR(root, leaf_list):
            if root == None:
                return
            elif root.left == None and root.right == None:
                leaf_list.append(root.val)
            else:
                DLR(root.left, leaf_list)
                DLR(root.right, leaf_list)
        
        leaf_val_1 = list()
        leaf_val_2 = list()
        DLR(root1, leaf_val_1)
        DLR(root2, leaf_val_2)
        
        if leaf_val_1 == leaf_val_2:
            return True
        else:
            return False
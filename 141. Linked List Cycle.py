# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        pre = cur = head
        while cur != None and cur.next != None:
            pre = pre.next
            cur = cur.next.next
            if cur == pre:
                return True
        return False

        


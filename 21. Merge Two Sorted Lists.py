class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, L1, L2):
        ptr1, ptr2 = L1, L2
        ans = []
        while ptr1:
            ans.append(ptr1.val)
            ptr1 = ptr1.next
        while ptr2:
            ans.append(ptr2.val)
            ptr2 = ptr2.next
        return sorted(ans)

# 本機端測試用
L1 = ListNode(1)
L1.next = ListNode(2)
L1.next.next = ListNode(4)
L2 = ListNode(1)
L2.next = ListNode(3)
L2.next.next = ListNode(4)

sol = Solution()
print(sol.mergeTwoLists(L1, L2))
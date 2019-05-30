class Solution:
    def searchInsert(self, List, target):
        ret_idx = len(List)
        for i in range(len(List)):
            if target <= List[i]:
                return i
        return ret_idx
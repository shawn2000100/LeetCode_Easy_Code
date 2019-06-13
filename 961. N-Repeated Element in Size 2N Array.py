class Solution:
    def repeatedNTimes(self, A):
        count = {}
        for i in A:
            if i not in count:
                count[i] = 1
            else:
                return i
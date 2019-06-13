class Solution:
    def sortArrayByParity(self, A):
        even, odd = [], []
        for i in A:
            if i & 1:
                odd.append(i)
            else:
                even.append(i)
        return even + odd
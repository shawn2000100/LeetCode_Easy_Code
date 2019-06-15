class Solution:
    def hammingDistance(self, x, y):
        res = bin(x ^ y)        
        return res.count('1')
class Solution:
    def numJewelsInStones(self, J, S):
        ans = 0
        for i in S:
            if i in J:
               ans += 1
        return ans
class Solution:
    def diStringMatch(self, S):
        low, hig = 0, len(S)
        ans = []
        for c in S:
            if c == 'I':
                ans.append(low)
                low += 1
            elif c == 'D':
                ans.append(hig)
                hig -= 1
                
        ans.append(low)
        return ans
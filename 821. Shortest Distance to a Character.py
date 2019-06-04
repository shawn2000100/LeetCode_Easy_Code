class Solution(object):
    def shortestToChar(self, S, C):
        n = len(S)
        ans = [0 for i in range(n)]
        
        idx = []
        for i in range(n):
            if S[i] == C:
                idx.append(i)
        
        for i in range(n):
            if S[i] != C:
                min_dist = 0x3f3f3f3f
                for j in idx:
                    min_dist = min(min_dist, abs(j - i))
                ans[i] = min_dist
        return ans
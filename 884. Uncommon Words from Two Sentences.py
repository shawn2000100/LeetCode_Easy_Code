class Solution:
    def uncommonFromSentences(self, A, B):
        A, B = A.split(), B.split()
        cnt = {}
        for a in A:
            if a not in cnt:
                cnt[a] = 1
            else:
                cnt[a] += 1
        for b in B:
            if b not in cnt:
                cnt[b] = 1
            else:
                cnt[b] += 1
        
        ans = []
        for i in cnt:
            if cnt[i] == 1:
                ans.append(i)
        
        return ans
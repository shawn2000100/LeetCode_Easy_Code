from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        m, n = len(s), len(p)
        if m < n:
            return []
        
        ans = []
        pCounter = Counter(p) # 目標比對字串
        sCounter = Counter(s[:n-1]) # 滑動窗口字串，前n-1個字元加進窗口，之後再慢慢往右加一
        
        for i in range(n-1, m):
            sCounter[s[i]] += 1 # 向右增加一個字元
            if sCounter == pCounter:
                ans.append(i - n + 1) # i向左n個字元長度再+1回來就是答案的起始index了
            
            sCounter[s[i - n + 1]] -= 1 # 最左邊刪掉一個字元，統計數-1
            if sCounter[s[i - n + 1]] == 0: #頻率為0，必須刪除。否則{‘a’: 0, ‘b’: 1}) != {‘b’: 1}
                 del sCounter[s[i - n + 1]]
        
        return ans
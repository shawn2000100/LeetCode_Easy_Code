class Solution:
    def removeOuterParentheses(self, S):
        s = []
        ans = ''
        for c in S:
            if c == '(':
                s.append(c)
                if len(s) > 1:
                    ans += c        
            elif c == ')':
                if len(s) > 1:
                    ans += c
                s.pop()
        return ans
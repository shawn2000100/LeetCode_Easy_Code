class Solution(object):
    def reverseString(self, s):
        n = len(s)
        for i in range(0, n/2):
            s[i], s[n-1-i] = s[n-1-i], s[i]
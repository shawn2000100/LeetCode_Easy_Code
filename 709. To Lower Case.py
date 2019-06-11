class Solution:
    def toLowerCase(self, str):
        A = ord('A')
        Z = ord('Z')
        dif = ord('a') - ord('A')
        ans = ''
        for c in str:
            val = ord(c)
            if val >= A and val <= Z:
                ans += chr(val + dif)
            else:
                ans += c
        return ans
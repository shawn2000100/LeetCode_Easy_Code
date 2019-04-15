class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0

        index = -1
        for i in range( len(haystack) - len(needle) + 1 ):
            for j in range( len(needle) ):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    index = i

            if index != -1:
                break

        return index
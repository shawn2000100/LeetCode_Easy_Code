'''
用迴圈慢慢比對即可，記得處理輸入字串為空的情形，算是一個小坑
'''


class Solution:
    def longestCommonPrefix(self, strs):
        # empty input
        if strs == []:
            return ""

        len_of_string = []
        for i in strs:
            len_of_string.append(len(i))
        min_len = min(len_of_string)

        prefix = ""
        for i in range(min_len):
            equal = True
            new_prefix = strs[0][i]
            for s in strs:
                if s[i] != new_prefix:
                    equal = False
                    break
            if not equal:
                break
            else:
                prefix += new_prefix

        return  prefix

# 本機端測試用
# sol = Solution()
# print(sol.longestCommonPrefix(["dog","racecar","car"]))
# print(sol.longestCommonPrefix(["flower","flow","flight"]))

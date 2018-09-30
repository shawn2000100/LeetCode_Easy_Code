class Solution:
    def isValid(self, s):
        map = {'(':')', '[':']', '{':'}'}
        stack = []
        for i in s:
            if i in map.keys():
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif i != map[stack.pop()]:
                    return False

        return True if len(stack) == 0 else False


# 本機端測試用
# sol = Solution()
# print(sol.isValid("()[]{}"))
# print(sol.isValid("([{}])"))
# print(sol.isValid(""))

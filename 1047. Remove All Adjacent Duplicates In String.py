class Solution(object):
    def removeDuplicates(self, S):
        stack = []
        for c in S:
            if stack and stack[-1] == c:
                stack.pop(-1)
                continue
            stack.append(c)
        return ''.join(stack)
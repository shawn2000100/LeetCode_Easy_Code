class Solution(object):
    def calPoints(self, ops):
        s = []
        for i in ops:
            if i == '+':
                score = s[-2] + s[-1]
                s.append(score)
            elif i == 'D':
                score = s[-1] * 2
                s.append(score)
            elif i == 'C':
                s.pop()
            else:
                s.append(int(i))
        return sum(s)
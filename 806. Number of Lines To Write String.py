class Solution(object):
    def numberOfLines(self, widths, S):
        width_used, line_used = 0, 1
        for c in S:
            w = widths[ord(c) - ord('a')] 
            width_used += w
            if width_used > 100:
                line_used += 1
                width_used = w
        return [line_used, width_used]
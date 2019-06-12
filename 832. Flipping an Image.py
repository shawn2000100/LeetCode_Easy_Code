class Solution:
    def flipAndInvertImage(self, A):
        ans = []
        for row in A:
            row.reverse()
            ans.append(row)
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                ans[i][j] = ans[i][j] ^ 1
        return ans
class Solution:
    def minDeletionSize(self, A):
        row, col = len(A), len(A[0])
        ans = 0
        for j in range(col):
            for i in range(1, row):
                if A[i][j] < A[i - 1][j]:
                    ans += 1
                    break
        return ans
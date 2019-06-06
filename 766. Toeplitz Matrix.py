class Solution:
    def isToeplitzMatrix(self, matrix):
        r_c = {}
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i - j not in r_c:
                    r_c[i - j] = matrix[i][j]
                elif r_c[i - j] != matrix[i][j]:
                    return False
        return True
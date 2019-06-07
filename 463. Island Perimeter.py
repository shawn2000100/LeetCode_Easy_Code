class Solution:
    def islandPerimeter(self, grid):
        sum = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if j == 0 or grid[i][j-1] == 0:
                    sum += 1
                if j == n-1 or grid[i][j+1] == 0:
                    sum += 1
                if i == 0 or grid[i-1][j] == 0:
                    sum += 1
                if i == m-1 or grid[i+1][j] == 0:
                    sum += 1
        return sum
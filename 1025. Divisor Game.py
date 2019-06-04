class Solution(object):
    def divisorGame(self, N):
        result = [False for i in range(1001)]
        result[2] = True
        for n in range(4, N+1):
            for x in range(1, n):
                if n % x == 0 and result[n - x] == False:
                    result[n] = True
                    break
        return result[N]
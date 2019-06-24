class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        
        a, b, c = 0, 1, None
        for i in range(2, N+1):
            c = a + b
            a = b
            b = c
        return c
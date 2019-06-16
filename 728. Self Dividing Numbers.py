class Solution:
    # 法二
    def selfDividingNumbers(self, left, right):
        def is_self_dividing(n):
            for d in str(n):
                if d == '0' or n % int(d) != 0:
                    return False
            return True
        
        ans = []
        for n in range(left, right + 1):
            if is_self_dividing(n):
                ans.append(n)
        return ans
    
#     # 法一
#     def selfDividingNumbers(self, left, right):
#         ans = []
#         for i in range(left, right + 1):
#             fit = True
#             tmp = i
#             while tmp:
#                 digit = tmp % 10
#                 if digit == 0:
#                     fit = False
#                     break
#                 if i % digit != 0:
#                     fit = False
#                 tmp //= 10
                
#             if fit:
#                 ans.append(i)
        
#         return ans
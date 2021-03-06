'''
有兩種解法：
1. 比較傳統的方法是逐次%10來取最右邊的位數，接著判斷反轉後的數值是否溢位(超出-2147483648 ~ +2147483647)，
但這樣子做稍微多花一些時間(多次的除法跟餘數運算)

2. 用字串的型態來儲存輸入，接著反轉，由於python本身支援大數運算，故只需把反轉後的字串轉為int型態後再判斷值域即可
'''

class Solution:
    def reverse(self, x):
        # 將int轉為str, 接著reverse, 再轉回int
        sign = 1 if x > 0 else -1
        x = int (str(abs(x))[::-1])
        # 如果x超出4byte整數的值域
        if not (x >= -2147483648 and x <= +2147483647):
            x = 0

        return sign * x

# 本機端測試用
# sol = Solution()
# print(sol.reverse(-214647))

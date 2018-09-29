'''
經典題型，經典的教科書解法是利用stack跟迴圈做前後的比對來判斷迴文，這邊為了精簡，我則是使用字串reverse的方式來做比對
'''

class Solution:
    def isPalindrome(self, x):
        return True if str(x) == str(x)[::-1] else False # Note：這題似乎一定要返回Bool值，直接回傳字串會ＷＡ

# 本機端測試用
# sol = Solution()
# print(sol.isPalindrome(121))

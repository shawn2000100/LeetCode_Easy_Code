'''
思考：
  如果直接使用雙層迴圈做查找，時間複雜度為O(N^2), 非常沒有效率。
於是使用字典(Hash)來當作資料結構，降低查找的時間，藉由此方法可將時間複雜度壓縮至O(N)

注意：each input would have exactly one solution 這敘述，我們確定剛好有唯一解才能用這種方法，否則遇到([3, 3, 3, 2], 5)這種測資的話可能會有問題
'''

class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, val in enumerate(nums):
           # 兩數相加 = Target, 故我們使用一個diff變數來紀錄下一個要查找的目標
           diff = target - val
           # 這一步有點類似說，向過往的紀錄查找，要是以前有存到這麼一個值，就return它
           # Note: 不能先儲存dic[val]後才比對diff，因為如果遇到同樣數值的input，上一個index會被蓋掉
           if diff in dic:
             return [dic[diff], i]
           dic[val] = i

# 本機端測試用
# sol = Solution()
# print(sol.twoSum([3, 3, 3, 2], 5))

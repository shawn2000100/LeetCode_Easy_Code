class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        ans = 1
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                ans += 1
                index += 1
                nums[index] = nums[i]

        for i in range(ans, len(nums)):
            nums.pop()

        return ans

# 本機端測試用
sol = Solution()
nums = [1, 1, 2, 2]
print(sol.removeDuplicates(nums))
print(nums)
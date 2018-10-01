class Solution:
    def removeElement(self, nums, val):
        ans = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ans] = nums[i]
                ans += 1

        return ans

# 本機端測試用
sol = Solution()
nums = [0,1,2,2,3,0,4,2]
print(sol.removeElement(nums, 2))
print(nums)
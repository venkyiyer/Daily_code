class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                return [i, d[diff]]
            d[nums[i]] = i

obj = Solution()
print(obj.twoSum(nums = [3,2,4], target = 6))
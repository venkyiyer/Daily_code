nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                return i, d[diff]
            d[nums[i]] = i
    
obj = Solution()
print(obj.twoSum(nums, target))
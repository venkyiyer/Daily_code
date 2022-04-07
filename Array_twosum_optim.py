class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i,num in enumerate(nums):
            if target-num in d:
                return d[target-num], i
            d[num]=i

obj = Solution()
print(obj.twoSum([2,7,11,15], 9))
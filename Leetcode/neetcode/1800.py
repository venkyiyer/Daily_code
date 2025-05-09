class Solution:
    def maxAscendingSum(self, nums):
        current = nums[0]
        res = current
        for i in range(1,len(nums)):
            if not(nums[i-1] < nums[i]):
                current = 0
            current += nums[i]
            res = max(res, current)
        
        return res

obj = Solution()
print(obj.maxAscendingSum([10,20,30,5,10,50]))
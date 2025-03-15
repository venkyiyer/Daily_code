nums = [-1,1,-1,1,-1]

class Solution:
    def arraySign(self, nums):
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
        
        if prod == 0:
            return 0
        elif prod > 1:
            return 1
        else:
            return -1

obj = Solution()
print(obj.arraySign(nums))
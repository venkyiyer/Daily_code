class Solution:
    def missingNumber(self,nums):
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        
        return len(nums)

obj = Solution()
print(obj.missingNumber([9,6,4,2,3,5,7,0,1]))
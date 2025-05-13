class Solution:
    def isArraySpecial(self, nums):
        if len(nums)==1:
            return True
        for i in range(len(nums)-1):
            if nums[i]%2 == 0 and nums[i+1]%2!=0:
                continue
            elif nums[i]%2 != 0 and nums[i+1]%2 == 0:
                continue 
            else:
                return False
        
        return True

obj = Solution()
print(obj.isArraySpecial([1]))
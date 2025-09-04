class Solution:
    def moveZeros(self, nums):
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1
        
        return nums

obj = Solution()
print(obj.moveZeros([0,1,0,3,12]))
        
        
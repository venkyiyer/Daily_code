class Solution:
    def sortArrayByParity(self, nums):
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[l] , nums[r] = nums[r], nums[l]
                l +=1
        
        return nums
    
obj = Solution()
print(obj.sortArrayByParity([3,1,2,4]))
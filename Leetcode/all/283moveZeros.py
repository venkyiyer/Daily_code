class Solution:
    def moveZeros(self, nums):
        left = 0
        for right in range(len(nums)):
            if nums[right] !=0:
                nums[right], nums[left] = nums[left], nums[right]
                left +=1
        return nums

obj = Solution()
print(obj.moveZeros([0,1,0,3,12]))
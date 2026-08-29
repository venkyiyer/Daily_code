class Solution:
    def removeElement(self, nums, val):
        k = len(nums)

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = '_'
                k -= 1
        
        return k, nums

obj = Solution()
print(obj.removeElement([0,1,2,2,3,0,4,2], 2))
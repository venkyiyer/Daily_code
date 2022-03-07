class Solution:
    def removeElement(self, nums, val):
        while val in nums:
                nums.remove(val)
        return len(nums), nums

obj = Solution()
print(obj.removeElement([0,1,2,2,3,0,4,2], 2))
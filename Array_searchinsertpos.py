class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            k = nums[i]
            if nums[i] == target:
                return i
            if k > target:
                l = i
                return l
            else:
                l = len(nums)
        return l         
obj = Solution()
print(obj.searchInsert([1,3,5,6], 2))
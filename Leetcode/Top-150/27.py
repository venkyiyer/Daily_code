class Solution:
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = '_'
            else:
                count += 1

        return count, sorted(nums)

obj = Solution()
print(obj.removeElement([0,1,2,2,3,0,4,2], 2))
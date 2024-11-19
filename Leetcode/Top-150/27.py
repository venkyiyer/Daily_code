class Solution:
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count +=1

        return count

obj = Solution()
print(obj.removeElement([2,2,3,3], 2))
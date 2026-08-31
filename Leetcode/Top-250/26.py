class Solution:
    def removeDuplicates(self, nums):
        l , r = 1, 1
        while r < len(nums):
            if nums[r] == nums[r-1]:
                r +=1
            else:
                nums[l] = nums[r]
                l +=1
                r+=1

        return nums

obj = Solution()
print(obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
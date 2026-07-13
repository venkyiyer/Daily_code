class Solution:
    def removeDuplicates(self, nums):
        left = 1 
        right = 2
        while left < right and right<=len(nums)-1:
            if nums[left-1] == nums[right]:
                pass
            else:
                nums[left] = nums[right]
                left += 1
            right +=1
        return left-1

obj= Solution()
print(obj.removeDuplicates(nums = [1,1,2]))
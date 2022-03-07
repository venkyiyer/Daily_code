import numbers


class Solution:
    def removeDuplicates(self, nums):
        k = 0
        for index in range(1,len(nums)):
            if(nums[index] != nums[index-1]):
                k+=1
                nums[k] = nums[index]
        return k+1

obj = Solution()
print(obj.removeDuplicates([0,0,1,1,1,2,3,3,4,4,5,5]))
nums = [1,1,1,1]

class Solution:
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count+=1
        
        return count
    
obj = Solution()
print(obj.numIdenticalPairs(nums))

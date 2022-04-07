class Solution:
    def majorityElement(self, nums):
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)-1):
                if nums[i] == nums[j]:
                    count +=1
                return count

obj = Solution()
print(obj.majorityElement([2,2,1,1,1,2,2]))
class Solution:
    def majorityElement(self, nums):
        result, count = 0, 0

        for i in nums:
            if count == 0:
                result = i
            count += (1 if i == result else -1)
        return result
    
obj = Solution()
print(obj.majorityElement([2,2,1,1,1,2,2]))
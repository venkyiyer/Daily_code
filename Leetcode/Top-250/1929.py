class Solution: 
    def getConctenation(self, nums):
        nums.extend(nums)
        
        return nums
        
obj = Solution()
print(obj.getConctenation([1,3,2,1]))
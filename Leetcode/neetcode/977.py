nums = [-4,-1,0,3,10]

class Solution:
    def sortedSquares(self, nums):
        return sorted(i*i for i in nums)

obj = Solution()
print(obj.sortedSquares(nums))
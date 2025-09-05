class Solution:
    def sortedSquares(self, nums):
        return sorted([x*x for x in nums])
    

obj = Solution()
print(obj.sortedSquares([-4,-1,0,3,10]))
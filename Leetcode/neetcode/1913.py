nums = [4,2,5,9,7,4,8]

class Solution:
    def maxProductDifference(self, nums):
        sortedNums = sorted(nums)
        return sortedNums[-1]*sortedNums[-2] - sortedNums[0]*sortedNums[1]

obj = Solution()
print(obj.maxProductDifference(nums))
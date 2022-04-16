class Solution:
    def missingNumber(self, nums):
        length = len(nums)
        actualsum = length*(length+1)/2
        listsum = sum(nums)
        diff = actualsum - listsum

        return int(diff)

obj = Solution()
print(obj.missingNumber([3,0,1]))       
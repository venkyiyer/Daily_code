class Solution:
    def concate(self, nums):
        nums.extend(nums)
        return nums

obj = Solution()
print(obj.concate(nums=[1,2,1]))
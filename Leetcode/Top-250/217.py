class Solution:
    def containsDuplicate(self, nums):
       return len(set(nums))!=len(nums)

obj = Solution()
print(obj.containsDuplicate([[1,1,1,3,3,4,3,2,4,2]]))

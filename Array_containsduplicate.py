class Solution:
    def containsDuplicate(self, nums):
         hashNum = {}
         for i in nums:
          if i not in hashNum:
             hashNum[i] = 1
          else:
              return True
         return False  

obj = Solution()
print(obj.containsDuplicate([1,2, 3, 4]))        
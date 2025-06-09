from collections import Counter
class Solution:
    def containsDuplicate(self, nums):
        total = Counter(nums)

        for i in total:
            if total[i] > 1:
                return True
        
        return False

obj = Solution()
print(obj.containsDuplicate([1,2,3,4]))
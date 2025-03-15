nums = [3,2,2]
from collections import Counter
class Solution:
    def findErrorNums(self, nums):
        l = [0,0]
        so = Counter(nums)
        for i in range(1, len(nums)+1):
            if so[i] == 0:
                l[1] = i
            if so[i] == 2:
                l[0] = i
        
        return l

obj = Solution()
print(obj.findErrorNums(nums))
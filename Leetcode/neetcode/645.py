nums = [1,2,2,4]
from collections import Counter
class Solution:
    def findErrorNums(self, nums):
        so = Counter(nums)
        mc = so.most_common()
        print(mc)

obj = Solution()
print(obj.findErrorNums(nums))
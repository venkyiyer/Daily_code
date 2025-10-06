from collections import Counter
class Solution:
    def findDuplicates(self, nums):
        res = []
        dc = Counter(nums)

        for k, v in dc.items():
            if v >= 2:
                res.append(k)
        
        return res
    
obj = Solution()
print(obj.findDuplicates([4,3,2,7,8,2,3,1]))
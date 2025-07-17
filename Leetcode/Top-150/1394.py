from collections import Counter
class Solution:
    def findLucky(self,arr):
        count = Counter(arr)
        l = -1
        for k, v in count.items():
            if k == v:
                l = max(k, l)
        
        return l

obj = Solution()
print(obj.findLucky([1,2,2,3,3,3]))

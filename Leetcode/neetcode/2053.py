from collections import Counter
class Solution:
    def kthDistinct(self, arr, k):
        ab = []
        ct = Counter(arr)
        for i in ct:
            if ct[i] == 1:
                ab.append(i)
        
        if len(ab) >= k:
            return ab[k-1]
        else:
            return ""

obj = Solution()
print(obj.kthDistinct(["a","b","a"], k=3))


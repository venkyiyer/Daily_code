from collections import Counter
class Solution:
    def maxDifference(self, s):
        maxodd = 0
        mineven = 100

        c = Counter(s)
        for i in c:
            if c[i]%2 ==0:
                mineven = min(c[i], mineven)
            else:
                maxodd = max(c[i], maxodd)
        
        return maxodd - mineven

obj = Solution()
print(obj.maxDifference(s = "abcabcab"))

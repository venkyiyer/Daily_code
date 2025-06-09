from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        c1 = Counter(s)
        c2 = Counter(t)
        if c1 == c2:
            return True
        return False

obj = Solution()
print(obj.isAnagram(s = "rat", t = "car"))
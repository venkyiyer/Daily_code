s = "loveleetcode"
from collections import Counter
class Solution:
    def firstUniqChar(self,s):
        so = Counter(s)
        for i in range(len(s)):
            if s[i] in so and so[s[i]] ==1:
                return i
        
        return -1

obj = Solution()
print(obj.firstUniqChar(s))

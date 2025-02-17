text = "loonbalxballpoonb"
from collections import Counter

class Solution:
    def maxNumberofBalloons(self, text:str):
        d1 = Counter(text)
        d2 = Counter('balloon')
        
        res = len(text)
        for i in d2:
            res = min(res, d1[i] // d2[i])
        
        return res

obj = Solution()
print(obj.maxNumberofBalloons(text))

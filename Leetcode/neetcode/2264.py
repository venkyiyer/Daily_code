num = "42352338"
from collections import Counter
class Solution:
    def largestGoodInteger(self, num):
        count = 1
        d={}
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                count+=1
                if count>=3:
                    if num[i] in d:
                        d[num[i]]+=1
                    else:
                        d[num[i]]=count
            else:
                count=1

        if d:
            maxElement = max(d)
            return maxElement*3
        else:
            return ""

obj = Solution()
print(obj.largestGoodInteger(num))
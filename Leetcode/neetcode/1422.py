from collections import Counter
s = "01001"
class Solution:
    def maxScore(self, s):
        no_zeros = 0
        no_ones = s.count('1')
        result = 0

        for i in range(len(s)-1):
            if s[i] == '0':
                no_zeros +=1
            else:
                no_ones -=1
            result = max(result, no_zeros+no_ones)
        return result

obj = Solution()
print(obj.maxScore(s))



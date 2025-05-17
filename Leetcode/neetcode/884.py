from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        res = []
        str1 = s1.split(' ')
        str2 = s2.split(' ')
        cnt1 = Counter(str1)
        cnt2 = Counter(str2)
        for i in cnt1:
            if i not in cnt2 and cnt1[i] == 1:
                res.append(i)
        
        for j in cnt2:
            if j not in cnt1 and cnt2[j] == 1:
                res.append(j)
        

        return res

obj = Solution()
print(obj.uncommonFromSentences(s1 = "apple apple", s2 = "banana"))

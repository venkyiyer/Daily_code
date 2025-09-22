class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        res1 = ''
        res2 = ''
        for i in word1:
            res1 += i
        for j in word2:
            res2 += j
        
        return res1 == res2
    

obj = Solution()
print(obj.arrayStringsAreEqual(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]))

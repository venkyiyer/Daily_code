word1 = ["a", "cb"]
word2 = ["ab", "c"]

class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        w1, w2= '', ''
        for i in word1:
            w1 += ''.join(i)
        
        for j in word2:
            w2 += ''.join(j)
        
        if w1 == w2:
            return True
        else:
            return False

obj = Solution()
print(obj.arrayStringsAreEqual(word1, word2))
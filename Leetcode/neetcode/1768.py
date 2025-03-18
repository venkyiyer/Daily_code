word1 = "abcd"
word2 = "pq"

class Solution:
    def mergeAlternatively(self, word1, word2):
        res = ''
        for i in range(min(len(word1), len(word2))):
            res += word1[i] + word2[i]

        
        return res + word1[i+1:] + word2[i+1:]

obj = Solution()
print(obj.mergeAlternatively(word1, word2))

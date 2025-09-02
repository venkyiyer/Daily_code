class Solution:
    def mergeAlternatively(self,word1, word2):
        res = ''
        min_loop = min(len(word1), len(word2))
        for i in range(min_loop):
            res += word1[i]
            res += word2[i]

        res += word1[i+1:] or word2[i+1:]

        return res

obj = Solution()
print(obj.mergeAlternatively(word1 = "abcd", word2 = "pq"))
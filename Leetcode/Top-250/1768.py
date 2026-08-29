class Solution: 
    def mergeAlternately(self, word1, word2):
        total = min(len(word1), len(word2))
        res = ''
        for i in range(total):
            res += word1[i]
            res += word2[i]

        res += word1[total:]
        res+= word2[total:]
        return res

obj = Solution()
print(obj.mergeAlternately(word1 = "abcd", word2 = "pq"))


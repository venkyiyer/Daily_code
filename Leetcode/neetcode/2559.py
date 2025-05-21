class Solution:
    def vowelStrings(self, words, queries):
        vowels = ['a', 'e', 'i', 'o', 'u']
        prefix = [0] * len(words) +1
        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                prefix[i+1] = prefix[i] + 1
            else:
                prefix[i+1] = prefix[i]
        
        res = []
        for q in queries:
            l, r = q
            res.append(prefix[r] - prefix[l])
        
        return res

obj = Solution()
print(obj.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))

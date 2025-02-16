pattern  = "abba"
s = "dog dog dog dog"

class Solution:
    def wordPattern(self, pattern:str, s: str):
        s = s.split()
        if len[s]!= len(pattern):
            return False
        mapper1 = {}
        mapper2 =  {}
        for i, p in enumerate(pattern):
            if ((p in mapper1 and mapper1[p]!= s[i]) or (s[i] in mapper2 and mapper2[s[i]]!=p)) :
                return False
            else:    
                mapper1[p] = s[i]
                mapper2[s[i]] = p
        return True

obj = Solution()
print(obj.wordPattern(pattern, s))
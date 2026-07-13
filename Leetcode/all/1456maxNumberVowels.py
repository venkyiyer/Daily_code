class Solution:
    def maxVowels(self, s, k):
        vowel = {'a', 'e', 'i', 'o', 'u'}
        l, count, res = 0, 0, 0

        for r in range(len(s)):
            if s[r] in vowel:
                count+=1
            else:0
            if r - l + 1 > k:
                count -= 1 if s[l] in vowel else 0
                l +=1
            
            res = max(res, count)

obj = Solution()
obj.maxVowels('abciiidef', 3)

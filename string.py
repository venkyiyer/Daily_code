class Solution:
    def lengthOfLongestSubstring(self, s):
        calc={}
        longest = []
        for index, alphabet in enumerate(s):
            if alphabet in calc:
                calc[alphabet]+=1
                if calc[alphabet] > 1:
                    longest.append(index)
            else:
                calc[alphabet]= 1
            
        return max(longest)

obj = Solution()
obj.lengthOfLongestSubstring('abcabcbb')


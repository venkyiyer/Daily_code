haystack = "leetcode"
needle = "leeto"

class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
    
        for i in range(len(haystack)+1-len(needle)):
            print(len(haystack)+1-len(needle))
            print(haystack[i:i+len(needle)])
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

obj = Solution()
print(obj.strStr(haystack, needle))
class Solution:
    def reverseString(self, s):
        for i in range (len(s)-1,-1,-1):
            s.append(s[i])
            s.pop(i)
            
obj = Solution()
print(obj.reverseString(["h","e","l","l","o"]))
s = "   fly me   to   the moon  "

class Solution:
    def lengthOfLastWord(self,s):
        ws, length = len(s)-1,0

        while s[ws] == " ":
            ws -=1
        while ws >=0 and s[ws] != " ":
            length +=1
            ws-=1
        return length
    
obj = Solution()
print(obj.lengthOfLastWord(s))
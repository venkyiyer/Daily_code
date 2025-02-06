s = "axc"
t = "ahbgdc"

class Solution():
    def isSubsequence(self, s, t):
        pt_s , pt_t = 0,0
        while pt_s < len(s) and pt_t< len(t):
            if s[pt_s] == t[pt_t]:
                pt_s +=1
            pt_t+=1
        
        return pt_s>=len(s)

obj = Solution()
print(obj.isSubsequence(s,t))
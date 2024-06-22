class Solution:
    def isSubsequence(self, s, t):
        pts_s , pts_t =  0,0 
        while pts_s < len(s) and pts_t < len(t):
            if s[pts_s] == t[pts_t]:
                pts_s+=1
            pts_t +=1
        return pts_s>= len(s)
        
obj = Solution()
print(obj.isSubsequence(s = "abc", t = "ahbgdc"))
            




            
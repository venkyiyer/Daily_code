class Solution:
    def isSubsequence(self, s, t):
        len_s = len(s)
        lst = []
        for i in range(len(t)):
            if t[i] in s:
                lst.append(i)
        
        if len(lst)== len_s and lst == sorted(lst):
            return True
        else:
            return False
        
obj = Solution()
print(obj.isSubsequence(s = "acb", t = "ahbgdc"))
            




            
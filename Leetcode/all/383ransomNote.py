class Solution:
    def canConstruct(self, ransomNote, magazine):
        dum = {}
        for i in magazine:
            if i not in dum:
                dum[i]=1 
            else:
                dum[i]+=1
        
        for i in ransomNote:
            if i not in dum and dum[i]<=0:
                return False
            dum[i]-=1
            
        return True

obj = Solution()
print(obj.canConstruct(ransomNote = "aa", magazine = "ab"))

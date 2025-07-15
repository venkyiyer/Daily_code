from collections import Counter
class Solution:
    def canConstruct(self, ransomNote, magazine):
        cntr = Counter(magazine)
        for i in ransomNote:
            if i in cntr:
                if cntr[i] == 0:
                    return False
                else:
                    cntr[i] -=1
            else:
                return False
        
        return True

obj= Solution()
print(obj.canConstruct(ransomNote = "aa", magazine = "aab"))
class Solution:
    def gcdOfStrings(self, str1, str2):
        def isDivisor(l):
            if len(str1) %l or len(str2)%l:
                return False
            f1, f2 = len(str1)//l, len(str2)//l
            return str1[:l]*f1 == str1 and str1[:l] *f2 == str2    

        for l in range(min(len(str1), len(str2)),0,-1):
            if isDivisor(l):
                return str1[:l]
        return ''
    
obj = Solution()
print(obj.gcdOfStrings(str1='ABABAB', str2="ABAB"))
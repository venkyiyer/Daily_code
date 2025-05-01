class Solution:
    def kthCharacter(self,k):
        s = ['a']
        while len(s[0])<k:
            for i in range(len(s[0])):
                append_chr = chr(ord(s[0][i])+1)
                s[0]+=append_chr
            k -=1
        return s[0][k-1]

obj = Solution()
print(obj.kthCharacter(5))
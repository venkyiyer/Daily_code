class Solution:
    def firstPalindrome(self, words) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        
        return ''
        
obj = Solution()
print(obj.firstPalindrome(["def","ghi"])) 
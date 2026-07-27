class Solution:
    def isPalindrome(self, s: str) -> bool:

        def checkalphanumeric(n):
            ((ord('A') <= ord(n) <= ord('Z')) or 
            (ord('a') <= ord(n) <= ord('z')) or
            (ord(0) <= ord(n) <= ord(9)))

        l, r = 0, len(s)-1
        while l<r:
            while l<r and not checkalphanumeric(s[l]):
                l+=1
            while r>l and not checkalphanumeric(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                print('False')
            l,r = l+1, r-1
class Solution:
    def isPalindrome(self,s):
        new_s = ''.join(ele.lower() for ele in s if ele.isalnum())
        if new_s == new_s[::-1]:
            return True

obj=Solution()
print(obj.isPalindrome(s='A man, a plan, a canal: Panama'))

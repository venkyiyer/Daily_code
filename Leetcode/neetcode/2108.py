words = ["def","ghi"]

class Solution:
    def firstPalindrome(self, words):
        for item in words:
            if item[::-1] == item:
                return item
        
        return " "

obj = Solution()
print(obj.firstPalindrome(words))
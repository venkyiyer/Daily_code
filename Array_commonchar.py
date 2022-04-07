class Solution:
    def commonChars(self, words):
        check = list(words[0])
        for word in words:
            newCheck = []
            for c in word:
                if c in check:
                    newCheck.append(c)
                    check.remove(c)
            check = newCheck
        
        return check

obj = Solution()
print(obj.commonChars(["bella","label","roller"]))
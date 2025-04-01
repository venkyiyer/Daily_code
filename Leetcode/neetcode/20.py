s = "()"

class Solution:
    def isValid(self, s):
        stack = []
        braces = {']': '[', '}':'{', ')':'('}

        for i in s:
            if i in braces:
                if stack and stack[-1] == braces[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False

obj = Solution()
print(obj.isValid(s))
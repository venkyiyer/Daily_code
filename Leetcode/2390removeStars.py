class Solution:
    def removeStars(self,s):
        stack = []
        for c in s:
            if c == '*':
                stack and stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)

obj = Solution()
print(obj.removeStars("leet**cod*"))
        
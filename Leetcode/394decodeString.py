class Solution:
    def decodeString(self, s):
        stack = []

        for i in s:
            if i!=']':
                stack.append(i)
            else:
                str = ''
                while stack[-1]!='[':
                    str = stack.pop() + str
                stack.pop()

                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k)*str)    
        
        return ''.join(stack)
    
obj = Solution()
print(obj.decodeString('3[a]2[bc]'))


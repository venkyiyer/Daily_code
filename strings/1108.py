class Solution:
    def defangIPaddr(self, address: str):
        x = address.replace('.', '[.]')
        return x

obj = Solution()
obj,defangIPaddr('1.1.1.1')
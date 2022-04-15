class Solution:
    def isPowerOfThree(self, n):
        while n >= 3:
            if n % 3 != 0:
                return False
            n = n / 3
        return n == 1
            
obj = Solution()
print(obj.isPowerOfThree(45))
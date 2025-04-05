num = 14
import math

class Solution:
    def isPerfectSquare(self, num):
        return True if math.sqrt(num)== math.isqrt(num) else False

obj = Solution()
print(obj.isPerfectSquare(num))
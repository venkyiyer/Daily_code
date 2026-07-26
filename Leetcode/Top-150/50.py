class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -n
        
        return self.power(x, n, 1)

    def power(self, x, n, ans):
        if n ==0:
            return ans

        if n%2 ==1:
            ans = ans * x
        
        return self.power(x *x, n//2, ans)


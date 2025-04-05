n = 10
pick = 6

class Solution:
    def guessNumber(self, n, pick):
        n = [i for i in range(1,n+1)]
        l,r = 0, len(n-1)
        guessNumber = float('inf')

        while guessNumber==0:
            mid = (l+r)//2

            if n[mid] == guessNumber:
                return guessNumber

obj = Solution()
print(obj.guessNumber(n, pick))

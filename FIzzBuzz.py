class Solution:
    def fizzBuzz(self, n: int):
        newL = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5  == 0:
                i = 'FizzBuzz'
            elif i% 3 == 0:
                i = 'Fizz'
            elif i % 5 == 0:
                i = 'Buzz'
            newL.append(str(i))
        return newL 

obj = Solution()
print(obj.fizzBuzz(5))